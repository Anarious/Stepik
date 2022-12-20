import random


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
length = int(input('Какой длины должен быть пароль? '))
pwd_digits = input('Включать ли в пароль цифры от 0 до 9? ')
pwd_uppercase = input('Включать ли в пароль прописные буквы? ')
pwd_lowercase = input('Включать ли в пароль строчные буквы? ')
pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ')
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? ')

if pwd_digits == 'yes':
    chars += digits
if pwd_uppercase == "yes":
    chars += uppercase_letters
if pwd_lowercase == "yes":
    chars += lowercase_letters
if pwd_punctuation == "yes":
    chars += punctuation
if pwd_exceptions == "yes":
    for i in 'il1Lo0O':
        if i in chars:
            chars.replace(i, '')


def generate_password(length, chars):
    pwd = ''
    for i in range(length):
        pwd += random.choice(chars)
    return pwd

for i in range(pwd_quantity):
    print(generate_password(length, chars))
