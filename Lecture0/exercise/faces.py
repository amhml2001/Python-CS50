def main():
    words = str(input("Diga algo: "))
    print(convert(words))
    
def convert(w):
    w = str(w).replace(":(", "🙁")
    w = str(w).replace(":)", "🙂")
    return w
    
main()