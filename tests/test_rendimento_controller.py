import pytest
from src.controllers.RendimentoController import RendimentoController

add_rendimento_list = [
    ('rendimento de 100', 100),
    ('rendimento de 1', 1),
    ('rendimento de 999999', 999999),
]

@pytest.mark.parametrize(['descricao', 'valor'], add_rendimento_list)
def test_add_rendimento(descricao, valor):
    controller = RendimentoController()
    result = controller.add(valor, descricao)
    assert result.valor == valor
    assert result.descricao == descricao

def test_add_invalid_rendimento():
    ...

def test_get_one_rendimento():
    ...

def test_get_invalid_rendimento():
    ...

def test_list_rendimento():
    ...

def test_update_rendimento():
    ...

def test_update_invalid_rendimento():
    ...

def test_delete_rendimento():
    ...

def test_delete_invalid_rendimento():
    ...