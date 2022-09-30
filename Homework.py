import random


string = input("Введите пароль состоящий из не менее 20 символов\n")
symbols = ('<', ',', '.', '!', '?')
kol_symbols = 0
dlina_str = 0
kol_bykv = 0
dlina_str = len(string)
password = ''
random_symbols = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM<>?!#-+"
for i in string:
    if i in symbols:
        kol_symbols += 1
    elif i.istitle():
        kol_bykv += 1
if kol_bykv > 3 and kol_symbols > 2 and dlina_str > 20:
    print(string)
else:
    symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ<>?!'
    len_pass = input("Если не получается нормально ввести пароль, введите что угодно\n")
    for i in range(len(symbols)):
        len_pass = random.choice(symbols)
        print(len_pass, end='')
