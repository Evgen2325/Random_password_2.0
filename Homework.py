import random

string = input("Input your password\n")
symbols = ('<', ',', '.', '!', '?')
alphabet = "abcdefgjiklmnoprstqwvxyz"
countSymbols = 0
countUppercase = 0
dlina_str = len(string)

for i in string:
    if i in symbols:
        countSymbols += 1
    elif i.istitle():
        countUppercase += 1
if countUppercase > 3 and countSymbols > 2 and dlina_str > 20:
    print(string)
else:
    lenNewPassword = random.randint(20, 40)
    newPassword = []
    expectedUppercaseLetters = 4
    expectedSymbols = 5
    i = 0
    while i < lenNewPassword:
        if i < expectedSymbols:
            newPassword.append(random.choice(symbols))
        elif expectedSymbols <= i < expectedSymbols + expectedUppercaseLetters:
            newPassword.append(str(random.choice(alphabet)).upper())
        else:
            newPassword.append(str(random.choice(alphabet)))
        i += 1

    random.shuffle(newPassword)
    print("Your new password with " + str(lenNewPassword) + " symbols")
    print("".join(newPassword))
