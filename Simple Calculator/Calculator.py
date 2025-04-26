from Calculator_appendix import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*":multiply,
              "/":divide,
              }


def calculator():
    print(logo)
    accumulate = True
    n1 = float(input("What is the first number?: "))
    while accumulate:
        print("+\n-\n*\n/")
        op = input("Pick an operation: ")
        n2 = float(input("What is the next number?: "))
        result = operations[f"{op}"](n1,n2)
        print(f"{n1} {op} {n2} = {result}")
        ans = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if ans == 'y':
            n1 = result
        elif ans == 'n':
            print("\n" * 100)
            calculator()
        else:
            print("What do you mean?")

calculator()