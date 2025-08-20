
import typer
from rich.console import Console
from rich.prompt import Prompt
from .commands import init_db, gerar_jogos, mostrar_jogos, total, remover_jogos, remover_quadras

app = typer.Typer()
console = Console()


def menu_interativo() -> None:
    console.print("[bold cyan]Bem-vindo ao sistema Mega-Sena CLI[/bold cyan]")
    while True:
        console.print("\n1. Inicializar banco de dados")
        console.print("2. Gerar todos os jogos")
        console.print("3. Mostrar jogos")
        console.print("4. Total de jogos")
        console.print("5. Remover jogos com três números consecutivos")
        console.print("6. Remover quadras")
        console.print("0. Sair")

        opcao = Prompt.ask("Escolha uma opção", choices=["0", "1", "2", "3", "4", "5", "6"])
        if opcao == "1":
            init_db()
        elif opcao == "2":
            gerar_jogos()
        elif opcao == "3":
            mostrar_jogos()
        elif opcao == "4":
            total()
        elif opcao == "5":
            remover_jogos()
        elif opcao == "6":
            remover_quadras()
        elif opcao == "0":
            console.print("👋 Saindo...")
            break
