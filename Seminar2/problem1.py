#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
#Функцию hex используйте для проверки своего результата.

def int_to_hex(n):
    hex_chars = "0123456789ABCDEF"
    if n == 0:
        return "0"
    hex_string = ""
    while n > 0:
        hex_string = hex_chars[n % 16] + hex_string
        n = n // 16
    return hex_string

# Пример использования
number = 2056
hex_representation = int_to_hex(number)
print(f"Шестнадцатеричное представление числа {number} без использования встроенных функций: 0x{hex_representation}")
print(f"Проверка с помощью встроенной функции hex: {hex(number)}")