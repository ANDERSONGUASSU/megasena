"""
Calcula um ID único para um jogo da Mega-Sena.

Returns:
    int: ID único do jogo.
"""
from math import comb


def jogo_para_id(jogo: list[int]) -> int:
    """
    Calcula um ID único para um jogo da Mega-Sena.
    O jogo deve estar ordenado em ordem crescente.
    """
    id_unico = 0
    for i, numero in enumerate(jogo):
        id_unico += comb(numero - 1, i + 1)
    return id_unico
