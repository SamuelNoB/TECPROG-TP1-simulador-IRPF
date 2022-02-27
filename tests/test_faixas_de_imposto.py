import pytest
from src.models.Faixas_de_imposto import Faixa_de_imposto

rendimentos = [1, 10, 1000]

faixa_1 = [
  (1500, 1500, 0),
]

@pytest.mark.parametrize('rendimento', rendimentos)
def test_faixas_de_imposto_class(rendimento):
  faixa_de_imposto = Faixa_de_imposto(rbt=rendimento)
  assert faixa_de_imposto.rbt == rendimento

@pytest.mark.parametrize(['rendimento', 'valor_base','imposto_esperado'], faixa_1)
def test_faixa_1(rendimento, valor_base, imposto_esperado):
  faixa_de_imposto = Faixa_de_imposto(rbt=rendimento)
  imposto_calculado = faixa_de_imposto.calcular_imposto()
  assert imposto_calculado['faixa_1']['valor_imposto'] == imposto_esperado
  assert imposto_calculado['faixa_1']['valor_base'] == valor_base

