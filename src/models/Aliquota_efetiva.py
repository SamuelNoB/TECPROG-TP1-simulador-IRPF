from dataclasses import dataclass
from ..helpers.custom_round import normal_round


@dataclass
class Aliquota_efetiva:
    imposto_total: float
    valor_base: float

    def calcular_aliquota(self) -> float:
        return normal_round((self.imposto_total / self.valor_base) * 100, 2)

