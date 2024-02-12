#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
#Программа должна подсказывать “больше” или “меньше” после каждой попытки.
#Для генерации случайного числа используйте код:
#from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint


def guess_number():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    print("Я загадал число от 0 до 1000. Попробуй угадать его за 10 попыток!")

    for attempt in range(1, 11):
        try:
            guess = int(input(f"Попытка {attempt}: "))
            if guess < num:
                print("Больше!")
            elif guess > num:
                print("Меньше!")
            else:
                print(f"Поздравляю! Ты угадал число {num} с {attempt} попытки.")
                break
        except ValueError:
            print("Пожалуйста, вводи только целые числа.")

        if attempt == 10:
            print(f"К сожалению, ты не угадал. Я загадал число {num}.")


guess_number()