#CONDITIONS
x = int(input("What's X? "));
y = int(input("What's Y? "));

if x < y:
    print("1.X is less than Y");
elif x == y:
    print("1.X is equal to Y");
else:
    print("1.X is greater than Y");

if x == y:
    print("2.X is equal to Y");
else:
    print("2. X is not equal to Y");
    
#Score
score = int(input("Student score: "))
if score >= 90:
    print("3.A");
elif score >= 80:
    print("3.B");
elif score >= 70:
    print("3.D");
else:
    print("3.F");

#Par ou Impar
def main():
    z = int(input("What's Z? "))
    if is_even(z):
        print("Even");
    else:
        print("Odd");

def is_even(n):
    #V é a mesma cosia que: return True if n % 2 == 0 else False;
    return n % 2 == 0;

#MATCH (Similar ao switch)
name = input("What's your name? ");

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor");
    case "Draco":
        print("Slytherin");
    case _:
        print("Who?")
    
main()