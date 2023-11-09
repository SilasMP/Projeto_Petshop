from datetime import date
import pytest


@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva_string):
    
    assert str(reserva_string) == f'Tom: {date.today()} - Tarde'

@pytest.mark.django_db
def test_qtd_de_reservas_agendadas_por_petshop(agendamentos_por_petshop): 

    assert agendamentos_por_petshop == 3

@pytest.mark.django_db
def test_envio_de_reserva_sem_o_preenchimento_do_campo_nome(client, dados_validos):
    dados = dados_validos
    dados['nome'] = ""

    response = client.post('/reserva', dados)

    assert 'Este campo é obrigatório.' in str(response.content.decode('utf-8'))

@pytest.mark.django_db
def test_envio_de_reserva_sem_o_preenchimento_do_campo_email(client, dados_validos):
    dados = dados_validos
    dados['email'] = ""

    response = client.post('/reserva', dados)

    assert 'Este campo é obrigatório.' in str(response.content.decode('utf-8'))

@pytest.mark.django_db
def test_envio_de_reserva_sem_o_preenchimento_do_campo_data(client, dados_validos):
    dados = dados_validos
    dados['data'] = ""

    response = client.post('/reserva', dados)

    assert 'Este campo é obrigatório.' in str(response.content.decode('utf-8'))

@pytest.mark.django_db
def test_envio_de_reserva_sem_o_preenchimento_do_campo_turno(client, dados_validos):
    dados = dados_validos
    dados['turno'] = ""

    response = client.post('/reserva', dados)

    assert 'Este campo é obrigatório.' in str(response.content.decode('utf-8'))

@pytest.mark.django_db
def test_envio_de_reserva_sem_o_preenchimento_do_campo_tamanho(client, dados_validos):
    dados = dados_validos
    dados['tamanho'] = ""

    response = client.post('/reserva', dados)

    assert 'Este campo é obrigatório.' in str(response.content.decode('utf-8'))

@pytest.mark.django_db
def test_envio_de_reserva_sem_o_preenchimento_do_campo_petshop(client, dados_validos):
    dados = dados_validos
    dados['petshop'] = ""

    response = client.post('/reserva', dados)

    assert 'Este campo é obrigatório.' in str(response.content.decode('utf-8'))