from desconto.desconto import calcular_desconto
import pytest


def test_des_menor_0():
    with pytest.raises(ValueError, match="O desconto deve estar entre 0 e 100."):
        calcular_desconto(10, -2)

def test_des_maior_100():
    with pytest.raises(ValueError, match="O desconto deve estar entre 0 e 100."):
        calcular_desconto(90, 120)

def test_val_n_numerico():
    with pytest.raises(TypeError, match="Erro: O valor total e o desconto devem ser numéricos."):
        calcular_desconto("oito", 20)

def test_val_des_vazios():
    with pytest.raises(TypeError, match="Erro: O valor total e o desconto devem ser numéricos."):
        calcular_desconto(None, None)

def test_so_um_for_informado():
    with pytest.raises(TypeError, match="Erro: O valor total e o desconto devem ser numéricos."):
        calcular_desconto(13, None)

def test_negativo():
    with pytest.raises(ValueError, match="O valor do produto não pode ser negativo."):
        calcular_desconto(-11, 20)
    