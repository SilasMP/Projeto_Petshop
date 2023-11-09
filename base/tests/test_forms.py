import pytest
from pytest_django.asserts import assertTemplateUsed

def test_envio_de_msg_sem_o_preenchimento_do_campo_nome(client, envio_de_msg):
    mensagem = envio_de_msg
    mensagem['nome'] = ""

    response = client.post('/contato', mensagem)

    assert 'Este campo é obrigatório.' in str(response.content.decode('utf-8'))

def test_envio_de_msg_sem_o_preenchimento_do_campo_email(client, envio_de_msg):
    mensagem = envio_de_msg
    mensagem['email'] = ""

    response = client.post('/contato', mensagem)

    assert 'Este campo é obrigatório.' in str(response.content.decode('utf-8'))

def test_envio_de_msg_sem_o_preenchimento_do_campo_msg(client, envio_de_msg):
    mensagem = envio_de_msg
    mensagem['mensagem'] = ""

    response = client.post('/contato', mensagem)

    assert 'Este campo é obrigatório.' in str(response.content.decode('utf-8'))