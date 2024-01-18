from pypdf import PdfReader, PdfWriter

from pdf.constants import OUTPUT_DIR
from utils.print import print


def run_split() -> None:
    path = input("Ubicación del archivo PDF: ")
    pdf: PdfReader = PdfReader(path)
    filename, _ = path.split("/")[-1].split(".")

    print(f"Hay {len(pdf.pages)} páginas en el archivo PDF.")
    print("Elige el rango de páginas que deseas extraer.")
    print("Escribe el número de la primera página.")
    first_page = int(input())
    print("Escribe el número de la última página.")
    last_page = int(input())

    pdf_writer = PdfWriter()
    for page in range(first_page - 1, last_page):
        pdf_writer.add_page(pdf.pages[page])

    output_filename = f"{OUTPUT_DIR}/{filename}_{first_page}_{last_page}.pdf"
    with open(output_filename, "wb") as out:
        pdf_writer.write(out)

        print(f"Se ha creado el archivo {output_filename}")
