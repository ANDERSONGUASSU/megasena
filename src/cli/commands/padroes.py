import typer
from rich.console import Console
from src.core.padroes import analisar_padroes

app = typer.Typer()
console = Console()


@app.command()
def analisar_padroes(arquivo: str) -> None:
    """Analisa os padrões de jogos a partir de um arquivo."""
    console.print(f"Analisando padrões no arquivo: {arquivo}")
    # Chama a função de análise de padrões
    analisar_padroes(arquivo)
