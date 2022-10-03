import random

symbols = '1234567890qwertyuiopasdfghjklzxcvbnm'
lenght = input('Input lenght password please: \n')
password = ''
for i in range(int(lenght)):
    password += random.choice(symbols)
print(password)
symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ<>?!'
    len_pass = input("Если не получается нормально ввести пароль, введите что угодно\n")
    for i in range(len(symbols)):
        len_pass = random.choice(symbols)
        print(len_pass, end='')