import pytest
from datetime import date
from model_bakery import baker
from base.models import Contato

@pytest.fixture
def contato_string():
    contato = baker.make(
        Contato,
        nome='Tom',
        email= 'tom@email.com',
    )
    return contato

@pytest.fixture
def envio_de_msg():
    mensagem = {
        'nome': 'Fulano',
        'email': 'fulano@email.com',
        'mensagem': 'Alguma mensagem'
    }
    return mensagem