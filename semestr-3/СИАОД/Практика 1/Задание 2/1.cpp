#include <iostream>
#include <vector>
#include <chrono>
#include <random>

using namespace std;

int main() {
    const int maxNum = 9999999;
    
    // Ввод количества семизначных чисел
    int numCount;
    cout << "Vvedite kolichestvo chisel: ";
    cin >> numCount;

    // Проверка на неправильный ввод
    if (numCount <= 0) {
        cout << "Oshibka.\n";
        return 1;
    }

    vector<bool> bitArray(maxNum + 1, false);
    vector<int> randomNumbers;

    // Генерация случайных семизначных чисел
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis(0, maxNum);

    auto start = chrono::high_resolution_clock::now();

    for (int i = 0; i < numCount; ++i) {
        int num = dis(gen);
        randomNumbers.push_back(num);
        bitArray[num] = true;
    }

    // Вывод сгенерированных чисел
    cout << "Generaciya:\n";
    for (int num : randomNumbers) {
        cout << num << " ";
    }
    cout << "\n";

    // Вывод отсортированных чисел
    cout << "Otsortirovannie chisla:\n";
    for (int i = 0; i <= maxNum; ++i) {
        if (bitArray[i]) {
            cout << i << " ";
        }
    }

    cout << "\n";
    
    auto stop = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
    cout << "Vremya raboti: " << duration.count() << " mc" << endl;

    return 0;
}
