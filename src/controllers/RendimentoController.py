from ..models.Rendimento import Rendimento
class RendimentoController:
    __rendimentos: list[Rendimento]  = []
    def __init__(self, rendimentos: list[Rendimento] = []) -> None:
        self.__rendimentos = rendimentos

    def add(self, valor: float, descricao: str) -> Rendimento:
        result = Rendimento(descricao, valor)
        self.__rendimentos.append(result)
        return result

    def update():
        ...
    
    def get():
        ...

    def list():
        ...
    
    def delete():
        ...