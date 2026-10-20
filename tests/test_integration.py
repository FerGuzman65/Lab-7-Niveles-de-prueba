"""Actividad 2: Pruebas de integración (interacción Library + Book + User)."""
import pytest

from book import Book
from user import User
from library import Library


@pytest.fixture
def lib():
    lib = Library()
    lib.add_book(Book("1984", "George Orwell", 1949, "ISBN001"))
    lib.add_user(User("Anna", "U001"))
    lib.add_user(User("Juan", "U002"))
    return lib


# IT-01: se agrega un libro y un usuario pide prestado el libro disponible
def test_it01_borrow_available_book(lib):
    lib.borrow_book("U001", "ISBN001")
    assert lib._find_book("ISBN001").borrowed is True
    assert lib._find_user("U001").get_history() == ["Borrowed: 1984"]


# IT-02: se presta un libro y otro usuario intenta pedirlo -> rechazo
def test_it02_reject_borrow_of_borrowed_book(lib):
    lib.borrow_book("U001", "ISBN001")
    with pytest.raises(ValueError, match="already borrowed"):
        lib.borrow_book("U002", "ISBN001")
    assert lib._find_user("U002").get_history() == []


# IT-03: devolución correcta y nuevo préstamo del mismo libro con otro usuario
def test_it03_return_then_borrow_by_other_user(lib):
    lib.borrow_book("U001", "ISBN001")
    lib.return_book("U001", "ISBN001")
    lib.borrow_book("U002", "ISBN001")
    assert lib._find_book("ISBN001").borrowed is True
    assert lib._find_user("U001").get_history() == ["Borrowed: 1984", "Returned: 1984"]
    assert lib._find_user("U002").get_history() == ["Borrowed: 1984"]
