def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print(deep(ans))
    
def deep(a):
    if (a == "forty-two" or a == "forty two" or int(a) == 42):
        return "Yes"
    else:
        return "No"
        

main()