from random import randint


target = randint(1, 10)
count = 3
print("Попыток: ", count)
while count != 0:
    num = int(input('Укадайте число: '))

    if num == target:
        print('Вы угадали!')
        break
    elif num != target:
        count -= 1
        print('Не верно, у вас осталось попыток:', count)

        if num > target:
            print("Ваше число больше")
        elif num < target:
            print("Ваше число меньше")

    elif count == 0:
        print('Вы исчерпали кол-во попыток')