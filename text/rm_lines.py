import pyperclip

from text.constants import EOF, NEWLINE, REMOVE_NEWLINES_INSTRUCTIONS, SPACE
from utils.print import print


def remove_newlines(text) -> None:
    """Función que elimina los saltos de línea de un texto."""
    return text.replace(NEWLINE, SPACE)


def run_rmln() -> None:
    print(REMOVE_NEWLINES_INSTRUCTIONS)

    lines = []
    while True:
        line = input()
        if line == EOF:
            break
        lines.append(line)

    text = NEWLINE.join(lines)
    modified_text = remove_newlines(text)

    # Mostrar el texto modificado en consola
    print(f"{NEWLINE}Texto modificado:")
    print(modified_text)

    # Copiar el texto modificado al portapapeles
    pyperclip.copy(modified_text)
    print(f"{NEWLINE}El texto modificado ha sido copiado al portapapeles.")
    print("---")
