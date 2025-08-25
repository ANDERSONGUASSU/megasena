import typer
from rich.console import Console
from src.core.remover_seq_com_3 import remover_seq_com_3

app = typer.Typer()
console = Console()


@app.command()
def remover_jogos() -> None:
    """Remove jogos com três números consecutivos."""
    remover_seq_com_3()
    console.print('[bold green]Jogos removidos com sucesso![/bold green]')
