from desconto.desconto import calcular_desconto
import pytest


@pytest.mark.parametrize("valor, desconto, esperado",
                         [
                             [80, 10, 72.00],
                             [54.87, 13, 47.74],
                             [600, 12.50, 525.00],
                             [154.98, 3.5, 149.56],
                             [10,  0, 10.00],
                             [10, 100, 0.00],
                             [0.50, 30, 0.35]
                         ],
                         ids=[
                             "valor inteiro",
                             "valor decimal",
                             "desconto decimal",
                             "valor e desconto decimal",
                             "desconto 0",
                             "desconto 100",
                             "valor em centavos"
                         ])
def test_boletim_happy_patch(valor, desconto, esperado):
    assert calcular_desconto(valor, desconto) == esperado

