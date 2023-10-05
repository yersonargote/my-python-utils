import typer

from rm_newln import run_rmln
from word_count import run_word_counter

app = typer.Typer()


@app.command()
def rmln():
    """Remove new line of a given text"""
    run_rmln()


@app.command()
def wrdc():
    """Word counter of a given text"""
    run_word_counter()


if __name__ == "__main__":
    app()
