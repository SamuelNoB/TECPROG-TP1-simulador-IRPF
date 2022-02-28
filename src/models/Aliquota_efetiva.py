from dataclasses import dataclass

@dataclass
class Aliquota_efetiva:
  imposto_total:float
  valor_base:float

  def calcular_aliquota(self) -> float:
    return round((self.imposto_total / self.valor_base)*100 , 2)