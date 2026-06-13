from rich.console import Console
from rich.theme import Theme
from rich.rule import Rule
from rich.text import Text
from rich.progress import (
    Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
)

_theme = Theme({
    "primary": "bold bright_cyan",
    "success": "bright_green",
    "error": "bold bright_red",
    "warning": "yellow",
    "info": "dim",
})

console = Console(theme=_theme)

_BANNER = r"""
 ██████╗ ██╗   ██╗██████╗ ██████╗ ████████╗
██╔════╝ ██║   ██║██╔══██╗██╔══██╗╚══██╔══╝
██║  ███╗██║   ██║██████╔╝██████╔╝   ██║
██║   ██║╚██╗ ██╔╝██╔══██╗██╔══██╗   ██║
╚██████╔╝ ╚████╔╝ ██║  ██║██║  ██║   ██║
 ╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═╝
"""


def show_banner() -> None:
    console.print(Text(_BANNER, style="bold bright_cyan"))
    console.print(
        Text("  gUrrT · Video RAG CLI", style="dim cyan"),
    )
    console.print(Rule(style="cyan"))


def info(msg: str) -> None:
    console.print(f"[info]  {msg}[/info]")


def success(msg: str) -> None:
    console.print(f"[success]  {msg}[/success]")


def warn(msg: str) -> None:
    console.print(f"[warning]  {msg}[/warning]")


def error(msg: str) -> None:
    console.print(f"[error]  {msg}[/error]")


def step(msg: str) -> None:
    console.print(f"[primary]→[/primary]  {msg}")


def make_progress() -> Progress:
    return Progress(
        SpinnerColumn(style="cyan"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=None, style="cyan", complete_style="bright_cyan"),
        TextColumn("[dim]{task.percentage:>3.0f}%[/dim]"),
        TimeElapsedColumn(),
        console=console,
    )
