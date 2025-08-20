import typer
from rich.console import Console
from src.core.remover_quadra import processar_resultados

app = typer.Typer()
console = Console()


@app.command()
def remover_quadras() -> None:
    """Remove quadras da tabela de jogos."""
    processar_resultados()
