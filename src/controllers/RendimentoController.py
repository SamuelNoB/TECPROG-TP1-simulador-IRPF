from ..models.Rendimento import Rendimento


class RendimentoController:
    """
    Classe responsável por fazer o gerenciamento de um conjunto de rendimentos
    """
    def __init__(self, rendimentos=[]) -> None:
        self.__rendimentos = rendimentos

    def add(self, valor: float, descricao: str) -> Rendimento:
        result = Rendimento(descricao, valor)
        self.__rendimentos.append(result)
        return result

    def list(self):
        return self.__rendimentos

    def count_total_rendimento_value(self):
        sum = 0
        for rend in self.__rendimentos:
            sum += rend.valor
        return sum
