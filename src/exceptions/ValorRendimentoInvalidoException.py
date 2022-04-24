class ValorRendimentoInvalidoException(Exception):
    def __init__(self) -> None:
        super().__init__("valor de rendimento inserido é inválido")
