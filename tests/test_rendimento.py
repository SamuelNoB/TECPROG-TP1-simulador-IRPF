import pytest
from src.Rendimento import Rendimento
from src.exceptions.DescricaoEmBrancoException import DescricaoEmBrancoException
from src.exceptions.ValorRendimentoInvalidoException import ValorRendimentoInvalidoException

rendimento_list = [
    ('rendimento de 100', 100),
    ('rendimento de 1', 1),
    ('rendimento de 999999', 999999),
]

rendimento_list_invalid_value = [
    ('rendimento de 0', 0),
    ('rendimento de -1', -1),
    ('rendimento de ""', ''),
    ('rendimento de None', None),
]

invalid_description_list = ['', None]

@pytest.mark.parametrize(['descricao', 'valor'], rendimento_list)
def test_rendimento_class(descricao, valor):
    um_rendimento = Rendimento(descricao, valor)
    assert um_rendimento.valor == valor


@pytest.mark.parametrize(['descricao', 'valor'], rendimento_list_invalid_value)
def test_rendimento_class_invalid_value(descricao, valor):
    with pytest.raises(ValorRendimentoInvalidoException):
        Rendimento(descricao, valor)

@pytest.mark.parametrize('descricao', invalid_description_list)
def test_rendimento_class_invalid_description(descricao):
    valor = 10
    with pytest.raises(DescricaoEmBrancoException):
        Rendimento(descricao, valor)
