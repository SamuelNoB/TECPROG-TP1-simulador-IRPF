import pytest
from src.models.Faixas_de_imposto import Faixa_de_imposto

rendimentos = [1, 10, 1000]

faixa_um_valor = [
  (1500, 1500, 0),
]

faixa_dois_valores = [
  (1000, 1000, 0),
  (1903.98, 1903.98, 0),
]

faixa_tres_valores = [
  (0, 0, 0),
  (50, 50, 0),
  (1900, 1900, 0)
]

@pytest.mark.parametrize('rendimento', rendimentos)
def test_faixas_de_imposto_class(rendimento):
  faixa_de_imposto = Faixa_de_imposto(rbt=rendimento)
  assert faixa_de_imposto.rbt == rendimento

@pytest.mark.parametrize(['rendimento', 'valor_base','imposto_esperado'], faixa_um_valor)
def test_faixa_1_um_valor(rendimento, valor_base, imposto_esperado):
  faixa_de_imposto = Faixa_de_imposto(rbt=rendimento)
  imposto_calculado = faixa_de_imposto.calcular_imposto()
  assert imposto_calculado['faixa_1']['valor_imposto'] == imposto_esperado
  assert imposto_calculado['faixa_1']['valor_base'] == valor_base

@pytest.mark.parametrize(['rendimento', 'valor_base','imposto_esperado'], faixa_dois_valores)
def test_faixa_1_dois_valores(rendimento, valor_base, imposto_esperado):
  faixa_de_imposto = Faixa_de_imposto(rbt=rendimento)
  imposto_calculado = faixa_de_imposto.calcular_imposto()
  assert imposto_calculado['faixa_1']['valor_imposto'] == imposto_esperado
  assert imposto_calculado['faixa_1']['valor_base'] == valor_base

@pytest.mark.parametrize(['rendimento', 'valor_base','imposto_esperado'], faixa_tres_valores)
def test_faixa_1_tres_valores(rendimento, valor_base, imposto_esperado):
  faixa_de_imposto = Faixa_de_imposto(rbt=rendimento)
  imposto_calculado = faixa_de_imposto.calcular_imposto()
  assert imposto_calculado['faixa_1']['valor_imposto'] == imposto_esperado
  assert imposto_calculado['faixa_1']['valor_base'] == valor_base