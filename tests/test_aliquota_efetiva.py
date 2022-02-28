from hashlib import new
import pytest
from src.models.Aliquota_efetiva import Aliquota_efetiva

um_caso = [(95.20, 3000)]

@pytest.mark.parametrize(['imposto_total', 'valor_base'], um_caso)
def test_calculo_aliquota_efetiva(imposto_total, valor_base):
  aliquota_efetiva = Aliquota_efetiva(imposto_total, valor_base)
  aliquota_calculada = aliquota_efetiva.calcular_aliquota()
  assert aliquota_calculada == 3.17
    