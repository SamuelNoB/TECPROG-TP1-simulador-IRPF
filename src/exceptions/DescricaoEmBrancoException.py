class DescricaoEmBrancoException(Exception):
    """
    Classe que trata o erro de descrição em branco
    """
    def __init__(self) -> None:
        super().__init__("Descrição inserida é inválida")
