import typer
from rich.console import Console
from src.core.verificar_qtd_jogos import contar_jogos

app = typer.Typer()
console = Console()


@app.command()
def total() -> None:
    """Mostra o total de jogos cadastrados."""
    qtd = contar_jogos()
    console.print(f"[bold green]Total de jogos cadastrados:[/bold green] {qtd:,}"
                  .replace(",", ".") + f" de {50_063_860:,}".replace(",", "."))
