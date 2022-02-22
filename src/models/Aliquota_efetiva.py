from dataclasses import dataclass
import math
@dataclass
class Aliquota_efetiva:
  imposto_total:float
  valor_base:float

  def __post_init__(self)->None:
    def normal_round(n, decimals=0):
      multiplier = 10 ** decimals
      expoN = n * multiplier
      if abs(expoN) - abs(math.floor(expoN)) < 0.5:
        return math.floor(expoN) / multiplier
      return math.ceil(expoN) / multiplier
    self.normal_round = normal_round

  def calcular_aliquota(self) -> float:
    return self.normal_round((self.imposto_total / self.valor_base)*100 , 2)