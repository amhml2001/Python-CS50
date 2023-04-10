#Type conversion from str to int
x = int(input("What's x? "))
y = int(input("What's y? "))

print(f"1. { x + y }")

#Float
m = float(input("What's m? "))
n = float(input("What's n? "))

print( f"2. {m + n}" )

#round -> round(number [, ndigits])
#Obs: dentro dos colchetes são os parâmetros opcionais

#Round
z = round( m + n )
print(f"3. {z: ,}") #Formata os valores colocando , separando os milhares 1000 -> 1,000

#Round with parameters
d =  round( m / n, 2 )
print(f"4. {d}")

#Format string to 2 decimals
print(f"5. {d:.2f}")#Formata o valor com duas casas decimais

#Function with return
def main():
    x = int(input("What's x? "))
    print("6. x squared is", square(x))
    
def square(n):
    return n * n #Or return n ** 2 Or return pow(n, 2)

main()
