from src.storage.sqlite import get_connection, close_connection


def contar_jogos() -> int:
    """
    Conta o número de jogos na tabela 'jogos'.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM jogos")
    count: int = cursor.fetchone()[0]

    close_connection(conn)
    return count
