from pytest_django.asserts import assertTemplateUsed
import pytest
from reserva.models import Reserva, Petshop


@pytest.mark.django_db
def test_reserva_view_deve_retornar_template(client):
    response = client.get('/reserva')

    assert response.status_code == 200
    assertTemplateUsed(response, 'reserva.html')


@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client, dados_validos):
    response = client.post('/reserva', dados_validos)

    assert response.status_code == 200
    assert 'Reserva realizada com Sucesso!' in str(response.content)
    
@pytest.mark.django_db
def test_reserva_view_deve_criar_reserva(client, dados_validos):
    
    client.post('/reserva', dados_validos)

    assert Reserva.objects.all().count() == 1
    reserva = Reserva.objects.first()

    assert reserva.nome == dados_validos['nome']
    assert reserva.turno == dados_validos['turno']
    