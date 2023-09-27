#include <iostream>

using namespace std;

int main() {
    int number;
    int mask = 0;

    // Вводим значение переменной с клавиатуры
    cout << "Vvedite celoe chislo: ";
    cin >> number;

    // Устанавливаем биты 5, 3 и 11 в маске (индексация начинается с 0)
    mask |= (1 << 5);
    mask |= (1 << 3);
    mask |= (1 << 11);

    // Обнуляем биты в числе с использованием маски
    number &= ~mask;

    // Выводим результат
    cout << "Resultat: " << number << endl;

    return 0;
}