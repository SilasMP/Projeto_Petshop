import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_todos_petshops():
    client = APIClient()
    resposta = client.get('/api/petshop')
    assert len(resposta.data['results']) == 0

@pytest.mark.django_db
def test_api_com_petshop_salvo(petshop):
    client = APIClient()
    resposta = client.get('/api/petshop')
    assert len(resposta.data['results']) == 1

@pytest.mark.django_db
def test_todos_agendamentos(agendamento):
    client = APIClient()
    resposta = client.get('/api/reservas')
    assert len(resposta.data['results']) == 1

#TESTES CRUD PARA RESERVAS
@pytest.mark.django_db
def test_criar_agendamento(usuario_autenticado, dados_agendamento):
    client = APIClient()
    client.force_authenticate(usuario_autenticado)
    resposta = client.post('/api/reservas', dados_agendamento)
    assert resposta.status_code == 201
    assert resposta.data['nome'] == dados_agendamento['nome']

@pytest.mark.django_db
def test_consultando_uma_reserva(agendamento):
    client = APIClient()
    resposta = client.get(f'/api/reservas/{agendamento.pk}')
    assert resposta.data['nome'] == agendamento.nome

@pytest.mark.django_db
def test_atualizando_dados_de_uma_reserva(usuario_autenticado, agendamento, dados_agendamento):
    client = APIClient()
    client.force_authenticate(usuario_autenticado)    
    resposta = client.put(f'/api/reservas/{agendamento.pk}', dados_agendamento)
    assert resposta.status_code == 200
    assert resposta.data['nome'] == dados_agendamento['nome']

@pytest.mark.django_db
def test_removendo_uma_reserva(usuario_autenticado, agendamento):
    client = APIClient()
    client.force_authenticate(usuario_autenticado)    
    resposta = client.delete(f'/api/reservas/{agendamento.pk}')
    assert resposta.status_code == 204
    resposta = client.get('/api/reservas')
    assert len(resposta.data['results']) == 0

#TESTES CRUD PARA PETSHOP
@pytest.mark.django_db
def test_criando_petshop(usuario_autenticado, dados_petshop):
    client = APIClient()
    client.force_authenticate(usuario_autenticado)
    resposta = client.post('/api/petshop', dados_petshop)    
    assert resposta.status_code == 201
    assert resposta.data['nome'] == dados_petshop['nome']

@pytest.mark.django_db
def test_consultando_um_petshop(petshop):
    client = APIClient()
    resposta = client.get(f'/api/petshop/{petshop.pk}')
    assert resposta.status_code == 200
    assert resposta.data['nome'] == petshop.nome

@pytest.mark.django_db
def test_atualizando_dados_de_um_petshop(usuario_autenticado, petshop, dados_petshop):
    client = APIClient()
    client.force_authenticate(usuario_autenticado)    
    resposta = client.put(f'/api/petshop/{petshop.pk}', dados_petshop)
    assert resposta.status_code == 200
    assert resposta.data['nome'] == dados_petshop['nome']

@pytest.mark.django_db
def test_removendo_um_petshop(usuario_autenticado, petshop):
    client = APIClient()
    client.force_authenticate(usuario_autenticado)    
    resposta = client.delete(f'/api/petshop/{petshop.pk}')
    assert resposta.status_code == 204
    resposta = client.get('/api/petshop')
    assert len(resposta.data['results']) == 0