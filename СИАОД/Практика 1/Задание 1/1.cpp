#include <iostream>

using namespace std;

int main() {
    
    setlocale(LC_ALL, "Russian");
    // Задаем исходное значение в шестнадцатеричной системе счисления
    int hexValue = 0x55; // Это значение имеет биты с номерами 0, 2, 4, 6, ...

    // Маска для установки битов с нечетными номерами в 1
    int mask = 0x55; // Эта маска имеет биты с номерами 0, 2, 4, 6, ...

    // Устанавливаем биты с нечетными номерами в 1 с помощью поразрядной операции ИЛИ
    int result = hexValue | mask;

    // Выводим исходное значение и результат
    cout << "Исходное значение: 0x" << hex << hexValue << endl;
    cout << "Результат: 0x" << hex << result << endl;

    return 0;
}
