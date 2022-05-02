class ValorRendimentoInvalidoException(Exception):
    """
    Classe que trata o erro de um valor de rendimento inválido
    """

    def __init__(self) -> None:
        super().__init__("valor de rendimento inserido é inválido")
