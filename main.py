from src.models.Aliquota_efetiva import Aliquota_efetiva
from src.models.Faixas_de_imposto import Faixa_de_imposto
from src.models.Rendimento import Rendimento
from src.controllers.RendimentoController import RendimentoController

value = int(input("Quantos rendimentos voce deseja cadastrar? "))

rendimentos = []
for i in range(value):
    desc = input(
        "Digite a descrição do seu rendimento (valores positivos) ou dedução (valores negativos): "
    )
    valor = float(
        input(
            "Digite o valor desse rendimento (valores positivos) ou dedução (valores negativos): "
        )
    )
    rendimentos.append(Rendimento(desc, valor))

total_rendimentos = RendimentoController(rendimentos)

rbt = total_rendimentos.count_total_rendimento_value()

faixa = Faixa_de_imposto(rbt)

calculado = faixa.calcular_imposto()

for i in calculado:
    print(f"{i}:   ")
    print(f"    Valor imposto: {calculado[i]['valor_imposto']}")
    print(f"    Valor base: {calculado[i]['valor_base']}")

aliquota_efetiva = Aliquota_efetiva(
    calculado["total"]["valor_imposto"], calculado["total"]["valor_base"]
)

print(f"\n\nAliquota efetiva - {aliquota_efetiva.calcular_aliquota()}")
