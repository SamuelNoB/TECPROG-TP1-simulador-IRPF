from dataclasses import dataclass, field
from ..exceptions.DescricaoEmBrancoException import DescricaoEmBrancoException
from ..exceptions.ValorRendimentoInvalidoException import (
    ValorRendimentoInvalidoException,
)


@dataclass
class Rendimento:
    """
    Classe que representa um rendimento
    """
    valor: float

    def __post_init__(self):
        if (type(self.valor) == str or self.valor == None) or self.valor == 0:
            raise (ValorRendimentoInvalidoException)
        if self.descricao == None or self.descricao == "":
            raise (DescricaoEmBrancoException)
