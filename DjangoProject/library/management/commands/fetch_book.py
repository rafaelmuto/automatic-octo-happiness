import json
from django.core.management.base import BaseCommand, CommandError
from library.services import OpenLibraryService

class Command(BaseCommand):
    help = 'Fetches book data from the OpenLibrary API using a given ISBN'

    def add_arguments(self, parser):
        parser.add_argument('isbn', type=str, help='The ISBN of the book to fetch.')

    def handle(self, *args, **options):
        isbn = options['isbn']
        self.stdout.write(self.style.NOTICE(f'Fetching book data for ISBN: {isbn}'))

        try:
            book_data = OpenLibraryService.search_by_isbn(isbn)
            if book_data:
                self.stdout.write(self.style.SUCCESS('Successfully fetched book data:'))
                # Pretty print the JSON response
                self.stdout.write(json.dumps(book_data, indent=4))
            else:
                raise CommandError('Book not found or API error.')

        except Exception as e:
            raise CommandError(f'An error occurred: {e}')
