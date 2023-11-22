import pytest
from datetime import date, timedelta
from model_bakery import baker
from reserva.models import Reserva, Petshop, Categoria

@pytest.fixture
def dados_agendamento_errado():
    petshop = baker.make(Petshop)    
    categoria = baker.make(Categoria)
    amanha = date.today() - timedelta(days=1)
    dados = {
        'nome': 'Joao',
        'email': 'joao@email.com',
        'data': amanha,
        'turno': 'tarde',
        'tamanho': 'pequeno',
        'categoria': categoria.pk,        
        'observacoes': 'Alguma observação relevante',
        'petshop': petshop.pk,
    }
    return dados

@pytest.fixture
def agendamento():
    return baker.make(Reserva)

@pytest.fixture
def petshop():
    return baker.make(Petshop)

@pytest.fixture
def dados_agendamento():
    petshop = baker.make(Petshop)    
    categoria = baker.make(Categoria)
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nome': 'Joao',
        'email': 'joao@email.com',
        'data': amanha,
        'turno': 'tarde',
        'tamanho': 'pequeno',
        'categoria': categoria.pk,        
        'observacoes': 'Alguma observação relevante',
        'petshop': petshop.pk,
    }
    return dados

@pytest.fixture
def usuario_autenticado():
    return baker.make('auth.User')

@pytest.fixture
def dados_petshop():
    dados = {
        'nome':'Filial_2',
        'rua':'Rua das flores',
        'numero':'10',
        'bairro':'Centro'
    }
    return dados