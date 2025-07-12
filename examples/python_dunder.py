
class Book:
    """
    Represents a single book with a title and author.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # __repr__: "Official" string representation.
    # Called by the `repr()` function. Its goal is to be unambiguous
    # and ideally should return an expression that can recreate the object.
    # It's a fallback for __str__ if it's not defined.
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

    # __str__: "Informal" or user-friendly string representation.
    # Called by `str()` and `print()`. It's for display to the end user.
    def __str__(self):
        return f'"{self.title}" by {self.author}'


class Library:
    """
    Represents a collection of books.
    """
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the {self.name} library.")

    # __len__: Defines behavior for the `len()` function.
    # It should return the number of items in the container.
    def __len__(self):
        return len(self.books)

    # __getitem__: Defines behavior for accessing items using square brackets (like a list).
    # This is called when you do `my_library[index]`.
    def __getitem__(self, index):
        return self.books[index]

    # __add__: Defines behavior for the `+` operator.
    # Here, we'll use it to combine two libraries into a new one.
    def __add__(self, other_library):
        new_library_name = f"{self.name} & {other_library.name}"
        new_library = Library(new_library_name)
        new_library.books = self.books + other_library.books
        return new_library


# --- Using the Classes and their Dunder Methods ---

# Create some book instances
book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("Dune", "Frank Herbert")
book3 = Book("1984", "George Orwell")

# --- __str__ vs __repr__ ---
print("--- str vs repr ---")
print(str(book1))  # Calls book1.__str__()
print(repr(book1)) # Calls book1.__repr__()
print("-" * 20)


# --- __len__ and __getitem__ ---
print("--- len and getitem ---")
my_library = Library("Central")
my_library.add_book(book1)
my_library.add_book(book2)

print(f"The library has {len(my_library)} books.") # Calls my_library.__len__()
print(f"The first book is: {my_library[0]}")   # Calls my_library.__getitem__(0)
print("-" * 20)


# --- __add__ ---
print("--- add ---")
other_library = Library("Westside")
other_library.add_book(book3)

combined_library = my_library + other_library # Calls my_library.__add__(other_library)

print(f"Combined library name: {combined_library.name}")
print(f"Combined library has {len(combined_library)} books:")
for book in combined_library: # This works because __getitem__ makes the class iterable
    print(f"- {book}")
print("-" * 20)
