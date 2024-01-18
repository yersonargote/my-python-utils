from rich.console import Console
from rich.markdown import Markdown


def print(text: str) -> None:
    """Print function with rich."""
    console = Console()
    md = Markdown(text)
    console.print(md)
