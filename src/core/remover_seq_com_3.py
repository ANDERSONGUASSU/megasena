from src.storage.sqlite import get_connection, close_connection


def remover_seq_com_3() -> None:
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM jogos
    WHERE (number_1 + 1 = number_2 AND number_2 + 1 = number_3)
       OR (number_2 + 1 = number_3 AND number_3 + 1 = number_4)
       OR (number_3 + 1 = number_4 AND number_4 + 1 = number_5)
       OR (number_4 + 1 = number_5 AND number_5 + 1 = number_6);
    """

    cursor.execute(query)
    conn.commit()

    print(f"{cursor.rowcount} jogos com 3 números consecutivos foram removidos.")

    close_connection(conn)
