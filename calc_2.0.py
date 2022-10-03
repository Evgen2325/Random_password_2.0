while True:
    stringInput = input("input for ex 2+2 or 2*6 .....\n")
    if stringInput == "q":
        break
    znak = ""
    i = 0
    for char in stringInput:
        if char in ('+', '-', '/', '*'):
            znak = char
            break
        i += 1
    a = int(stringInput[0:i])
    b = int(stringInput[i + 1::])
    if znak == "+":
        print(a + b)
    elif znak == "-":
        print(a - b)
    elif znak == "*":
        print(a * b)
    elif znak == "/":
        if b != 0:
            print(a / b)
        else:
            print('dont do it')
