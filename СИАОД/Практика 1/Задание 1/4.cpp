#include <iostream>

using namespace std;

int main() {
    // Объявляем переменную целого типа
    int myVariable;

    // Просим пользователя ввести значение переменной
    cout << "Bvedite znachenie peremennnoy: ";
    cin >> myVariable;

    // Задаем множитель
    int delitel = 8;

    // Умножаем значение переменной на множитель с использованием поразрядной операции
    myVariable = myVariable >> 4; // //т.к. 16 это 2^4

    // Выводим результат
    cout << "Znachenie peremennnoy posle deleniya na 16: " << myVariable << endl;

    return 0;
}
