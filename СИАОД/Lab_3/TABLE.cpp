#include <iostream>
#include <vector>

// Определение структуры для хранения информации о студентах
struct Student {
    int key;        // Номер зачетки студента
    int variant;    // Номер варианта задачи
};

// Определение размера хеш-таблицы
const int tableSize = 23;

// Определение смещения для метода открытого адреса
const int offset = 1;

// Хеш-функция: остаток от деления номера зачетки на размер таблицы
int hashFunction(int key) {
    return key % tableSize;
}

// Функция для вставки студента в хеш-таблицу с использованием метода открытого адреса
void insertStudent(Student table[], int key, int variant) {
    int index = hashFunction(key);
    
    // Проверка на коллизии и их разрешение с использованием метода открытого адреса
    while (table[index].key != -1) {
        index = (index + offset) % tableSize;
    }

    // Вставка студента в хеш-таблицу
    table[index].key = key;
    table[index].variant = variant;
}

// Функция для вывода хеш-таблицы с заголовками столбцов на русском языке
void printTable(const std::vector<Student>& table) {
    std::cout << "Номер зачетки\tНомер варианта\tКоллизия\n";
    for (const auto& student : table) {
        std::cout << student.key << "\t\t" << student.variant << "\t\t";
        if (student.key == -1) {
            std::cout << "Нет\n";
        } else {
            std::cout << "Да\n";
        }
    }
}

int main() {
    // Инициализация хеш-таблицы студентами
    std::vector<Student> hashTable(tableSize, {-1, -1});

    // Вставка студентов с номерами зачеток: 11, 15, 17, 3, 7, 44, 55, 33, 34, 12
    insertStudent(hashTable.data(), 11, 1);
    insertStudent(hashTable.data(), 15, 2);
    insertStudent(hashTable.data(), 17, 3);
    insertStudent(hashTable.data(), 3, 4);
    insertStudent(hashTable.data(), 7, 5);
    insertStudent(hashTable.data(), 44, 6);
    insertStudent(hashTable.data(), 55, 7);
    insertStudent(hashTable.data(), 33, 8);
    insertStudent(hashTable.data(), 34, 9);
    insertStudent(hashTable.data(), 12, 10);

    // Вывод начальной хеш-таблицы
    printTable(hashTable);
}