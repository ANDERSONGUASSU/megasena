# src/cli/commands.py
import typer
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from src.storage.sqlite import initialize_database, get_connection, close_connection
from src.core.combinacoes import gerar_todos_os_jogos

app = typer.Typer()
console = Console()


@app.command()
def init_db() -> None:
    """Inicializa o banco de dados."""
    initialize_database()
    console.print('[green]✅ Banco de dados inicializado com sucesso![/green]')


@app.command()
def gerar_jogos() -> None:
    """Gera todos os jogos da Mega-Sena e salva no banco."""
    console.print('[yellow]⚠️ Atenção! Isso vai gerar 50 milhões de jogos![/yellow]')
    if typer.confirm('Deseja continuar?'):
        gerar_todos_os_jogos()
        console.print('[green]✅ Todos os jogos foram gerados e salvos no banco![/green]')
    else:
        console.print('[red]Operação cancelada[/red]')


@app.command()
def mostrar_jogos(limit: int = 10) -> None:
    """Mostra os primeiros jogos cadastrados."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM jogos LIMIT ?', (limit,))
    jogos = cursor.fetchall()
    close_connection(conn)

    table = Table(title='Jogos Mega-Sena')
    table.add_column('ID', style='cyan')
    for i in range(1, 7):
        table.add_column(f'N{i}', style='magenta')
    for jogo in jogos:
        table.add_row(str(jogo[0]), *map(str, jogo[1:]))
    console.print(table)


def menu_interativo() -> None:
    console.print("[bold cyan]Bem-vindo ao sistema Mega-Sena CLI[/bold cyan]")
    while True:
        console.print("\n1. Inicializar banco de dados")
        console.print("2. Gerar todos os jogos")
        console.print("3. Mostrar jogos")
        console.print("0. Sair")

        opcao = Prompt.ask("Escolha uma opção", choices=["0", "1", "2", "3"])
        if opcao == "1":
            init_db()
        elif opcao == "2":
            gerar_jogos()
        elif opcao == "3":
            mostrar_jogos()
        elif opcao == "0":
            console.print("👋 Saindo...")
            break

