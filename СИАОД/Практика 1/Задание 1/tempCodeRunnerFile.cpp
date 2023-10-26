#include <iostream>

using namespace std;

int main() {
    // Объявляем переменную целого типа
    int myVariable;

    // Просим пользователя ввести значение переменной
    cout << "Vvedite znachenie peremennoy: ";
    cin >> myVariable;

    // Задаем номер бита, который мы хотим обнулить (номерация с 0)
    int n;
    cout << "Vvedite nomer bite, kotoriy nujno obnulit: ";
    cin >> n;

    // Создаем маску с битом, который нужно обнулить
    int mask = 1 << n;

    // Инвертируем маску, чтобы бит с номером n был равен 0, а остальные биты - 1
    mask = ~mask;

    // Обнуляем n-й бит в значении переменной, используя маску
    myVariable = myVariable & mask;

    // Выводим результат
    cout << "Znachenie peremennoy posle obnuleniya " << n << "-go bita: " << myVariable << endl;

    return 0;
}
