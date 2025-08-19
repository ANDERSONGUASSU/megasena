
import typer
from rich.console import Console
from rich.table import Table
from src.storage.sqlite import get_connection, close_connection

app = typer.Typer()
console = Console()


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
