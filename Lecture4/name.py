import sys

# sys.argv pega os valores do prompt e forma uma lista onde index 0 é o nome do programa sendo rodado
if len(sys.argv) < 2:
    # sys.exit() say da execução do programa. terminate program
    sys.exit("Too few arguments")

# Podemos fazer sys.argv[1] para pegar o valor no index 1 da lista de argumentos passados
# Podemos também usar : para pegar um intervalo da lista, neste caso estamos pegando do index 1 até o fim
for arg in sys.argv[1:]:
    print("hello my name is", arg)
# python name.py Amanda -> hello my name is Amanda
# python name.py "Amanda Hossoda" -> hello my name is Amanda Hossoda
