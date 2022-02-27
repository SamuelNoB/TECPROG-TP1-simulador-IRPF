from dataclasses import dataclass
import math

@dataclass
class Faixa_de_imposto:
  rbt: float

  def __post_init__(self) -> None:
      self.tabela_irrf_2022 = {
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
      import math

      def normal_round(n, decimals=0):
        multiplier = 10 ** decimals
        expoN = n * multiplier
        if abs(expoN) - abs(math.floor(expoN)) < 0.5:
          return math.floor(expoN) / multiplier
        return math.ceil(expoN) / multiplier

      # def normal_round(n, decimals=0):
      #   multiplier = 10 ** decimals
      #   return math.ceil(n * multiplier) / multiplier
      self.normal_round = normal_round
 
    
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
    for faixa in self.tabela_irrf_2022:

      valor_maximo_na_faixa = round(self.tabela_irrf_2022[faixa]['max'] - maximo_anterior, 2)
      maximo_anterior = self.tabela_irrf_2022[faixa]['max']

      if(rendimento <= valor_maximo_na_faixa):
        calculado[faixa]['valor_base'] = rendimento
        calculado[faixa]['valor_imposto'] = self.normal_round(self.tabela_irrf_2022[faixa]['aliquota'] * rendimento, 4)
        total_imposto+=calculado[faixa]['valor_imposto'] 
        break
        
      else:
        calculado[faixa]['valor_base'] = valor_maximo_na_faixa
        rendimento = round(rendimento - calculado[faixa]['valor_base'], 2)
        calculado[faixa]['valor_imposto'] = self.normal_round(
          self.tabela_irrf_2022[faixa]['aliquota'] * valor_maximo_na_faixa, 4
          )
        total_imposto+=calculado[faixa]['valor_imposto'] 

    calculado['total']['valor_base'] = self.rbt
    calculado['total']['valor_imposto'] = self.normal_round(total_imposto, 2)
    return calculado