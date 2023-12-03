#include <iostream>
using namespace std;

struct Tnode {
    int key;
    Tnode* LeftTree;
    Tnode* RightTree;
};

// Операция вставки нового значения в БДП
Tnode* InsertNode(Tnode* root, int value) {
    if (root == NULL) {
        Tnode* newNode = new Tnode;
        newNode->key = value;
        newNode->LeftTree = newNode->RightTree = NULL;
        return newNode;
    }

    if (value < root->key) {
        root->LeftTree = InsertNode(root->LeftTree, value);
    } else if (value > root->key) {
        root->RightTree = InsertNode(root->RightTree, value);
    }

    return root;
}

// Операция удаления узла
Tnode* DeleteNode(Tnode* root, int value) {
    if (root == NULL) {
        return root;
    }

    if (value < root->key) {
        root->LeftTree = DeleteNode(root->LeftTree, value);
    } else if (value > root->key) {
        root->RightTree = DeleteNode(root->RightTree, value);
    } else {
        if (root->LeftTree == NULL) {
            Tnode* temp = root->RightTree;
            delete root;
            return temp;
        } else if (root->RightTree == NULL) {
            Tnode* temp = root->LeftTree;
            delete root;
            return temp;
        }

        Tnode* temp = root->RightTree;
        while (temp->LeftTree != NULL) {
            temp = temp->LeftTree;
        }

        root->key = temp->key;
        root->RightTree = DeleteNode(root->RightTree, temp->key);
    }

    return root;
}

void DeleteTree(Tnode*& root) {
    if (root != NULL) {
        DeleteTree(root->LeftTree);
        DeleteTree(root->RightTree);
        delete root;
        root = NULL;
    }
}

int GetTreeHeight(Tnode* root) {
    if (root == NULL) {
        return 0;
    } else {
        int leftHeight = GetTreeHeight(root->LeftTree);
        int rightHeight = GetTreeHeight(root->RightTree);
        return 1 + max(leftHeight, rightHeight);
    }
}

int GetNodeLevel(Tnode* root, int value, int level = 1) {
    if (root == NULL) {
        return 0;
    }

    if (value == root->key) {
        return level;
    } else if (value < root->key) {
        return GetNodeLevel(root->LeftTree, value, level + 1);
    } else {
        return GetNodeLevel(root->RightTree, value, level + 1);
    }
}

// Отобразить дерево на экране, повернув его справа налево
void PrintTree(Tnode* root, int level, int L) {
    if (root != NULL) {
        PrintTree(root->RightTree, level + 1, L);
        for (int i = 1; i < level * L; i++) {
            cout << ' ';
        }
        cout << root->key << endl;
        PrintTree(root->LeftTree, level + 1, L);
    }
}

// Функция для создания дерева на основе массива значений
Tnode* CreateTree(int values[], int numElements) {
    Tnode* root = NULL;

    for (int i = 0; i < numElements; i++) {
        root = InsertNode(root, values[i]);
    }

    return root;
}

int main() {
    Tnode* root = NULL;

    // Ручной ввод элементов узлов дерева
    int numElements;
    cout << "Введите количество элементов узлов дерева: ";
    cin >> numElements;

    int values[numElements];
    for (int i = 0; i < numElements; i++) {
        cout << "Введите значение " << i + 1 << "-го элемента: ";
        cin >> values[i];
    }

    // Используйте функцию CreateTree для создания дерева
    root = CreateTree(values, numElements);

    // Отобразить дерево на экране
    cout << "Бинарное дерево: " << endl;
    PrintTree(root, 0, 5);
    cout << endl;

    // Пример удаления узла
    int nodeToDelete;
    cout << "Введите значение узла для удаления: ";
    cin >> nodeToDelete;
    root = DeleteNode(root, nodeToDelete);

    // Отобразить дерево после удаления узла
    cout << "Бинарное дерево после удаления узла: " << endl;
    PrintTree(root, 0, 5);
    cout << endl;

    cout << "Высота дерева: " << GetTreeHeight(root) << endl;
    cout << "Глубина значения для узла 10: " << GetNodeLevel(root, 10) << endl;

    // Удалить дерево
    DeleteTree(root);

    return 0;
}
