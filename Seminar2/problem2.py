# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

def sum_and_multiply_fractions(frac1, frac2):
    num1, den1 = map(int, frac1.split('/'))
    num2, den2 = map(int, frac2.split('/'))
    common_denominator = den1 * den2
    sum_num = num1 * (common_denominator // den1) + num2 * (common_denominator // den2)
    product_num = num1 * num2
    product_den = den1 * den2
    return (f"{sum_num}/{common_denominator}", f"{product_num}/{product_den}")

from fractions import Fraction

frac1 = input("Введите первую дробь: ")
frac2 = input("Введите вторую дробь: ")

sum_frac, prod_frac = sum_and_multiply_fractions(frac1, frac2)

sum_check = Fraction(sum_frac) == Fraction(frac1) + Fraction(frac2)

prod_check = Fraction(prod_frac) == Fraction(frac1) * Fraction(frac2)

print(f"Сумма: {sum_frac}, Проверка: {sum_check}")
print(f"Произведение: {prod_frac}, Проверка: {prod_check}")