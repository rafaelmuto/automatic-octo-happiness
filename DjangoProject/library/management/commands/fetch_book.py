from django.core.management.base import BaseCommand, CommandError
from datetime import datetime


from library.models import Author, Book
from library.services import OpenLibraryService


class Command(BaseCommand):
    help = (
        "Fetches book and author data from OpenLibrary and stores it in the database."
    )

    def add_arguments(self, parser):
        parser.add_argument("isbn", type=str, help="The ISBN of the book to fetch.")

    def handle(self, *args, **options):
        isbn = options["isbn"]
        self.stdout.write(self.style.NOTICE(f"Fetching book data for ISBN: {isbn}"))

        # Check if the book already exists
        if Book.objects.filter(isbn=isbn).exists():
            self.stdout.write(
                self.style.SUCCESS(f"Book with ISBN {isbn} already exists.")
            )
            return

        # Fetch book data from OpenLibrary
        book_data = OpenLibraryService.search_by_isbn(isbn)
        if not book_data:
            raise CommandError(f"No book found in OpenLibrary with ISBN: {isbn}")

        # Extract the author's OpenLibrary key from the initial data
        author_url = book_data.get("authors", [{}])[0].get("url")
        if not author_url:
            raise CommandError("No author url found in the initial book data.")

        author_key = author_url.split("/")[-2]
        if not author_key:
            raise CommandError("Could not extract author key from the url.")

        # Extract the book's OpenLibrary key
        book_key = book_data.get("key")
        if not book_key:
            # Some responses have the key in a different location
            if "works" in book_data and book_data["works"]:
                book_key = book_data["works"][0].get("key")

        if not book_key:
            raise CommandError("Could not find an OpenLibrary key for the book.")

        book_key = book_key.split("/")[-1]
        if not book_key or not book_key.startswith("OL"):
            raise CommandError("Could not extract book key from the url.")
        
        # Fetch detailed book data using the OpenLibrary key
        detailed_book_data = OpenLibraryService.get_data_by_key(f'/books/{book_key}')
        if not detailed_book_data:
            raise CommandError(
                f"Could not fetch detailed book data for key: {book_key}"
            )

        # Handle the author
        try:
            author = Author.objects.get(olid=author_key)
            self.stdout.write(self.style.SUCCESS(f"Author with key {author_key} already exists."))
        except Author.DoesNotExist:
            author_data = OpenLibraryService.get_data_by_key(f"/authors/{author_key}")
            if not author_data:
                raise CommandError(f"Could not fetch author data for key: {author_key}")

            author_name = author_data.get("name", "Unknown Author")

            birth_date_str = author_data.get("birth_date")
            birth_date = None
            if birth_date_str:
                try:
                    # Attempt to parse different date formats
                    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
                except ValueError:
                    try:
                        birth_date = datetime.strptime(
                            birth_date_str, "%d %B %Y"
                        ).date()
                    except ValueError:
                        self.stdout.write(
                            self.style.WARNING(
                                f"Could not parse birth date: {birth_date_str}"
                            )
                        )

            death_date_str = author_data.get("death_date")
            death_date = None
            if death_date_str:
                try:
                    # Attempt to parse different date formats
                    death_date = datetime.strptime(death_date_str, "%Y-%m-%d").date()
                except ValueError:
                    try:
                        death_date = datetime.strptime(
                            death_date_str, "%d %B %Y"
                        ).date()
                    except ValueError:
                        self.stdout.write(
                            self.style.WARNING(
                                f"Could not parse death date: {death_date_str}"
                            )
                        )

            author = Author.objects.create(
                name=author_name,
                olid=author_key,
                birth_date=birth_date,
                death_date=death_date,
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created author: {author.name}")
            )

        # Create the book
        publish_date_str = detailed_book_data.get("publish_date")
        if not publish_date_str:
            # Fallback to the publish_date from the initial search
            publish_date_str = book_data.get("publish_date")

        publish_date = None
        if publish_date_str:
            try:
                publish_date = datetime.strptime(publish_date_str, "%Y-%m-%d").date()
            except ValueError:
                try:
                    publish_date = datetime.strptime(
                        publish_date_str, "%B %d, %Y"
                    ).date()
                except ValueError:
                    try:
                        publish_date = datetime.strptime(publish_date_str, "%Y").date()
                    except ValueError:
                        try:
                            publish_date = datetime.strptime(
                                publish_date_str, "%Y?"
                            ).date()
                        except ValueError:
                            self.stdout.write(
                                self.style.WARNING(
                                    f"Could not parse publish date: {publish_date_str}"
                                )
                            )

        publisher_list = detailed_book_data.get("publishers", [])
        publisher = publisher_list[0] if publisher_list else None

        book = Book.objects.create(
            title=detailed_book_data.get("title", book_data.get("title")),
            author=author,
            publish_date=publish_date,
            isbn=isbn,
            olid=book_key,
            number_of_pages=detailed_book_data.get(
                "number_of_pages", book_data.get("number_of_pages")
            ),
            publisher=publisher,
        )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created book: {book.title}")
        )
