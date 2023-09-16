#include <iostream>

using namespace std;

int main() {
    // Объявляем переменную целого типа
    int myVariable;

    // Просим пользователя ввести значение переменной
    cout << "Bvedite znachenie peremennnoy: ";
    cin >> myVariable;

    // Умножаем значение переменной на множитель с использованием поразрядной операции
    myVariable = myVariable << 3; //т.к. 8 это 2^3

    // Выводим результат
    cout << "Znachenie peremennnoy posle umnozheniya na 8: " << myVariable << endl;

    return 0;
}
