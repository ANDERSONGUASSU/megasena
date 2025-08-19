import typer
from src.core.combinacoes import gerar_todos_os_jogos
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def gerar_jogos() -> None:
    """Gera todos os jogos da Mega-Sena e salva no banco."""
    console.print('[yellow]⚠️ Atenção! Isso vai gerar 50 milhões de jogos![/yellow]')
    if typer.confirm('Deseja continuar?'):
        gerar_todos_os_jogos()
        console.print('[green]✅ Todos os jogos foram gerados e salvos no banco![/green]')
    else:
        console.print('[red]Operação cancelada[/red]')