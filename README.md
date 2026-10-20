# Lab 7 - Niveles de prueba

Pruebas unitarias, de integración y de sistema con pytest sobre el sistema de biblioteca (`Book`, `User`, `Library`, `main.py`).

Manuel Fernando Guzmán Arias - 4948560

## Cómo correr las pruebas

```
pip install pytest
pytest -v
```

## Casos de prueba

Primero se corrieron 13 casos sobre el código original (6 pasan, 7 fallan). Después se corrigió el código y se agregaron UT-08, IT-04 y ST-04, más las pruebas de clase en `tests/test_library.py`.

| ID | Nivel | Caso | Código original | Código corregido |
|----|-------|------|-----------------|------------------|
| UT-01 | Unidad | `Book.borrow()` marca el libro como prestado | PASA | PASA |
| UT-02 | Unidad | `Book.borrow()` dos veces lanza `ValueError` | PASA | PASA |
| UT-03 | Unidad | `Book.return_book()` sin préstamo lanza `ValueError` | PASA | PASA |
| UT-04 | Unidad | `User.register_borrow()` guarda `Borrowed: <título>` | FALLA | PASA |
| UT-05 | Unidad | `User.register_return()` guarda `Returned: <título>` | FALLA | PASA |
| UT-06 | Unidad | `Library._find_book()` con ISBN inexistente lanza `ValueError` | PASA | PASA |
| UT-07 | Unidad | `Library._find_user()` con usuario existente no imprime error | FALLA | PASA |
| UT-08 | Unidad | `Library.get_available_books()` (RF6) | — | PASA |
| IT-01 | Integración | Se agrega un libro y un usuario lo pide prestado | FALLA | PASA |
| IT-02 | Integración | Rechazo de préstamo de un libro ya prestado | PASA | PASA |
| IT-03 | Integración | Devolución y nuevo préstamo con otro usuario | FALLA | PASA |
| IT-04 | Integración | Préstamos deshabilitados lanzan `ValueError` (RNF2) | — | PASA |
| ST-01 | Sistema | Menú: pedir prestado y ver historial | FALLA | PASA |
| ST-02 | Sistema | Menú: pedir prestado y devolver | FALLA | PASA |
| ST-03 | Sistema | Menú: entradas inválidas sin que truene (RNF2) | PASA | PASA |
| ST-04 | Sistema | Menú: listado de libros disponibles (RF6) | — | PASA |

Resultado final: 21 pruebas, todas pasan. Por nivel: `pytest -m unit`, `pytest -m integration`, `pytest -m system`.

## Errores encontrados y corrección

1. `main.py`: las opciones 1 (Borrow) y 2 (Return) del menú estaban invertidas. Se corrigió.
2. `user.py`: el historial guardaba `Borrwed` y `Reurned`. Corregido en clase.
3. `library.py`: `_find_user()` imprimía `User not found` cuando sí encontraba al usuario. Corregido en clase.
4. RF6 no estaba implementado. Se agregó `Library.get_available_books()` y la opción 4 del menú.
5. `library.py`: con `loans_enabled = False`, `borrow_book()` regresaba sin error y el menú decía `Book successfully borrowed`. Ahora lanza `ValueError("Loans are disabled")`.

Reporte: [Lab 7 - Niveles de prueba - Fer Guzman.pdf](Lab%207%20-%20Niveles%20de%20prueba%20-%20Fer%20Guzman.pdf)
