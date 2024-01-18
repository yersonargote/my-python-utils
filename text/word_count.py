def word_counter(text):
    """Función que cuenta las palabras en un texto dado."""
    return len(text.split())


def run_word_counter():
    print(
        """
---------------------------------------------------------------
    Word Counter
        - Cuenta la cantidad de palabras dado un texto
---------------------------------------------------------------
    Por favor, introduce el texto. Cuando hayas terminado,
    escribe 'EOF' en una nueva línea y presiona Enter:
---------------------------------------------------------------
    """
    )

    lines = []
    while True:
        line = input()
        if line == "EOF":
            break
        lines.append(line)

    text = "\n".join(lines)
    total = word_counter(text)

    print("\nTotal de palabras:")
    print(total)
    print("-------------------------------------------------------")
