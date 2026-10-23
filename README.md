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

## Pruebas adicionales (Preparación Examen Práctico P2)

Se incorporaron 5 pruebas adicionales (`tests/test_examen.py`) enfocadas en los temas clave del examen práctico que no se habían cubierto en los niveles originales del laboratorio:

1. **`@pytest.mark.parametrize`**: Evalúa en una sola función múltiples combinaciones de entradas no válidas (usuario inexistente, libro inexistente y parámetros vacíos) con `ids` descriptivos y validación de `match`.
2. **`capsys`**: Captura la salida enviada a consola (`stdout`) mediante `print()` para comprobar mensajes de éxito y error en pantalla (`safe_borrow`).
3. **`monkeypatch.delattr`**: Elimina temporalmente atributos opcionales (`year` en `Book`) para comprobar que funciones utilitarias (`describe()`) sean tolerantes a atributos faltantes sin arrojar `AttributeError`.
4. **`pytest.raises` con inspección de `exc_info.value`**: Demuestra la inspección detallada del objeto de excepción capturado (`exc_info.type` y `str(exc_info.value)`) más allá del uso simple de `match`.
5. **Manejo defensivo con `try-except`**: Valida que un método seguro (`safe_borrow`) capture la excepción internamente, imprima el mensaje correspondiente y retorne un booleano (`False` en error, `True` en éxito) sin que pytest registre una excepción no controlada.

Para correr únicamente estas pruebas:
```bash
pytest -m examen -v
```

Total general del proyecto: **28 casos ejecutados y aprobados**.

Reporte: [Lab 7 - Niveles de prueba - Fer Guzman.pdf](Lab%207%20-%20Niveles%20de%20prueba%20-%20Fer%20Guzman.pdf)
