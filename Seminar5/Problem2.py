# 3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ["Иван", "Мария", "Петр"]
rate = [10000, 15000, 12000]
bonus = ["10%", "15%", "12.5%"]

result = {names[i]: rate[i] * float(bonus[i].strip('%')) / 100 for i in range(len(names))}
print(result)