from pdf.enums import PDFActions
from pdf.split import run_split


def run_pdf_action(action: PDFActions):
    match action:
        case PDFActions.SPLIT:
            run_split()
