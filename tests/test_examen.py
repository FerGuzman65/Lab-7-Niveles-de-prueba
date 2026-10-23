"""Pruebas adicionales para el Laboratorio 7 (Preparación Examen Práctico Parcial 2).

Temas del examen práctico que no se habían cubierto en los 21 casos originales:
1. @pytest.mark.parametrize (evaluación con múltiples juegos de datos e IDs)
2. capsys (captura y aserción de salida estándar en consola)
3. monkeypatch.delattr (eliminación temporal de atributos para pruebas de robustez)
4. pytest.raises con inspección de exc_info.value (validación detallada del error)
5. try-except (verificación de manejo seguro de excepciones sin propagación)
"""
import pytest
from book import Book, describe
from user import User
from library import Library


@pytest.fixture
def lib_examen():
    """Fixture que inicializa una biblioteca con libros y usuario de prueba."""
    lib = Library()
    lib.add_book(Book("1984", "George Orwell", 1949, "ISBN001"))
    lib.add_book(Book("Moby Dick", "Herman Melville", 1851, "ISBN004"))
    lib.add_user(User("Anna", "U001"))
    return lib


# ----------------------------------------------------------------------
# 1. PARAMETRIZE: Valida múltiples combinaciones con un solo método de prueba
# ----------------------------------------------------------------------
@pytest.mark.examen
@pytest.mark.unit
@pytest.mark.parametrize(
    "user_id, isbn, error_msg",
    [
        ("U999", "ISBN001", "User not found"),
        ("U001", "ISBN999", "Book not found"),
        ("", "", "User not found"),
    ],
    ids=["usuario-inexistente", "libro-inexistente", "entradas-vacias"],
)
def test_adicional_01_parametrize_invalid_inputs(lib_examen, user_id, isbn, error_msg):
    """Verifica que borrow_book arroje ValueError con el mensaje correcto para varias entradas inválidas."""
    with pytest.raises(ValueError, match=error_msg):
        lib_examen.borrow_book(user_id, isbn)


# ----------------------------------------------------------------------
# 2. CAPSYS: Captura y verifica mensajes enviados a stdout por print()
# ----------------------------------------------------------------------
@pytest.mark.examen
@pytest.mark.unit
def test_adicional_02_capsys_safe_borrow_messages(lib_examen, capsys):
    """Verifica la salida por consola al prestar un libro exitosamente y al intentar prestarlo de nuevo."""
    lib_examen.safe_borrow("U001", "ISBN001")
    lib_examen.safe_borrow("U001", "ISBN001")
    captured = capsys.readouterr().out
    assert "Book successfully borrowed\n" in captured
    assert "Error: The book is already borrowed\n" in captured


# ----------------------------------------------------------------------
# 3. MONKEYPATCH.DELATTR: Elimina atributos temporalmente para validar robustez
# ----------------------------------------------------------------------
@pytest.mark.examen
@pytest.mark.unit
def test_adicional_03_delattr_book_without_optional_attribute(monkeypatch):
    """Comprueba que la función describe maneja libros sin atributo 'year' sin lanzar AttributeError."""
    book = Book("1984", "George Orwell", 1949, "ISBN001")
    assert describe(book) == "1984 (1949)"
    monkeypatch.delattr(book, "year")
    assert describe(book) == "1984"


# ----------------------------------------------------------------------
# 4. PYTEST.RAISES CON INSPECCIÓN DE EXC_INFO: Análisis detallado de la excepción
# ----------------------------------------------------------------------
@pytest.mark.examen
@pytest.mark.unit
def test_adicional_04_raises_inspect_exception_value(lib_examen):
    """Inspecciona el objeto de excepción capturado para comprobar mensaje y tipo exacto."""
    with pytest.raises(ValueError) as exc_info:
        lib_examen.borrow_book("U999", "ISBN001")
    assert exc_info.type is ValueError
    assert str(exc_info.value) == "User not found"


# ----------------------------------------------------------------------
# 5. TRY-EXCEPT: Validación de función que atrapa errores y no los propaga
# ----------------------------------------------------------------------
@pytest.mark.examen
@pytest.mark.unit
def test_adicional_05_try_except_defensive_return(lib_examen):
    """Comprueba que safe_borrow captura la excepción internamente, devolviendo False en error y True en éxito."""
    # Usuario inexistente: captura ValueError y regresa False (no debe lanzar excepción a pytest)
    result_error = lib_examen.safe_borrow("U999", "ISBN001")
    assert result_error is False

    # Datos correctos: realiza el préstamo y regresa True
    result_ok = lib_examen.safe_borrow("U001", "ISBN001")
    assert result_ok is True
    assert lib_examen.books[0].borrowed is True
