"""
Função para gerar todos os jogos possíveis da Mega-Sena.
"""
from itertools import combinations
from math import comb
from tqdm import tqdm
from src.core.ids import jogo_para_id
from src.storage.sqlite import get_connection, close_connection


def gerar_todos_os_jogos() -> None:
    """
    Função para gerar todos os jogos possíveis da Mega-Sena.
    """
    conn = get_connection()
    cursor = conn.cursor()

    mega_sena_numbers = list(range(1, 61))
    batch_size = 1000
    batch = []

    total_combinacoes = comb(60, 6)  # 50.063.860

    # tqdm mostra progresso
    for combo in tqdm(
        combinations(mega_sena_numbers, 6),
        total=total_combinacoes,
        desc='Gerando combinações',
    ):
        id_unico = jogo_para_id(list(combo))
        batch.append((id_unico, *combo))

        if len(batch) == batch_size:
            cursor.executemany(
                'INSERT INTO jogos VALUES (?, ?, ?, ?, ?, ?, ?)', batch
            )
            conn.commit()
            batch = []

    if batch:
        cursor.executemany(
            'INSERT INTO jogos VALUES (?, ?, ?, ?, ?, ?, ?)', batch
        )
        conn.commit()

    conn.commit()
    close_connection(conn)
