import pytest
import maior_para_menor

def test_funcao_numeros_em_ordem_decrescente():
    """
    Verifica se a lista desordenada retorna de forma ordenada do maior para o menor
    """
    assert [5, 4, 3, 2, 1] == maior_para_menor.decrescente([3, 5, 1, 2, 4])