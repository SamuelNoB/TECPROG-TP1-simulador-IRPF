class DescricaoEmBrancoException(Exception):
    def __init__(self) -> None:
        super().__init__('Descrição inserida é inválida')