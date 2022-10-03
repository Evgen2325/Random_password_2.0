import random

string = input("Input your password\n")

symbols = ('<', ',', '.', '!', '?')
alphabet = "abcdefgjiklmnoprstqwvxyz"

kol_symbols = 0
dlina_str = 0
kol_bykv = 0
dlina_str = len(string)

for i in string:
    if i in symbols:
        kol_symbols += 1
    elif i.istitle():
        kol_bykv += 1
if kol_bykv > 3 and kol_symbols > 2 and dlina_str > 20:
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