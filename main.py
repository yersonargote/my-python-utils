from typing import Annotated

import typer

from pdf.enums import PDFActions
from pdf.service import run_pdf_action
from text.enums import TXTActions
from text.service import run_text_action

app = typer.Typer()


@app.command("txt")
def txt(
    action: Annotated[
        TXTActions,
        typer.Argument(help="Acción a realizar con el texto. Ex: wrdc, rm_newln"),
    ],
):
    run_text_action(action)


@app.command("pdf")
def pdf(
    action: Annotated[
        PDFActions,
        typer.Argument(help="Acción a realizar con el PDF., Ex: split"),
    ],
):
    run_pdf_action(action)


if __name__ == "__main__":
    app()
