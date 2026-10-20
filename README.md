# Lab 7 - Niveles de prueba

Pruebas unitarias, de integración y de sistema con pytest sobre el sistema de biblioteca (`Book`, `User`, `Library`, `main.py`).

Manuel Fernando Guzmán Arias - 4948560

## Cómo correr las pruebas

```
pip install pytest
pytest -v
```

## Casos de prueba

| ID | Nivel | Caso | Resultado |
|----|-------|------|-----------|
| UT-01 | Unidad | `Book.borrow()` marca el libro como prestado | PASA |
| UT-02 | Unidad | `Book.borrow()` dos veces lanza `ValueError` | PASA |
| UT-03 | Unidad | `Book.return_book()` sin préstamo lanza `ValueError` | PASA |
| UT-04 | Unidad | `User.register_borrow()` guarda `Borrowed: <título>` | FALLA |
| UT-05 | Unidad | `User.register_return()` guarda `Returned: <título>` | FALLA |
| UT-06 | Unidad | `Library._find_book()` con ISBN inexistente lanza `ValueError` | PASA |
| UT-07 | Unidad | `Library._find_user()` con usuario existente no imprime error | FALLA |
| IT-01 | Integración | Se agrega un libro y un usuario lo pide prestado | FALLA |
| IT-02 | Integración | Rechazo de préstamo de un libro ya prestado | PASA |
| IT-03 | Integración | Devolución y nuevo préstamo con otro usuario | FALLA |
| ST-01 | Sistema | Menú: pedir prestado y ver historial | FALLA |
| ST-02 | Sistema | Menú: pedir prestado y devolver | FALLA |
| ST-03 | Sistema | Menú: entradas inválidas sin que truene (RNF2) | PASA |

Total: 13 casos, 6 pasan y 7 fallan.

## Errores encontrados

1. `main.py`: las opciones 1 (Borrow) y 2 (Return) del menú están invertidas (ST-01, ST-02).
2. `user.py`: el historial guarda `Borrwed` y `Reurned` (UT-04, UT-05, IT-01, IT-03).
3. `library.py`: `_find_user()` imprime `User not found` cuando sí encuentra al usuario (UT-07).
4. RF6 no está implementado: no hay forma de listar los libros disponibles.
5. `library.py`: con `loans_enabled = False`, `borrow_book()` regresa sin lanzar excepción y `main.py` imprime `Book successfully borrowed` de todos modos (RNF2).

Las pruebas que fallan documentan estos defectos; el código original no se modificó.
