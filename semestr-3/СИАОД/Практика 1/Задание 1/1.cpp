#include <iostream>
using namespace std;

int main() {
    int myVar;  // Объявляем целочисленную переменную myVar
    myVar = 0x33;  // Присваиваем значение 0x33 (в двоичной системе: 00110011)
    
    // Выводим исходное значение myVar
    cout << "Iskhodnoe znachenie myVar (hex): " << hex << myVar << endl;
    
    // Маска для установки битов с нечетными номерами в 1
    int mask = 0xAA;  // Маска в шестнадцатеричной системе: 10101010
    
    // Выполняем операцию ИЛИ (|) с маской, чтобы установить биты с нечетными номерами в 1
    myVar |= mask;
    
    // Выводим измененное значение переменной myVar
    cout << "Resultat myVar (hex): " << hex << myVar << endl;
    
    return 0;
}
