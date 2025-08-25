from typing import Generator
from itertools import combinations
from tqdm import tqdm
from src.core.ids import jogo_para_id
from src.storage.sqlite import get_connection, close_connection


RESULTS_FILE = 'megasena-resultados.txt'
BATCH_SIZE = 1000


def gerar_quadras(jogo: list[int]) -> list[tuple[int, int, int, int]]:
    """
    Gera todas as quadras possíveis de um jogo (c(6,4) = 15).
    """
    return list(combinations(sorted(jogo), 4))


def expandir_quadra(
    quadra: tuple[int, int, int, int]
) -> Generator[tuple[int, int, int, int, int, int], None, None]:
    restantes = [n for n in range(1, 61) if n not in quadra]
    return (quadra + comb_extra for comb_extra in combinations(restantes, 2))


def processar_resultados() -> None:
    conn = get_connection()
    cursor = conn.cursor()

    with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        for linha in tqdm(linhas, desc='Processando resultados'):
            # 2903 - 20,24,27,46,50,54
            _, numeros_txt = linha.strip().split(' - ')
            numeros = list(map(int, numeros_txt.split(',')))

            # 1. gerar quadras
            quadras = gerar_quadras(numeros)

            ids_para_deletar = (
                set()
            )  # usar set para evitar duplicatas dentro do concurso

            # 2. expandir quadras e gerar ids
            for quadra in quadras:
                jogos = expandir_quadra(quadra)
                for jogo in jogos:
                    ids_para_deletar.add(jogo_para_id(list(jogo)))

            # 3. deletar em batches
            ids_list = list(ids_para_deletar)
            for i in tqdm(
                range(0, len(ids_list), BATCH_SIZE),
                desc='Deletando jogos',
                leave=False,
            ):
                batch = ids_list[i : i + BATCH_SIZE]
                cursor.executemany(
                    'DELETE FROM jogos WHERE id = ?', [(x,) for x in batch]
                )
                conn.commit()

    close_connection(conn)
