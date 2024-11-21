import pytest
from calculator import square

# pytest é uma ferramenta útil para ver os erros desses assert
# pytest <nome do arquivo>
# podemos rodar o pytest em um folder com vários arquivos de teste

# Lembre de sempre ter multiplos valores/testes para cada caso
# Evite criar funções sem retorno, pois testar eles são mais chatos


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

# Se passar uma string vai dar o erro TypeError? Se sim, está funcionando. Se não tem algum erro na lógica
def test_str():
    with pytest.raises(TypeError):
        square("cat")

# assert <valor> == pytest.approx(<number>, abs=0.1) -> approx da uma tolerância igual ao valor em abs

# isso não faz nada se a condição que passamos for verdadeiro,
# mas se for falso ele dá um erro, AssertionError para ser exato
# neste caso ele é o mesmo que escrever
# if square(2) != 4:
#     print('2 squared was not 4')
#     assert square(2) == 4
# except AssertionError:
#     print('2 squared was not 4')
