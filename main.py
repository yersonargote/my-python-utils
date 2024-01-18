from typing import Annotated

import typer

from pdf.enums import PDFActions
from pdf.service import run_pdf_action
from text.enums import TXTActions
from text.service import run_text_action

app = typer.Typer(help="Herramienta para manipular archivos de texto y PDFs.")


@app.command(
    "txt",
    help="Manipular texto plano. Acciones: wrdc, rmln.",
)
def txt(
    action: Annotated[
        TXTActions,
        typer.Argument(
            help="Acciones: [wrdc] para contar palabras, [rmln] para remover saltos de línea.",
        ),
    ],
):
    run_text_action(action)


@app.command(
    "pdf",
    help="Manipular archivos PDF. Acciones: split.",
)
def pdf(
    action: Annotated[
        PDFActions,
        typer.Argument(help="Acciones: [split] para extraer páginas dado un rango."),
    ],
):
    run_pdf_action(action)


if __name__ == "__main__":
    app()
