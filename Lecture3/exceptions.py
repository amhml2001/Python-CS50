#SHIFT + ALT + A --> Comentar 
""" while True:
    try:
        x = int( input("What's x? ") )
    except ValueError: # Se der erro
        print("x is not an interger")
    else:   #Se passarmos um valor válido
        break """
    
    #OR
    
""" while True:
    try:
        x = int( input("What's x? ") )
        break
    except ValueError: # Se der erro
        print("x is not an interger") """

def get_int(prompt):
    while True:
        try:
            return int( input(prompt) )
        except ValueError: # Se der erro
            pass #Passa sem fazer mais nada
    
    
x = get_int("What's x? ")
print(f"x is {x}")