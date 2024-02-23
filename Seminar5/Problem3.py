# 4. Создайте функцию генератор чисел Фибоначчи
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8


# рекурсия
def fibonacci(number: int):
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


def fib_list(number: int):
    fib_lst = []
    for i in range(0, number + 1):
        fib_lst.append(fibonacci(i))
    return fib_lst


print(fibonacci(10))
print(fib_list(10))


# генератор

def fib_gen(max_value):
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b


a = fib_gen(60)

print(*a)
