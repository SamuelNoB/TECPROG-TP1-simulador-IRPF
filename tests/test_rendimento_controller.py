from unittest import result
import pytest
from src.models.Rendimento import Rendimento
from src.controllers.RendimentoController import RendimentoController
from src.exceptions.DescricaoEmBrancoException import DescricaoEmBrancoException
from src.exceptions.ValorRendimentoInvalidoException import ValorRendimentoInvalidoException

add_rendimento_list = [
    ('rendimento de 100', 100),
    ('rendimento de 1', 1),
    ('rendimento de 999999', 999999),
]

rendimento_list_invalid_param = [
    ('rendimento de 0', 0),
    ('rendimento de -1', -1),
    ('rendimento de ""', ''),
    ('rendimento de None', None),
    ('', None)
]

rendimento_list_count = [
    ([('rend1', 10), ('rend2', 20)], 2),
    ([('rend1', 10)], 1),
    ([], 0)
]

rendimento_list_total_value = [
    ([('rend1', 40), ('rend2', 40)], 80),
    ([('rend1', 1000), ('rend1', 2000.25), ('rend1', 1000.45)], 4000.70),
]

@pytest.mark.parametrize(['descricao', 'valor'], add_rendimento_list)
def test_add_rendimento(descricao, valor):
    controller = RendimentoController([])
    result = controller.add(valor, descricao)
    assert result.valor == valor
    assert result.descricao == descricao

@pytest.mark.parametrize(['descricao', 'valor'], rendimento_list_invalid_param)
def test_add_invalid_rendimento(descricao, valor):
    controller = RendimentoController()
    with pytest.raises((ValorRendimentoInvalidoException, DescricaoEmBrancoException)):
        controller.add(valor, descricao)

@pytest.mark.parametrize(['rendimentos', 'resultado'], rendimento_list_count)
def test_list_rendimento(rendimentos, resultado):
    controller = RendimentoController([])
    for rendimento in rendimentos:
        controller.add(rendimento[1], rendimento[0])
    result = len(controller.list())
    assert result == resultado

@pytest.mark.parametrize(['rendimentos', 'resultado'], rendimento_list_total_value)
def test_count_total_rendimento_value(rendimentos, resultado):
    rendimentos_list = []
    for rendimento in rendimentos:
        rendimentos_list.append(Rendimento(rendimento[0], rendimento[1]))
    
    controller = RendimentoController(rendimentos_list)
    result = controller.count_total_rendimento_value()
    assert result == resultado
