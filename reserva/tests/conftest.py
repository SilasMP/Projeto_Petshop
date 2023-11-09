import pytest
from model_bakery import baker
from reserva.models import Reserva, Petshop
from datetime import date, timedelta

@pytest.fixture
def reserva_string():
    data = date.today()
    reserva = baker.make(
        Reserva,
        nome='Tom',
        data = data,
        turno= 'Tarde',
    )
    return reserva

@pytest.fixture
def agendamentos_por_petshop():
    petshop = baker.make(Petshop)
    quantidade = 3
    agendamentos = baker.make(
        Reserva,
        quantidade,
        petshop=petshop,
    )
    return petshop.qtda_reservas()

@pytest.fixture
def dados_validos():
    baker.make(Petshop)
    
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nome': 'João',
        'email': 'joao@email.com',
        'data': amanha,
        'turno': 'tarde',
        'tamanho': 'pequeno',
        'observacoes': 'Alguma observação relevante',
        'petshop': 1,
    }
    return dados

@pytest.fixture
def dados_para_agendamento_excedido():
    baker.make(Petshop)
    
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nome': 'João',
        'email': 'joao@email.com',
        'data': amanha,
        'turno': 'tarde',
        'tamanho': 'pequeno',
        'observacoes': 'Alguma observação relevante',
        'petshop': 1,
    }
    return dados

@pytest.fixture
def dados_invalidos():
    baker.make(Petshop)
    
    ontem = date.today() - timedelta(days=1)
    dados = {
        'nome': 'João',
        'email': 'joao@email.com',
        'data': ontem,
        'turno': 'tarde',
        'tamanho': 'pequeno',
        'observacoes': 'Alguma observação relevante',
        'petshop': 1,
    }
    return dados