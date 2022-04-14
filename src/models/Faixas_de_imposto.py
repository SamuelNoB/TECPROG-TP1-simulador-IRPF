from dataclasses import dataclass
from ..helpers.custom_round import normal_round


TABELA_IRRF_2022 = {
        'faixa_1':{
          'min': 0,
          'max':1903.98,
          'aliquota': 0
        },
        'faixa_2':{
          'min': 1903.99,
          'max':2826.65,
          'aliquota': 0.075
        },
        'faixa_3':{
          'min': 2826.66,
          'max':3751.05,
          'aliquota': 0.15
        },
        'faixa_4':{
          'min': 3751.06,
          'max':4664.68,
          'aliquota': 0.225
        },
        'faixa_5':{
          'min': 4664.69,
          'max':float('inf'),
          'aliquota': 0.275
        },
      }
@dataclass
class Faixa_de_imposto:
  rbt: float

  def calcular_imposto(self) -> dict:
    rendimento = self.rbt
    total_imposto = 0
    calculado = {
      'faixa_1': { 'valor_imposto': 0, 'valor_base': 0 },
      'faixa_2': { 'valor_imposto': 0, 'valor_base': 0 },
      'faixa_3': { 'valor_imposto': 0, 'valor_base': 0 },
      'faixa_4': { 'valor_imposto': 0, 'valor_base': 0 },
      'faixa_5': { 'valor_imposto': 0, 'valor_base': 0 },
      'total':{'valor_imposto': 0, 'valor_base':0 }
    }
    maximo_anterior = 0
    for faixa in TABELA_IRRF_2022:

      valor_maximo_na_faixa = round(TABELA_IRRF_2022[faixa]['max'] - maximo_anterior, 2)
      maximo_anterior = TABELA_IRRF_2022[faixa]['max']

      if(rendimento <= valor_maximo_na_faixa):
        calculado[faixa]['valor_base'] = rendimento
        calculado[faixa]['valor_imposto'] = normal_round(TABELA_IRRF_2022[faixa]['aliquota'] * rendimento, 4)
        total_imposto+=calculado[faixa]['valor_imposto'] 
        break
        
      else:
        calculado[faixa]['valor_base'] = valor_maximo_na_faixa
        rendimento = round(rendimento - calculado[faixa]['valor_base'], 2)
        calculado[faixa]['valor_imposto'] = normal_round(
          TABELA_IRRF_2022[faixa]['aliquota'] * valor_maximo_na_faixa, 4
          )
        total_imposto+=calculado[faixa]['valor_imposto'] 

    calculado['total']['valor_base'] = self.rbt
    calculado['total']['valor_imposto'] = normal_round(total_imposto, 2)
    return calculado