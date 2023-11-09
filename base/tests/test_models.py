import pytest

@pytest.mark.django_db
def test_str_contato_deve_retornar_string_formatada(contato_string):
    
    assert str(contato_string) == 'Tom [tom@email.com]'
