import random


print('Добро пожаловать в числовую угадайку')


def is_valid(num, max):
    return num in range(1, max)

def play_again(max):
    new_game = input('Do you wanna play again? If yes write YES if no write NO: ')
    if new_game.lower() == 'yes':
        guess_number(max)
    else:
        pass



def guess_number(max):
    num = random.randint(1, max)
    print(num)
    count = 0
    while True:

        b = int(input(f'Please input a number from 1 to {max}: '))
        count += 1
        if is_valid(b, max) ==  False:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        if b == num:
            print('Вы угадали, поздравляем!')
            break
        elif b > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        elif b < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
    print(f'Попыток сделано {count}')
    play_again(max)
    return 'Спасибо, что играли в числовую угадайку. Еще увидимся...'


print(guess_number(500))
