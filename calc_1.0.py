print("Welcome to calculator version 1.0\nPlease input 'q' for exit")
while True:
    char = input("choice function +, -, *, /\n")
    if char == "q":
        break
    elif char not in ("+", "-", "*", "/"):
        continue
    a = float(input())
    b = float(input())
    if char == "+":
        print(a + b)
    elif char == "-":
        print(a - b)
    elif char == "*":
        print(a * b)
    elif char == "/":
        if b != 0:
            print(a / b)
