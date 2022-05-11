import random

print('Добро пожаловать в числовую угадайку')
n = input("Put a digit: ")
num = int(input("Right limit"))


def is_valid(n: str):
    return not (n.isdigit() and is_valid(n))


total = 0
guess = random.randint(1, num)
again = "yes"
print(guess)


def body_game(n, total):
    while True:
        if is_valid(n) is False:
            n = input(f'А может быть все-таки введем целое число от 1 до {num}?')
            continue
        else:
            n = int(n)
        total += 1
        if int(n) > guess:
            n = input('Ваше число больше загаданного, попробуйте еще разок')
            continue
        elif int(n) < guess:
            n = input('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif int(n) == guess:
            print('Вы угадали, поздравляем!')
            print("Tries: ", total)



def continue_game(n):
    again = input('Would you like to play one more time? (yes, no): ')
    while again.lower() == 'yes':
        body_game(n, total)
    if again.lower() not in ["yes"]:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


body_game(n, total)
continue_game(n)
