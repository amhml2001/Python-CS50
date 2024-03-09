def main():
    greet = input("Greeting: ")
    print(f"${calc_money(greet)}")

def calc_money(g):
    greet = str(g).lower().strip().replace(",", "")
    if greet == "hello" or greet.split(" ")[0] == "hello":
        return 0
    elif greet[0] == "h":
        return 20
    else:
        return 100

main()