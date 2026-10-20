"""Actividad 3: Pruebas de sistema (caminos completos por el menú de consola)."""
import builtins

import main


def run_with_inputs(monkeypatch, capsys, inputs):
    answers = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(answers))
    main.run()
    return capsys.readouterr().out


# ST-01: opción 1 (Borrow) con libro disponible -> préstamo exitoso y aparece en el historial
def test_st01_borrow_from_menu_and_view_history(monkeypatch, capsys):
    out = run_with_inputs(monkeypatch, capsys, ["1", "ISBN001", "U001", "3", "U001", "0"])
    assert "Book successfully borrowed" in out
    assert "Borrowed: 1984" in out


# ST-02: préstamo (opción 1) y devolución (opción 2) del mismo libro
def test_st02_borrow_then_return_from_menu(monkeypatch, capsys):
    out = run_with_inputs(monkeypatch, capsys, ["1", "ISBN002", "U002", "2", "ISBN002", "U002", "0"])
    assert "Book successfully borrowed" in out
    assert "Book successfully returned" in out
    assert "Error" not in out


# ST-03: entradas inválidas (opción, ISBN y usuario) se manejan sin que el programa truene (RNF2)
def test_st03_invalid_inputs_are_handled(monkeypatch, capsys):
    out = run_with_inputs(monkeypatch, capsys, ["9", "1", "ISBN999", "U001", "3", "U999", "0"])
    assert "Invalid option" in out
    assert "Error: Book not found" in out
    assert "Error: User not found" in out
