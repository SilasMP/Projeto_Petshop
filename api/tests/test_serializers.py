import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_tentativa_de_agendamento_com_data_passada(usuario_autenticado, dados_agendamento_errado):
    client = APIClient()
    client.force_authenticate(usuario_autenticado)
    resposta = client.post('/api/reservas', dados_agendamento_errado)
    assert 'Não é possível agendar em uma data antiga' in str(resposta.content.decode('utf-8'))

@pytest.mark.django_db
def test_agendamento_em_data_e_turno_excedidos(usuario_autenticado, dados_agendamento):      
    client = APIClient()
    client.force_authenticate(usuario_autenticado)
    
    for qtde_de_post in range(4):
        resposta = client.post('/api/reservas', dados_agendamento)
    
    assert resposta.status_code == 400
    assert 'O limite de agendamentos para este turno ja foi atingido' in str(resposta.content.decode('utf-8'))