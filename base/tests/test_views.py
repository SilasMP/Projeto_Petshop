import pytest
from pytest_django.asserts import assertTemplateUsed

def test_home_view_deve_retornar_template(client):
    response = client.get('')

    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')

def test_contato_view_deve_retornar_template(client):
    response = client.get('/contato')

    assert response.status_code == 200
    assertTemplateUsed(response, 'contato.html')

@pytest.mark.django_db
def test_envio_de_msg_no_contato_retorna_sucesso(client, envio_de_msg):
    response = client.post('/contato', envio_de_msg)

    assert response.status_code == 200
    assert 'Mensagem encaminhada com Sucesso!' in str(response.content)