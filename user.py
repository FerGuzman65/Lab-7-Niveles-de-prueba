class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.history = []

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.name == other.name and self.user_id == other.user_id and self.history == other.history

    def register_borrow(self, book):
        self.history.append(f"Borrowed: {book.title}")

    def register_return(self, book):
        self.history.append(f"Returned: {book.title}")

    def get_history(self):
        return self.history
