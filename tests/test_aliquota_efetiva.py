from hashlib import new
import pytest
from src.models.Aliquota_efetiva import Aliquota_efetiva

um_caso = [(95.20, 3000, 3.17)]

dois_casos = [(7.20, 2000, 0.36), (376.37, 4500, 8.36)]

tres_casos = [(0, 10, 0), (3255.64, 15000.00, 21.70), (0, 1900, 0)]

@pytest.mark.parametrize(['imposto_total', 'valor_base', 'aliquota_efetiva_esperada'], um_caso)
def test_calculo_aliquota_efetiva(imposto_total, valor_base, aliquota_efetiva_esperada):
  aliquota_efetiva = Aliquota_efetiva(imposto_total, valor_base)
  aliquota_calculada = aliquota_efetiva.calcular_aliquota()
  assert aliquota_calculada == aliquota_efetiva_esperada

@pytest.mark.parametrize(['imposto_total', 'valor_base', 'aliquota_efetiva_esperada'], dois_casos)
def test_calculo_aliquota_efetiva(imposto_total, valor_base, aliquota_efetiva_esperada):
  aliquota_efetiva = Aliquota_efetiva(imposto_total, valor_base)
  aliquota_calculada = aliquota_efetiva.calcular_aliquota()
  assert aliquota_calculada == aliquota_efetiva_esperada

@pytest.mark.parametrize(['imposto_total', 'valor_base', 'aliquota_efetiva_esperada'], tres_casos)
def test_calculo_aliquota_efetiva(imposto_total, valor_base, aliquota_efetiva_esperada):
  aliquota_efetiva = Aliquota_efetiva(imposto_total, valor_base)
  aliquota_calculada = aliquota_efetiva.calcular_aliquota()
  assert aliquota_calculada == aliquota_efetiva_esperada