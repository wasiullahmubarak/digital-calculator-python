print("welcome to digital calculator")


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,

}
history = []
def calculator():
    should_continue = True
    while should_continue:
        num1 = float(input("type your number:"))
        for symbol in operation:
            print(symbol)
        operational_symbol = input("type your operational symbol:")
        num2 = float(input("type your second number:"))
        answer = (operation[operational_symbol](num1, num2))
        print(f"{num1}{operational_symbol}{num2}  = {answer}")
        history.append(f"{num1}{operational_symbol}{num2}  = {answer}")
        choice = (input("type 'y' to add with result or type 'n' to start h for history to reset type 'e' to end  :"))
        if choice == "y":
            num1 = answer
        elif choice == "n":
            print("\n" * 20)
        elif choice == "h":
            print(history)
        else:
            if choice == "e":
                should_continue = False
                calculator()

calculator()


