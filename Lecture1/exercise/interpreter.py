exp = str(input("Expression: "))
x, y, z = exp.split(" ")

match y:
    case "+":
        r = int(x) + int(z)
        print(f"{r:.1f}")
    case "-":
        r = int(x) - int(z)
        print(f"{r:.1f}")
    case "*":
        r = int(x) * int(z)
        print(f"{r:.1f}")
    case "/":
        if z == 0:
            print("Can't divide by zero")
        else:
            r = int(x) / int(z)
            print(f"{r:.1f}")