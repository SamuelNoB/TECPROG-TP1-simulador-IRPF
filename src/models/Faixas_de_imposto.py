from dataclasses import dataclass

@dataclass
class Faixa_de_imposto:
  rbt: float
    
  def calcular_imposto(self) -> dict:

    return {'faixa_1':{
      'valor_imposto': 0,
      'valor_base':1500
    }}