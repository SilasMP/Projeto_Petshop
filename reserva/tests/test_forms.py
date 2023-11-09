import pytest
from model_bakery import baker
from reserva.models import Reserva
from datetime import date, timedelta


@pytest.mark.django_db
def test_formulario_preenchido_com_data_no_passado(client, dados_invalidos):
    response = client.post('/reserva', dados_invalidos)

    assert response.status_code == 200
    assert 'Não é possível agendar em uma data anterior a de hoje' in str(response.content.decode('utf-8'))

@pytest.mark.django_db
def test_numero_de_reservas_excedido(client, dados_para_agendamento_excedido):
    quantidade = 4
    amanha = date.today() + timedelta(days=1)
    baker.make(
        Reserva,
        quantidade,
        data = amanha,
        )
  
    response = client.post('/reserva', dados_para_agendamento_excedido)

    assert 'Não há agenda disponivel para este turno no momento' in str(response.content.decode('utf-8'))