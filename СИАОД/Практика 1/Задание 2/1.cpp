#include <iostream>
#include <vector>

using namespace std;

// Функция для вывода битового представления числа
void printBinary(unsigned int num) {
    for (int i = 6; i >= 0; i--) {
        cout << ((num >> i) & 1);
    }
}

int main() {
    vector<unsigned int> numbers; // Массив для хранения чисел в битовом представлении

    // Ввод семизначных чисел с клавиатуры и сохранение их в массиве
    cout << "Vvedite 7-znachnye chisla (cherez probel): ";
    for (int i = 0; i < 10; i++) { // Для теста вводим 10 чисел
        unsigned int num;
        cin >> num;
        numbers.push_back(num);
    }

    // Сортировка пузырьком (по битовому представлению)
    int n = numbers.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (numbers[j] > numbers[j + 1]) {
                swap(numbers[j], numbers[j + 1]);
            }
        }
    }

    // Вывод отсортированных чисел
    cout << "Otsortirovannye chisla:" << endl;
    for (unsigned int num : numbers) {
        printBinary(num);
        cout << endl;
    }

    return 0;
}
