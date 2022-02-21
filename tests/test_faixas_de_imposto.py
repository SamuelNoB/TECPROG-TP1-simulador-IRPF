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

@pytest.mark.parametrize('faixas', [faixa_um_valor, faixa_dois_valores, faixa_tres_valores])
def test_faixa_1_um_valor(faixas):
  for valores in faixas:
    faixa_de_imposto = Faixa_de_imposto(rbt=valores[0])
    imposto_calculado = faixa_de_imposto.calcular_imposto()
    assert imposto_calculado['faixa_1']['valor_base'] == valores[1]
    assert imposto_calculado['faixa_1']['valor_imposto'] == valores[2]
  
# todas as faixas -------------------------------------------------------------------------------

um_caso = [(1500, {
  'faixa_1': { 'valor_imposto': 0, 'valor_base': 1500 },
  'faixa_2': { 'valor_imposto': 0, 'valor_base': 0 },
  'faixa_3': { 'valor_imposto': 0, 'valor_base': 0 },
  'faixa_4': { 'valor_imposto': 0, 'valor_base': 0 },
  'faixa_5': { 'valor_imposto': 0, 'valor_base': 0 },
  'total':{'valor_imposto': 0, 'valor_base':1500 }
  })
]

dois_casos = [
  (1700, {
  'faixa_1': { 'valor_imposto': 0, 'valor_base': 1700 },
  'faixa_2': { 'valor_imposto': 0, 'valor_base': 0 },
  'faixa_3': { 'valor_imposto': 0, 'valor_base': 0 },
  'faixa_4': { 'valor_imposto': 0, 'valor_base': 0 },
  'faixa_5': { 'valor_imposto': 0, 'valor_base': 0 },
  'total':{'valor_imposto': 0, 'valor_base':1700 }
  }),
  (2500, {
  'faixa_1': { 'valor_imposto': 0, 'valor_base': 1903.98 },
  'faixa_2': { 'valor_imposto': 44.7015, 'valor_base': 596.02 },
  'faixa_3': { 'valor_imposto': 0, 'valor_base': 0 },
  'faixa_4': { 'valor_imposto': 0, 'valor_base': 0 },
  'faixa_5': { 'valor_imposto': 0, 'valor_base': 0 },
  'total':{'valor_imposto': 44.70, 'valor_base':2500 }
  })
]

tres_casos = [
  (1900, {
  'faixa_1': { 'valor_imposto': 0, 'valor_base': 1900 },
  'faixa_2': { 'valor_imposto': 0, 'valor_base': 0 },
  'faixa_3': { 'valor_imposto': 0, 'valor_base': 0 },
  'faixa_4': { 'valor_imposto': 0, 'valor_base': 0 },
  'faixa_5': { 'valor_imposto': 0, 'valor_base': 0 },
  'total':{'valor_imposto': 0, 'valor_base':1900 }
  }),

  (4500, {
  'faixa_1': { 'valor_imposto': 0, 'valor_base': 1903.98 },
  'faixa_2': { 'valor_imposto': 69.2003, 'valor_base': 922.67 },
  'faixa_3': { 'valor_imposto': 138.6600, 'valor_base': 924.40 },
  'faixa_4': { 'valor_imposto': 168.5138, 'valor_base': 748.95 },
  'faixa_5': { 'valor_imposto': 0, 'valor_base': 0 },
  'total':{'valor_imposto': 376.37, 'valor_base':4500 }
  }),

  (10000, {
  'faixa_1': { 'valor_imposto': 0, 'valor_base': 1903.98 },
  'faixa_2': { 'valor_imposto': 69.2003, 'valor_base': 922.67 },
  'faixa_3': { 'valor_imposto': 138.6600, 'valor_base': 924.40 },
  'faixa_4': { 'valor_imposto': 205.5668, 'valor_base': 913.63 },
  'faixa_5': { 'valor_imposto': 1467.2130, 'valor_base': 5335.32 },
  'total':{'valor_imposto': 1880.64, 'valor_base':10000 }
  })
]


@pytest.mark.parametrize('casos', [um_caso, dois_casos, tres_casos])
def teste_faixas(casos):
  for dados in casos:
    faixa_de_imposto = Faixa_de_imposto(rbt=dados[0])
    imposto_calculado = faixa_de_imposto.calcular_imposto()
    for faixa in dados[1]:
      print(faixa, '->',dados[1][faixa]['valor_base'], dados[1][faixa]['valor_imposto'], imposto_calculado[faixa]['valor_imposto'] )
      assert dados[1][faixa]['valor_base'] == imposto_calculado[faixa]['valor_base']
      assert dados[1][faixa]['valor_imposto'] == imposto_calculado[faixa]['valor_imposto']