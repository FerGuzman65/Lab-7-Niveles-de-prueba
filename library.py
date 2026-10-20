from book import Book
from user import User

settings = {
    "loans_enabled": True,
}


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def get_books(self):
        return self.books

    def get_users(self):
        return self.users

    def get_available_books(self):
        return [b for b in self.books if not b.borrowed]

    def borrow_book(self, user_id, isbn):
        if not settings["loans_enabled"]:
            raise ValueError("Loans are disabled")
        user = self._find_user(user_id)
        book = self._find_book(isbn)

        book.borrow()
        user.register_borrow(book)

    def return_book(self, user_id, isbn):
        user = self._find_user(user_id)
        book = self._find_book(isbn)

        book.return_book()
        user.register_return(book)

    def _find_user(self, user_id):
        for u in self.users:
            if u.user_id == user_id:
                return u
        raise ValueError("User not found")

    def _find_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        raise ValueError("Book not found")
