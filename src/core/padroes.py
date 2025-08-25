from collections import Counter
from typing import Generator
from math import factorial


# -------------------------------
# Definição dos grupos originais
# -------------------------------
grupos_4 = {
    'G1': set(range(1, 6)) | set(range(11, 16)) | set(range(21, 26)),
    'G2': set(range(6, 11)) | set(range(16, 21)) | set(range(26, 31)),
    'G3': set(range(31, 36)) | set(range(41, 46)) | set(range(51, 56)),
    'G4': set(range(36, 41)) | set(range(46, 51)) | set(range(56, 61)),
}

# -------------------------------
# Novo conjunto: grupos de 10 em 10
# -------------------------------
grupos_6 = {
    'H1': set(range(1, 11)),
    'H2': set(range(11, 21)),
    'H3': set(range(21, 31)),
    'H4': set(range(31, 41)),
    'H5': set(range(41, 51)),
    'H6': set(range(51, 61)),
}


# -------------------------------
# Funções auxiliares
# -------------------------------
def todas_decomposicoes_de_6_em_n(n: int) -> Generator[tuple[int, ...], None, None]:
    """Todas as tuplas (a1,...,an) com soma 6 e cada termo >=0."""
    def gerar(atual, soma, k):
        if k == n - 1:
            yield tuple(atual + [6 - soma])
            return
        for i in range(6 - soma + 1):
            yield from gerar(atual + [i], soma + i, k + 1)

    yield from gerar([], 0, 0)


def prob_teorica(padrao: tuple[int, ...]) -> float:
    """Probabilidade teórica de um padrão (a1,...,an) com p=1/n cada grupo."""
    n = len(padrao)
    total = factorial(6)
    for x in padrao:
        total //= factorial(x)
    return total * ((1 / n) ** 6)


def carregar_resultados(arquivo: str) -> list[tuple[int, ...]]:
    """Carrega resultados no formato 'xxxx - n1,n2,...,n6'."""
    jogos = []
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(' - ')
            if len(partes) != 2:
                continue
            dezenas = tuple(sorted(int(x) for x in partes[1].split(',')))
            if len(dezenas) == 6:
                jogos.append(dezenas)
    return jogos


def classificar_jogo(jogo: tuple[int, ...], grupos: dict[str, set[int]]) -> tuple[int, ...]:
    """Conta quantos números do jogo caem em cada grupo definido."""
    return tuple(sum(1 for n in jogo if n in g) for g in grupos.values())


def analisar_padroes(arquivo: str, grupos: dict[str, set[int]]) -> None:
    jogos = carregar_resultados(arquivo)

    # Conta frequência dos padrões
    padroes = [classificar_jogo(j, grupos) for j in jogos]
    freq = Counter(padroes)

    # Gera ranking incluindo padrões que não saíram
    ranking = []
    for padrao in todas_decomposicoes_de_6_em_n(len(grupos)):
        ranking.append((padrao, freq.get(padrao, 0), prob_teorica(padrao)))

    # Ordena por frequência (decrescente)
    ranking.sort(key=lambda x: x[1], reverse=True)

    # Exibir resultado
    print(f"\n=== Análise para {len(grupos)} grupos ===")
    print(f"{'Padrão':<25}{'Frequência':<12}{'Prob Teórica':<15}")
    print('-' * 55)
    for padrao, f, p in ranking:
        print(f'{padrao!s:<25}{f:<12}{p:.6f}')
