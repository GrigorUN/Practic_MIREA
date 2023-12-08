#include <iostream>
#include <string>
using namespace std;

const int TABLE_SIZE = 10; // Размер хеш-таблицы

struct HashTableElement {
    string key; // ключ элемента
    int value; // значение элемента
    bool flag; // флаг
};

class HashTable {
private:
    HashTableElement table[TABLE_SIZE]; // массив элементов
    int hashFunction(const string& key); // метод для вычисления индекса элемента в таблице на основе ключа

public:
    HashTable(); // конструктор класса
    void insert(const string& key, int value); // метод для вставки
    int search(const string& key); // метод для поиска
    void remove(const string& key);
};

HashTable::HashTable() {    
    // Инициализация таблицы
    for (int i = 0; i < TABLE_SIZE; ++i) {
        table[i].key = "";
        table[i].value = 0;
        table[i].flag = false;
    }
}

int HashTable::hashFunction(const string& key) {
    int sum = 0;
    for (char ch : key) {
        sum += static_cast<int>(ch);
    }
    return sum % TABLE_SIZE;
}

void HashTable::insert(const string& key, int value) {
    int index = hashFunction(key);
    while (table[index].flag) { // если ячейка уже занята
        index = (index + 1) % TABLE_SIZE; // производим смещение на 1
    }
    table[index].key = key;
    table[index].value = value;
    table[index].flag = true;
}

int HashTable::search(const string& key) {
    int index = hashFunction(key);
    while (table[index].flag) {
        if (table[index].key == key) {
            return table[index].value; // найден элемент с заданным ключом
        }
        index = (index + 1) % TABLE_SIZE; // производим смещение на 1
    }
    return -1; // элемент с заданным ключом не найден
}

void HashTable::remove(const string& key) {
    int index = hashFunction(key);
    while (table[index].flag) {
        if (table[index].key == key) {
            table[index].flag = false;
            return;
        }
        index = (index + 1) % TABLE_SIZE;
    }
}

int main() {
    HashTable hashTable;

    // Вставляем элементы в хеш-таблицу
    hashTable.insert("1", 10);
    hashTable.insert("2", 20);
    hashTable.insert("3", 30);

    // Поиск элементов по ключу
    string keyToSearch = "4";
    int foundValue = hashTable.search(keyToSearch);
    if (foundValue != -1) {
        std::cout << "Значение для ключа " << keyToSearch << ": " << foundValue << std::endl;
    } else {
        std::cout << "Элемент с ключом " << keyToSearch << " не найден." << std::endl;
    }

    // Удаление элемента
    hashTable.remove("2");

    return 0;
}
