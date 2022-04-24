from dataclasses import dataclass
from ..helpers.custom_round import normal_round


TABELA_IRRF_2022 = {
    "faixa_1": {"min": 0, "max": 1903.98, "aliquota": 0},
    "faixa_2": {"min": 1903.99, "max": 2826.65, "aliquota": 0.075},
    "faixa_3": {"min": 2826.66, "max": 3751.05, "aliquota": 0.15},
    "faixa_4": {"min": 3751.06, "max": 4664.68, "aliquota": 0.225},
    "faixa_5": {"min": 4664.69, "max": float("inf"), "aliquota": 0.275},
}


@dataclass
class Faixa_de_imposto:
    rbt: float

    def calcular_imposto(self) -> dict:
        calculo_imposto = Calculo_imposto(self)
        return calculo_imposto.compute()


@dataclass
class Calculo_imposto:

    total_imposto: float
    maximo_anterior: float

    def __init__(self, faixa_de_imposto: Faixa_de_imposto):
        self.faixa_de_imposto = faixa_de_imposto
        self.total_imposto = 0
        self.maximo_anterior = 0

    def compute(self) -> dict:
        rendimento = self.faixa_de_imposto.rbt
        print(f"rendimento: {rendimento}")
        calculado = {
            "faixa_1": {"valor_imposto": 0, "valor_base": 0},
            "faixa_2": {"valor_imposto": 0, "valor_base": 0},
            "faixa_3": {"valor_imposto": 0, "valor_base": 0},
            "faixa_4": {"valor_imposto": 0, "valor_base": 0},
            "faixa_5": {"valor_imposto": 0, "valor_base": 0},
            "total": {"valor_imposto": 0, "valor_base": 0},
        }
        for faixa in TABELA_IRRF_2022:

            valor_maximo_na_faixa = round(
                TABELA_IRRF_2022[faixa]["max"] - self.maximo_anterior, 2
            )
            self.maximo_anterior = TABELA_IRRF_2022[faixa]["max"]

            if rendimento <= valor_maximo_na_faixa:
                calculado[faixa]["valor_base"] = rendimento
                calculado[faixa]["valor_imposto"] = normal_round(
                    TABELA_IRRF_2022[faixa]["aliquota"] * rendimento, 4
                )
                self.total_imposto += calculado[faixa]["valor_imposto"]
                break

            else:
                calculado[faixa]["valor_base"] = valor_maximo_na_faixa
                rendimento = round(
                    rendimento - calculado[faixa]["valor_base"], 2
                )
                calculado[faixa]["valor_imposto"] = normal_round(
                    TABELA_IRRF_2022[faixa]["aliquota"]
                    * valor_maximo_na_faixa,
                    4,
                )
                self.total_imposto += calculado[faixa]["valor_imposto"]
        calculado["total"]["valor_base"] = self.faixa_de_imposto.rbt
        calculado["total"]["valor_imposto"] = normal_round(
            self.total_imposto, 2
        )
        print(f"calculado: {calculado}")
        return calculado
