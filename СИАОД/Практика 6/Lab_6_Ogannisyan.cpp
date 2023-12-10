#include <iostream>
#include <vector>
#include <queue>

using namespace std;
// Структура для представления ребра графа
struct Edge {
    int source;
    int destination;
    int weight; // если граф взвешенный
};

// Класс для представления графа
class Graph {
public:
    // Конструктор
    Graph(int vertices, bool weighted);

    // Метод для добавления ребра
    void addEdge(int source, int destination, int weight);

    // Методы для ввода и вывода графа
    void inputGraph();
    void printGraph();

    // Алгоритмы задач
    bool isConnected(); // Определить связность графа
    void findDominatingSets(); // Определить доминирующие множества графа

private:
    int vertices; // количество вершин
    bool weighted; // является ли граф взвешенным
    vector<Edge> edges; // вектор для хранения рёбер графа
};

// Реализация методов класса Graph
Graph::Graph(int vertices, bool weighted) : vertices(vertices), weighted(weighted) {}

void Graph::addEdge(int source, int destination, int weight) {
    Edge edge = {source, destination, weight};
    edges.push_back(edge);
}

void Graph::inputGraph() {
    int source, destination, weight;

    cout << "Введите ребра графа (source destination weight): " << endl;
    for (int i = 0; i < vertices; ++i) {
        cin >> source >> destination;
        if (weighted) {
            cin >> weight;
        } else {
            weight = 0; // если граф не взвешенный, присваиваем вес 0
        }
        addEdge(source, destination, weight);
    }
}

void Graph::printGraph() {
    cout << "Граф представлен списками смежных вершин:" << endl;
    for (const auto &edge : edges) {
        cout << edge.source << " -> " << edge.destination;
        if (weighted) {
            cout << " (вес: " << edge.weight << ")";
        }
        cout << endl;
    }
}

bool Graph::isConnected() {
    // Используем BFS для определения связности графа
    vector<bool> visited(vertices, false);
    queue<int> q;

    // Начинаем с первой вершины
    q.push(0);
    visited[0] = true;

    while (!q.empty()) {
        int current = q.front();
        q.pop();

        // Проходим по всем смежным вершинам
        for (const auto &edge : edges) {
            if (edge.source == current && !visited[edge.destination]) {
                q.push(edge.destination);
                visited[edge.destination] = true;
            }
        }
    }

    // Если все вершины посещены, граф связный
    for (bool v : visited) {
        if (!v) {
            return false;
        }
    }
    return true;
}

void Graph::findDominatingSets() {
    // Используем жадный алгоритм для поиска доминирующих множеств
    vector<int> dominatingSet;

    // Идем по всем вершинам
    for (int i = 0; i < vertices; ++i) {
        bool isDominated = false;

        // Проверяем, доминируется ли текущая вершина
        for (const auto &edge : edges) {
            if (edge.destination == i) {
                isDominated = true;
                break;
            }
        }

        // Если не доминируется, добавляем в множество
        if (!isDominated) {
            dominatingSet.push_back(i);
        }
    }

    // Выводим результат
    cout << "Доминирующее множество: ";
    for (int vertex : dominatingSet) {
        cout << vertex << " ";
    }
    cout << endl;
}

int main() {
    // Пример использования класса Graph
    int vertices;
    bool weighted;

    cout << "Введите количество вершин графа: ";
    cin >> vertices;

    cout << "Граф взвешенный? (1 - да, 0 - нет): ";
    cin >> weighted;

    Graph myGraph(vertices, weighted); // Создаем граф

    myGraph.inputGraph();   // Вводим граф с клавиатуры
    myGraph.printGraph();   // Выводим граф в виде списков смежных вершин

    // Проверяем связность графа
    if (myGraph.isConnected()) {
        cout << "Граф связный." << endl;
    } else {
        cout << "Граф не связный." << endl;
    }

    // Находим доминирующие множества графа
    myGraph.findDominatingSets();

    return 0;
}
