from dataclasses import dataclass
import math
@dataclass
class Aliquota_efetiva:
  imposto_total:float
  valor_base:float

  @staticmethod
  def decimal_part(number: float) -> float:
    return abs(number) - abs(math.floor(number))

  def normal_round(self, n, decimals=0):
    multiplier = 10 ** decimals
    expoN = n * multiplier
    if self.decimal_part(expoN) < 0.5:
      return math.floor(expoN) / multiplier
    return math.ceil(expoN) / multiplier

  def calcular_aliquota(self) -> float:
    return self.normal_round((self.imposto_total / self.valor_base)*100, 2)