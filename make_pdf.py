import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

pdf_filename = "Evidencia - Avance Lab 7 - Fer Guzman.pdf"
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=letter,
    rightMargin=45,
    leftMargin=45,
    topMargin=35,
    bottomMargin=35
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "DocTitle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=13,
    leading=17,
    textColor=colors.HexColor("#1a1a1a")
)

subtitle_style = ParagraphStyle(
    "DocSubtitle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9.5,
    leading=14,
    textColor=colors.HexColor("#333333")
)

h1_style = ParagraphStyle(
    "H1",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=11,
    leading=15,
    spaceBefore=8,
    spaceAfter=4,
    textColor=colors.HexColor("#1a1a1a")
)

body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9,
    leading=13,
    textColor=colors.HexColor("#222222")
)

story = []

# Encabezado institucional
logo_path = "c:/Users/solac/OneDrive - Universidad Autonoma de Guadalajara/UAG/UAGLOGO.png"

info_text = """<b>Universidad Autónoma de Guadalajara</b><br/>
Pruebas de software — Parcial 2<br/>
<b>Actividad: Laboratorio #7 — Pruebas Adicionales (Preparación Examen Práctico)</b><br/>
Alumno: Manuel Fernando Guzmán Arias &nbsp;|&nbsp; Código: 4948560<br/>
Carrera: Ingeniería de Software y Minería de Datos &nbsp;|&nbsp; Fecha: 23 de octubre de 2026<br/>
<b>Repositorio GitHub:</b> https://github.com/FerGuzman65/Lab-7-Niveles-de-prueba"""

if os.path.exists(logo_path):
    logo = RLImage(logo_path, width=1.35*inch, height=0.71*inch)
    header_table = Table([[logo, Paragraph(info_text, subtitle_style)]], colWidths=[1.5*inch, 5.7*inch])
    header_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(header_table)
else:
    story.append(Paragraph(info_text, subtitle_style))

story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cccccc"), spaceBefore=2, spaceAfter=8))

# Sección 1
story.append(Paragraph("1. Descripción de la actividad y selección de temas", h1_style))
desc_text = """Para dar cumplimiento a la actividad del Laboratorio #7, se agregaron <b>cinco pruebas adicionales</b> priorizando los temas clave del examen práctico de Parcial 2 que no habían sido repasados en los niveles originales del laboratorio:<br/><br/>
1. <b>@pytest.mark.parametrize</b>: Evaluación de una misma prueba contra múltiples combinaciones de datos inválidos utilizando IDs descriptivos y verificación con <code>match</code>.<br/>
2. <b>Fixture capsys</b>: Captura y validación de la salida enviada a consola (<code>stdout</code>) mediante <code>print()</code>.<br/>
3. <b>monkeypatch.delattr</b>: Eliminación temporal de atributos opcionales en objetos para comprobar la tolerancia a atributos faltantes sin generar <code>AttributeError</code>.<br/>
4. <b>pytest.raises con inspección de exc_info.value</b>: Inspección explícita del objeto de excepción para validar el tipo exacto y el contenido textual del error.<br/>
5. <b>Manejo defensivo con try-except</b>: Validación de métodos que atrapan excepciones internamente sin propagarlas hacia pytest, retornando códigos de error o booleanos."""
story.append(Paragraph(desc_text, body_style))
story.append(Spacer(1, 6))

# Sección 2
story.append(Paragraph("2. Detalle de las pruebas implementadas (tests/test_examen.py)", h1_style))
pruebas_detail = """• <b>test_adicional_01_parametrize_invalid_inputs</b>: Aplica <code>@pytest.mark.parametrize</code> para verificar que <code>borrow_book</code> lance <code>ValueError</code> con el mensaje exacto para: usuario inexistente (<code>U999</code>), libro inexistente (<code>ISBN999</code>) y valores vacíos.<br/>
• <b>test_adicional_02_capsys_safe_borrow_messages</b>: Utiliza la fixture <code>capsys</code> para comprobar que <code>safe_borrow</code> imprima en consola <i>\"Book successfully borrowed\"</i> y posteriormente <i>\"Error: The book is already borrowed\"</i>.<br/>
• <b>test_adicional_03_delattr_book_without_optional_attribute</b>: Emplea <code>monkeypatch.delattr(book, 'year')</code> para comprobar que la función <code>describe()</code> formatee la información del libro aun cuando no contenga el atributo de año.<br/>
• <b>test_adicional_04_raises_inspect_exception_value</b>: Emplea <code>with pytest.raises(ValueError) as exc_info:</code> para validar que <code>exc_info.type is ValueError</code> y que <code>str(exc_info.value) == 'User not found'</code>.<br/>
• <b>test_adicional_05_try_except_defensive_return</b>: Valida que el método <code>safe_borrow</code> capture la excepción internamente con <code>try-except</code>, retornando <code>False</code> en caso de error y <code>True</code> en caso de préstamo exitoso."""
story.append(Paragraph(pruebas_detail, body_style))
story.append(Spacer(1, 8))

# Sección 3
story.append(Paragraph("3. Evidencia de ejecución en pytest (Capturas de pantalla)", h1_style))
story.append(Paragraph("<b>A. Ejecución de las 5 pruebas de preparación para el examen (pytest -m examen -v):</b>", body_style))
story.append(Spacer(1, 4))
if os.path.exists("captura_pytest_examen.png"):
    img1 = RLImage("captura_pytest_examen.png", width=7.0*inch, height=2.3*inch)
    story.append(img1)

story.append(PageBreak())

story.append(Paragraph("<b>B. Ejecución completa del proyecto (pytest -v — 28 casos en total):</b>", body_style))
story.append(Spacer(1, 4))
if os.path.exists("captura_pytest_total.png"):
    img2 = RLImage("captura_pytest_total.png", width=7.0*inch, height=5.5*inch)
    story.append(img2)

story.append(Spacer(1, 10))
story.append(Paragraph("4. Enlace del Repositorio Remoto", h1_style))
repo_p = """El repositorio remoto actualizado con los commits de estas pruebas adicionales y el código corregido se encuentra disponible en:<br/>
<b>https://github.com/FerGuzman65/Lab-7-Niveles-de-prueba</b>"""
story.append(Paragraph(repo_p, body_style))

story.append(Spacer(1, 8))
story.append(Paragraph("5. Conclusiones", h1_style))
concl_p = """La implementación de estas cinco pruebas adicionales permitió repasar de manera práctica los conceptos clave no cubiertos en las pruebas iniciales del laboratorio: parametrización de casos de prueba con <code>@pytest.mark.parametrize</code> para reducir código redundante, validación de salidas de consola con <code>capsys</code>, pruebas de robustez mediante simulación de atributos faltantes con <code>monkeypatch.delattr</code>, inspección profunda del tipo y mensaje de error con <code>pytest.raises</code> y el manejo controlado de errores defensivos mediante <code>try-except</code>. Estos ejercicios consolidan los conocimientos necesarios para el examen práctico de la materia."""
story.append(Paragraph(concl_p, body_style))

doc.build(story)
print("PDF generado exitosamente:", pdf_filename)
