#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

// Function to check if a file exists
bool fileExists(const string &filename) {
    ifstream file(filename);
    return file.good();
}

// Function to display the menu
void displayMenu() {
    cout << "1. Отображение содержимого файла" << endl;
    cout << "2. Добавить новую запись" << endl;
    cout << "3. Считывание значения по позиции" << endl;
    cout << "4. Определить количество записей" << endl;
    cout << "5. Создайте новый файл, состоящий из двух равных частей" << endl;
    cout << "6. Выход" << endl;
    cout << "Введите свой выбор: ";
}

// Function to display file content
void displayFileContent(const string &filename) {
    ifstream file(filename);
    if (file) {
        string line;
        while (getline(file, line)) {
            cout << line << endl;
        }
        file.close();
    } else {
        cout << "Ошибка: Невозможно открыть файл." << endl;
    }
}

// Function to add a new entry
void addNewEntry(const string &filename, int entry) {
    ofstream file(filename, ios::app);
    if (file) {
        file << entry << endl;
        file.close();
        cout << "Добавлена новая запись: " << entry << endl;
    } else {
        cout << "Ошибка: Невозможно открыть файл для записи." << endl;
    }
}

// Function to read a value by position
int readValueByPosition(const string &filename, int position) {
    ifstream file(filename);
    if (file) {
        int value;
        for (int i = 0; i < position; i++) {
            if (file >> value) {
                if (i == position - 1) {
                    file.close();
                    return value;
                }
            } else {
                file.close();
                cout << "Ошибка: Позиция превышает количество записей в файле." << endl;
                return -1;
            }
        }
    } else {
        cout << "Ошибка: Невозможно открыть файл для чтения." << endl;
    }
    return -1;
}

// Function to determine the number of entries
int countEntries(const string &filename) {
    ifstream file(filename);
    if (file) {
        int count = 0;
        int value;
        while (file >> value) {
            count++;
        }
        file.close();
        return count;
    } else {
        cout << "Ошибка: Невозможно открыть файл для чтения." << endl;
    }
    return -1;
}

// Function to create a new file with two equal parts
void createSplitFile(const string &filename) {
    ifstream file(filename);
    if (file) {
        vector<int> numbers;
        int value;
        while (file >> value) {
            numbers.push_back(value);
        }
        file.close();

        int count = numbers.size();
        int half = count / 2;

        ofstream newFile("сплит_" + filename);
        if (newFile) {
            newFile << half << endl;
            for (int i = 0; i < half; i++) {
                newFile << numbers[i] << endl;
            }
            newFile << (count - half) << endl;
            for (int i = half; i < count; i++) {
                newFile << numbers[i] << endl;
            }
            newFile.close();
            cout << "Новый разделенный файл создан успешно." << endl;
        } else {
            cout << "Ошибка: Невозможно создать разделенный файл." << endl;
        }
    } else {
        cout << "Ошибка: Невозможно открыть файл для чтения." << endl;
    }
}

int main() {
    string filename;
    cout << "Введите имя файла: ";
    cin >> filename;

    if (!fileExists(filename)) {
        cout << "Ошибка: Файл не существует." << endl;
        return 1;
    }

    int choice;
    int value = 0; // Объявляем переменную value
    int count = 0; // Объявляем переменную count

    do {
        displayMenu();
        cin >> choice;

        switch (choice) {
            case 1:
                displayFileContent(filename);
                break;
            case 2:
                int entry;
                cout << "ENTERВведите новую запись: ";
                cin >> entry;
                addNewEntry(filename, entry);
                break;
            case 3:
                int position;
                cout << "Введите позицию: ";
                cin >> position;
                value = readValueByPosition(filename, position); // Используем value
                if (value != -1) {
                    cout << "Значение на позиции " << position << ": " << value << endl;
                }
                break;
            case 4:
                count = countEntries(filename); // Используем count
                if (count != -1) {
                    cout << "Количество записей в файле: " << count << endl;
                }
                break;
            case 5:
                createSplitFile(filename);
                break;
            case 6:
                cout << "Пока!" << endl;
                break;
            default:
                cout << "Неверный выбор. Пожалуйста, попробуйте еще раз." << endl;
                break;
        }
    } while (choice != 6);

    return 0;
}
