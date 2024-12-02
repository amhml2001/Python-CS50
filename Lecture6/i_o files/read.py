# -----------------------------------
#OPEN HAS A DOCUMENTATION
#Read file using 'with':
#1. open file. (nome arquivo, modo) -> w: escrever/update; a:append; r: read
with open('E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/name.txt', 'r') as file:
    lines = file.readlines() #read all lines and return a list(each line is a node in the list)

#nice and simple read and print each line in a file
with open('E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/name.txt', 'r') as file1:
    for line1 in file1:
        print(f'hello, {line1.rstrip()}') #remove \n(formatação de linha no arquivo)


# -----------------------------------
#Read file using 'with' and sort:
#1. open file. (nome arquivo, modo) -> w: escrever/update; a:append; r: read
with open('E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/name.txt', 'r') as file2:
    for line2 in sorted(file2, reverse=True):
        print(f'hello, {line2.rstrip()}')

#Read file using 'with' and sort:
names = []
#1. open file. (nome arquivo, modo) -> w: escrever/update; a:append; r: read
with open('E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/name.txt', 'r') as file3:
    for line3 in file3:
        names.append(line3.rstrip()) #remove \n(formatação de linha no arquivo)

for name in sorted(names):
    print(f'hello, {name}')