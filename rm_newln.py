import pyperclip


def remove_newlines(text):
    """Función que elimina los saltos de línea de un texto."""
    return text.replace("\n", " ")


def run_rmln():
    print(
        """
----------------------------------------------------------------------------------
    Por favor, introduce el texto.
    Cuando hayas terminado, escribe 'EOF' en una nueva línea y presiona Enter:
----------------------------------------------------------------------------------
        """
    )

    lines = []
    while True:
        line = input()
        if line == "EOF":
            break
        lines.append(line)

    text = "\n".join(lines)
    modified_text = remove_newlines(text)

    # Mostrar el texto modificado en consola
    print("\nTexto modificado:")
    print(modified_text)

    # Copiar el texto modificado al portapapeles
    pyperclip.copy(modified_text)
    print("\nEl texto modificado ha sido copiado al portapapeles.")
    print("----------------------------------------")
