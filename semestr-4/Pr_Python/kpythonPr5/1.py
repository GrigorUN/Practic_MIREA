import sqlite3

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS accounts (account_number INTEGER PRIMARY KEY, balance REAL)")
        self.conn.commit()

    def deposit(self, amount):
        self.cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    def withdraw(self, amount):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        balance = self.cursor.fetchone()[0]
        self.cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        balance = self.cursor.fetchone()[0]
        return f"Баланс счета {self.account_number}: {balance}"

    def close_account(self):
        self.cursor.execute(
            "DELETE FROM accounts WHERE account_number = ?", (self.account_number,))
        self.conn.commit()
        return f"Счет {self.account_number} закрыт"

    def create_account(self, balance):
        self.cursor.execute(
            "INSERT INTO accounts (account_number, balance) VALUES (?, ?)", (self.account_number, balance))
        self.conn.commit()
        return f"Счет {self.account_number} успешно создан"
    
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    def withdraw(self, amount):
        self.balance -= amount
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self):
        return f"Баланс счета {self.account_number}: {self.balance}"
    
def encode_rle(data):
    encoded = bytes()
    count = 0
    last_char = data[-1]
    for i in range(1, len(data) + 1):
        if data[i] == last_char:
            count += 1
        else:
            encoded.append(data[i])
            encoded.append(count)
            count = 1
            last_char = data[i]
    encoded.append(count)
    encoded.append(last_char)
    return bytes(encoded)

def decode_rle(data):
    decoded = bytes()
    i = 1
    while i < len(data):
        count = data[i - 1]
        char = data[i]
        decoded.extend([char]*count)
        i += 1
    return bytes(decoded)

def triangle_type(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    if a == b == c:
        return "равнобедренный"
    elif a == b or a == c or b == c:
        return "равносторонний"
    elif a != b != c:
        return "разносторонний"
    
def distance(x1, y1, x2, y2):
    """
    Вычисляет евклидово расстояние между двумя точками на плоскости.

    Параметры:
    x1 (float): x-координата первой точки.
    y1 (float): y-координата первой точки.
    x2 (float): x-координата второй точки.
    y2 (float): y-координата второй точки.

    Возвращает:
    float: Евклидово расстояние между двумя точками.

    Примеры:
    >>> distance(0, 0, 3, 4)
    5.0
    >>> distance(0, 0, 0, 0)
    0.0
    >>> distance(1, 1, 1, 5)
    4.0
    """
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


def binary_search(arr, x):
    left = 0
    right = len(arr) 
    while left <= right:
        mid = round((left + right) / 2)
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid           
    return -1

import random

def bucketsort(arr, k):
    assert k > 0, "Количество корзин должно быть положительным"
    counts = [0] * k
    for x in arr:
        assert 0 <= x < k, f"Элемент {x} находится вне диапазона [0, {k - 1}]"
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr

def test_bucketsort():
    assert bucketsort([], 10) == [], "Ошибка при сортировке пустого массива"
    assert bucketsort([5], 10) == [5], "Ошибка при сортировке массива из одного элемента"

    random_arr = [random.randint(0, 9) for _ in range(100)]
    sorted_random_arr = bucketsort(random_arr, 10)
    assert sorted_random_arr == sorted(random_arr), "Ошибка при сортировке случайного массива"

    print("Все тесты успешно пройдены")

test_bucketsort()


print(distance(1,1,2,2))