class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"{amount} средств успешно сняты с счета {self.account_number}"
        else:
            return "Недостаточно средств на счете"

    def check_balance(self):
        return f"Баланс счета {self.account_number}: {self.balance}"

# Макетный код для тестирования
if __name__ == "__main__":
    account_number = input("Введите номер счета: ")
    initial_balance = float(input("Введите начальный баланс: "))
    account = BankAccount(account_number, initial_balance)

    while True:
        print("\nВыберите действие:")
        print("1. Пополнить счет")
        print("2. Снять средства со счета")
        print("3. Проверить баланс")
        print("4. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            amount = float(input("Введите сумму для пополнения: "))
            print(account.deposit(amount))
        elif choice == "2":
            amount = float(input("Введите сумму для снятия: "))
            print(account.withdraw(amount))
        elif choice == "3":
            print(account.check_balance())
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие снова.")
