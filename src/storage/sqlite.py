"""
Summary:
    Função para obter uma conexão com o banco de dados SQLite.
    Função para fechar a conexão com o banco de dados.
    Função para inicializar o banco de dados.
"""
import sqlite3
from pathlib import Path

DB_PATH = Path('src/data/megasena.db')


def get_connection() -> sqlite3.Connection:
    """
    Função para obter uma conexão com o banco de dados SQLite.

    Returns:
        sqlite3.Connection: Conexão com o banco de dados.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def close_connection(conn: sqlite3.Connection) -> None:
    """
    Função para fechar a conexão com o banco de dados SQLite.

    Args:
        conn (sqlite3.Connection): Conexão com o banco de dados.
    """
    conn.close()


def initialize_database() -> None:
    """
    Função para inicializar o banco de dados SQLite.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number_1 INTEGER NOT NULL,
            number_2 INTEGER NOT NULL,
            number_3 INTEGER NOT NULL,
            number_4 INTEGER NOT NULL,
            number_5 INTEGER NOT NULL,
            number_6 INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    close_connection(conn)
    print('Database initialized.')
