#Ask user for their name
name = input("What's your name? ")
#Say hello to the user --> Concat
print("1. hello, " + name)
#Pass multiple arguments to print --> already makes a space in between arguments
print("2. hello,", name)
#Parameters: print documentation --> print(*objects, sep=" ", end="\n")
print("3. hello, ", end="")
print(name)
#Format string or f string
print(f"4. hello, {name}")
print('5. hello, "friend"')
#Escape characters \ -> Eles indicam que aquele caracter não está fechando, esses caracters são literais
print("6. hello, \"friend\"")

#String methods
#Remove whitespace from str|     david    --> david
name = name.strip()
print("7. hello,", name)
#Captalize name | david --> David
name = name.capitalize()
print("8. hello,", name)
#Captalize the first letter of every word| david malan --> David Malan
name = name.title()
print("9. hello,", name)
#Chain methods
name = name.strip().title()
print("10. hello,", name)
#Input with methods
name2 = input("Name? ").strip().title()
print("11. hello,", name2)
#Split method| david malan --> david
first, last = name.split(" ")
one, two = name2.split(" ")
print(one, two)
print("12. hello,", first)
#Write python in terminal to use the interactive mode, the moment you execute a line it shows the result

#By creating a main function, you can organize your files and
#calling your function in whichever order they were defined
#Obs: Python doesn't recognize if a function that was declared later in the code 
def main():
    nameFunc = input("What's your name? ")
    hello(nameFunc)
    
#Define function
def hello(to="world"): #Default value is world
    print("13. Hello,", to)
    
#Call function
main()
