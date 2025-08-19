import typer
from rich.console import Console

from src.storage.sqlite import initialize_database

app = typer.Typer()
console = Console()


@app.command()
def init_db() -> None:
    """Inicializa o banco de dados."""
    initialize_database()
    console.print('[green]✅ Banco de dados inicializado com sucesso![/green]')
