import csv
names = []

# for _ in range(3):
#     names.append(input('What is your name? '))

# for name in sorted(names):
#     print(f'hello, {name}')
    
# -----------------------------------
name = input('Name: ')

#Save in file:
#1. open file. (nome arquivo, modo) -> w: escrever/update; a:append; r: read
file = open('E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/name.txt', 'a')
#2. write file
file.write(f"{name}\n") # sem \n ele escreve tudo junto
#3. close and save file
file.close()

#Save in file using 'with':
#1. open file. (nome arquivo, modo) -> w: escrever/update; a:append; r: read
with open('E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/name.txt', 'a') as file: #automaticamente fecha e salva o arquivo
#2. write file
    file.write(f"{name}\n") # sem \n ele escreve tudo junto


# -----------------------------------
#WRITE USING CSV
name = input("Name: ")
home = input("Home: ")

with open("E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/students.csv", 'a', newline='') as file2:
    writer = csv.writer(file2)
    writer.writerow([name, home])
    
with open("E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/students.csv", 'a', newline='') as file3: #in the same line we can read a file and write another. ex: with open("E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/students.csv", 'a', newline='') as file3, open('dados.csv', 'w'):
    writer = csv.DictWriter(file3, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})