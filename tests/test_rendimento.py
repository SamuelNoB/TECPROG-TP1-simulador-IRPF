import pytest
from src.Rendimento import Rendimento


rendimento_list = [
    ('rendimento de 100', 100),
    ('rendimento de 0', 0),
    ('rendimento de -1', -1),
]

@pytest.mark.parametrize(['descricao', 'valor'], rendimento_list)
def test_rendimento_class(descricao, valor):
    um_rendimento = Rendimento(descricao, valor)
    assert um_rendimento.valor_rendimento == valor
