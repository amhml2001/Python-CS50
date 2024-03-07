#WHILE
print("w1.")
i = 0
while i < 3:
    print("meow")
    i += 1
while True:
    n = int(input("What's n?"))
    if n > 0:
        break
print("w2.")
for _ in  range(n):
    print("meow")

#FOR
print("f1.")
for i in [0, 1, 2]:
    print("meow")
 
print("f2.")   
for _ in range(3):
    print("meow")

print("f3.")
print("meow\n" * 3, end="")

#Function version
def main():
    number = get_number()
    meow(number)
def meow(n):
    print("fu1.")
    for _ in range(n):
        print("meow")
def get_number():
    while True:
        n = int(input("what's n?"))
        if n > 0:
            return n

main()

#LIST
#Para declarar uma lista vc usa []
students = ["Hermione", "Harry", "Ron"]
print("l1.")
print(students[1])

print("l2.")
for student in students:
    print(student)
    
print("l3.")
for i in range(len(students)):
    print(students[i])
    
print("l4.")
for i in range(len(students)):
    print(i + 1, students[i])
    
#DICTIONARY
# Feito de chaves e valores. É declarado usando {} 
students2 = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}
print("d1.")
print(students2["Draco"])

print("d2.")
for student2 in students2:
    #a variável student2 é a chave, no caso o nome do aluno. e students2[student2] traz o valor da chave
    print(student2, students2[student2], sep=", ") 
    
students3 = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

print("d3.")
for student3 in students3:
    print(student3["name"], student3["house"], student3["patronus"], sep=", ")
 
#Function mode   
print("Mario 1.")    
for _ in range(3):
    print("#")
 
def main2():
    print("Mario 2.") 
    print_column(3)
    print("Mario 3.")
    print_row(4)
    print("Mario 4.")
    print_square(3)
    print("Mario 5.")
    print_square2(3)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)
    
def print_square(size):
    #For each row in square
    for i in range(size):
        #For each brick in row
        for j in range(size):
            #Print brick
            print("#", end="")
        #Print \n, muda a linha
        print()
        
def print_square2(size):
    for i in range(size):
       print_row(size)
    
def print_row(width):
    print("#" * width)

main2()