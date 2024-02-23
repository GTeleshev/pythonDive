# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег
# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

class ATM:
    operations_list = []

    def __init__(self):
        self.balance = 0
        self.operation_count = 0

    def deposit(self, amount):
        if amount % 50 == 0:
            self.apply_wealth_tax()
            self.balance += amount
            self.operation_count += 1
            self.apply_interest()
            self.operations_list.append(f"deposit: {amount}")
            print(f"Ваш баланс: {self.balance} у.е.")
        else:
            print("Сумма пополнения должна быть кратна 50 у.е.")

    def withdraw(self, amount):
        if amount % 50 == 0:
            self.apply_wealth_tax()
            fee = max(30, min(600, amount * 0.015))
            total_amount = amount + fee
            if total_amount <= self.balance:
                self.balance -= total_amount
                self.operation_count += 1
                self.apply_interest()
                self.operations_list.append(f"withdraw: {amount}")
                print(f"Ваш баланс после снятия: {self.balance} у.е.")
            else:
                print("Недостаточно средств на счету.")
        else:
            print("Сумма снятия должна быть кратна 50 у.е.")

    def apply_interest(self):
        if self.operation_count % 3 == 0:
            self.balance += self.balance * 0.03
            print(f"Начислены проценты. Ваш баланс: {self.balance} у.е.")

    def apply_wealth_tax(self):
        if self.balance > 5000000:
            print(f"Снимается налог на богатство в размере {self.balance * 0.1}")
            self.balance -= self.balance * 0.1


atm = ATM()
atm.deposit(50000050)
print(atm.balance)
atm.withdraw(500)
print(atm.balance)
print(atm.operations_list)
