class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.borrowed = False

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (
            self.title,
            self.author,
            self.year,
            self.isbn,
            self.borrowed,
        ) == (
            other.title,
            other.author,
            other.year,
            other.isbn,
            other.borrowed,
        )

    def borrow(self):
        if self.borrowed:
            raise ValueError("The book is already borrowed")
        self.borrowed = True

    def return_book(self):
        if not self.borrowed:
            raise ValueError("The book is not currently borrowed")
        self.borrowed = False


def describe(book):
    """Ficha informativa del libro; si el objeto no tiene año, no truena."""
    if hasattr(book, "year"):
        return f"{book.title} ({book.year})"
    return book.title
