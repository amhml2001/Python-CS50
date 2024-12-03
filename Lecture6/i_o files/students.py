# CSV HAS A DOCUMENTATION
import csv

with open('E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/names.csv', 'r') as file:
    for line in file:
        row = line.rstrip().split(',')
        print(f'{row[0]} is in {row[1]}')
        
print('----------------------')

with open('E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/names.csv', 'r') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        print(f'{name} is in {house}')

print('----------------------')
      
students = []
with open('E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/names.csv', 'r') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        student = {}
        # student['name'] = name
        # student['house'] = house
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

print('----------------------')

for student in sorted(students, key=lambda student: student['name']): # lambda is a anonimous function, only called onece here. before : is the parameter and after is the return value
    print(f"{student['name']} is in {student['house']}")

print('----------------------')
#----------------------------
#CSV LIBARRY
students1 = []
with open('E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
       students1.append({"name": row[0], "home": row[1]}) 
        
for student in sorted(students1, key=lambda student: student['name'], reverse=False): # lambda is a anonimous function, only called onece here. before : is the parameter and after is the return value
    print(f"{student['name']} is from {student['home']}")

print('----------------------')

students2 = []
with open('E:/ESTUDO/VsCode/CS50 Introduction Python/Lecture6/i_o files/students.csv', 'r') as file2:
    reader = csv.DictReader(file2)
    for row in reader:
        students2.append(row) # this is the same as the line bellow. since row is a dictionary
        # students2.append({"name": row["name"], "home": row["home"]})
        
for student in sorted(students2, key=lambda student: student['name']): # lambda is a anonimous function, only called onece here. before : is the parameter and after is the return value
    print(f"{student['name']} is from {student['home']}")

print('----------------------')

