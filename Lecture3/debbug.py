#F5 é o F8 do abap
#F10 é o F6 do abap, avança uma instrução
#F11 é o F5, avançamos e entramos na instrução
#F12 é o F7, saímos da função atual

def main():
    height = int(input("Height: "))
    pyramid(height)
    
def pyramid(n):
    for i in range(n):
        #print(i, end = " ")
        print("#" * (i + 1))

if __name__ == "__main__":
    main()