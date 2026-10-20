"""Actividad 1: Pruebas unitarias (métodos individuales de Book, User y Library)."""
import pytest

from book import Book
from user import User
from library import Library

pytestmark = pytest.mark.unit


def make_book():
    return Book("1984", "George Orwell", 1949, "ISBN001")


# UT-01: un libro nuevo inicia disponible y borrow() lo marca como prestado
def test_ut01_book_borrow_marks_as_borrowed():
    book = make_book()
    assert book.borrowed is False
    book.borrow()
    assert book.borrowed is True


# UT-02: borrow() sobre un libro ya prestado lanza ValueError
def test_ut02_book_borrow_twice_raises():
    book = make_book()
    book.borrow()
    with pytest.raises(ValueError, match="already borrowed"):
        book.borrow()


# UT-03: return_book() sobre un libro no prestado lanza ValueError
def test_ut03_book_return_not_borrowed_raises():
    book = make_book()
    with pytest.raises(ValueError, match="not currently borrowed"):
        book.return_book()


# UT-04: register_borrow() guarda el préstamo en el historial con el texto correcto
def test_ut04_user_register_borrow_history_text():
    user = User("Anna", "U001")
    user.register_borrow(make_book())
    assert user.get_history() == ["Borrowed: 1984"]


# UT-05: register_return() guarda la devolución en el historial con el texto correcto
def test_ut05_user_register_return_history_text():
    user = User("Anna", "U001")
    user.register_return(make_book())
    assert user.get_history() == ["Returned: 1984"]


# UT-06: _find_book() con un ISBN inexistente lanza ValueError
def test_ut06_library_find_book_not_found_raises():
    lib = Library()
    lib.add_book(make_book())
    with pytest.raises(ValueError, match="Book not found"):
        lib._find_book("ISBN999")


# UT-07: _find_user() con un usuario existente lo regresa sin imprimir "User not found"
def test_ut07_library_find_existing_user_no_error_message(capsys):
    lib = Library()
    user = User("Anna", "U001")
    lib.add_user(user)
    assert lib._find_user("U001") is user
    assert "User not found" not in capsys.readouterr().out


# UT-08: get_available_books() regresa solo los libros que no están prestados (RF6)
def test_ut08_library_get_available_books():
    lib = Library()
    b1 = make_book()
    b2 = Book("Moby Dick", "Herman Melville", 1851, "ISBN004")
    lib.add_book(b1)
    lib.add_book(b2)
    b1.borrow()
    assert lib.get_available_books() == [b2]
