import pytest

@pytest.mark.django_db
def test_formulario_preenchido_com_data_no_passado(client, dados_invalidos):
    response = client.post('/reserva', dados_invalidos)

    assert response.status_code == 200
    assert 'Não é possível agendar em uma data anterior a de hoje' in str(response.content.decode('utf-8'))

@pytest.mark.django_db
def test_numero_de_reservas_excedido(client, dados_validos):

    for qtde_de_post in range(4):    
        response = client.post('/reserva', dados_validos)

    assert 'Não há agenda disponivel para este turno no momento' in str(response.content.decode('utf-8'))