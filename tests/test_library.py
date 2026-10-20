import book
import pytest
import user
import library


@pytest.mark.unit
def test_borrow_book():
    book1 = book.Book("Orgullo y prejuicio", "Tenoch M.", 2026, "ISBN001")
    assert book1.title == "Orgullo y prejuicio"
    book1.borrow()
    assert book1.borrowed is True


@pytest.mark.unit
def test_borrow_two_times_book():
    book1 = book.Book("Orgullo y prejuicio", "Tenoch M.", 2026, "ISBN001")
    assert book1.title == "Orgullo y prejuicio"
    book1.borrow()

    with pytest.raises(ValueError, match="The book is already borrowed"):
        book1.borrow()


@pytest.mark.unit
def test_return_book():
    book1 = book.Book("Orgullo y prejuicio", "Tenoch M.", 2026, "ISBN001")
    book1.borrow()
    book1.return_book()
    assert book1.borrowed is False


@pytest.fixture
def lib_init():
    lib = library.Library()
    book_tenoch = book.Book("Orgullo y prejuicio", "Tenoch M.", 2026, "ISBN001")
    lib.add_book(book_tenoch)
    tenoch = user.User("Tenoch M.", "U001")
    lib.add_user(tenoch)
    return lib

@pytest.mark.integration
def test_library_init(lib_init):
    lib = lib_init
    lib.borrow_book("U001", "ISBN001")
    assert lib.books[0].borrowed == True

@pytest.mark.integration
def test_library_init_ID_not_registered(lib_init):
    lib = lib_init
    with pytest.raises(ValueError, match="User not found"):
        lib.borrow_book("U999", "ISBN001")
    assert lib.books[0].borrowed == False
