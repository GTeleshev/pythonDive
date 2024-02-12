#3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
#Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    try:
        number = int(input("Введите число: "))
        if number < 0 or number > 100000:
            print("Число должно быть в диапазоне от 0 до 100000.")
        elif is_prime(number):
            print(f"Число {number} является простым.")
        else:
            print(f"Число {number} является составным.")
    except ValueError:
        print("Введено не число. Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()