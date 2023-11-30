#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

// Функция для подсчета количества слов, равных последнему слову, и больших последнего слова
void countWords(const string& sentence);

// Функция для поиска префикса строки
vector<int> calculatePrefixFunction(const string& pattern);

int main() {
    // Пример использования
    string exampleSentence = "Это пример для проверки программы, состоящего из слов.";
    countWords(exampleSentence);

    return 0;
}

// Функция для подсчета количества слов, равных последнему слову, и больших последнего слова
void countWords(const string& sentence) {
    istringstream iss(sentence);
    vector<string> words;

    // Разбиваем предложение на слова
    string word;
    while (iss >> word) {
        words.push_back(word);
    }

    // Проверяем, что в предложении есть хотя бы одно слово
    if (words.empty()) {
        cout << "Предложение пусто." << endl;
        return;
    }

    // Получаем последнее слово
    string lastWord = words.back();

    // Подсчет слов, равных последнему, и больших последнего
    int equalCount = count(words.begin(), words.end(), lastWord);
    int greaterCount = count_if(words.begin(), words.end(), [lastWord](const string& w) {
        return w > lastWord;
    });

    // Вывод результатов для первой задачи
    cout << "Количество слов, равных последнему слову: " << equalCount << endl;
    cout << "Количество слов, больших последнего слова: " << greaterCount << endl;

    // Решение второй задачи - поиск минимальной длины строки S после обрезки
    vector<int> prefixFunction = calculatePrefixFunction(sentence);
    int minLength = sentence.length() - prefixFunction[sentence.length() - 1];

    // Вывод результатов для второй задачи
    cout << "Минимальная длина строки S после обрезки: " << minLength << endl;
}

// Функция для поиска префикса строки
vector<int> calculatePrefixFunction(const string& pattern) {
    int m = pattern.length();
    vector<int> prefixFunction(m, 0);

    int k = 0;
    for (int q = 1; q < m; ++q) {
        while (k > 0 && pattern[k] != pattern[q]) {
            k = prefixFunction[k - 1];
        }

        if (pattern[k] == pattern[q]) {
            ++k;
        }

        prefixFunction[q] = k;
    }

    return prefixFunction;
}
