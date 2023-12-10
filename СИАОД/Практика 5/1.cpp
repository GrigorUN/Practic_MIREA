#include <iostream>
#include <fstream>

class AVLTree {
private:
    struct TreeNode {
        int key;
        int fileRecord;
        int height;
        TreeNode* left;
        TreeNode* right;

        TreeNode(int k, int fr) : key(k), fileRecord(fr), height(1), left(nullptr), right(nullptr) {}
    };

    TreeNode* root;

    int getHeight(TreeNode* node);
    int getBalance(TreeNode* node);
    TreeNode* rotateRight(TreeNode* y);
    TreeNode* rotateLeft(TreeNode* x);
    TreeNode* insert(TreeNode* node, int key, int fileRecord);
    TreeNode* minValueNode(TreeNode* node);
    TreeNode* remove(TreeNode* node, int key);
    void display(TreeNode* node, int level);

public:
    AVLTree() : root(nullptr) {}
    void insert(int key, int fileRecord);
    void remove(int key);
    void display();
    bool search(int key, int& fileRecord);
};

int AVLTree::getHeight(TreeNode* node) {
    return (node != nullptr) ? node->height : 0;
}

int AVLTree::getBalance(TreeNode* node) {
    return (node != nullptr) ? getHeight(node->left) - getHeight(node->right) : 0;
}

AVLTree::TreeNode* AVLTree::rotateRight(TreeNode* y) {
    TreeNode* x = y->left;
    TreeNode* T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = std::max(getHeight(y->left), getHeight(y->right)) + 1;
    x->height = std::max(getHeight(x->left), getHeight(x->right)) + 1;

    return x;
}

AVLTree::TreeNode* AVLTree::rotateLeft(TreeNode* x) {
    TreeNode* y = x->right;
    TreeNode* T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = std::max(getHeight(x->left), getHeight(x->right)) + 1;
    y->height = std::max(getHeight(y->left), getHeight(y->right)) + 1;

    return y;
}

AVLTree::TreeNode* AVLTree::insert(TreeNode* node, int key, int fileRecord) {
    if (node == nullptr) {
        return new TreeNode(key, fileRecord);
    }

    if (key < node->key) {
        node->left = insert(node->left, key, fileRecord);
    } else if (key > node->key) {
        node->right = insert(node->right, key, fileRecord);
    } else {
        return node;
    }

    node->height = 1 + std::max(getHeight(node->left), getHeight(node->right));

    int balance = getBalance(node);

    if (balance > 1 && key < node->left->key) {
        return rotateRight(node);
    }

    if (balance < -1 && key > node->right->key) {
        return rotateLeft(node);
    }

    if (balance > 1 && key > node->left->key) {
        node->left = rotateLeft(node->left);
        return rotateRight(node);
    }

    if (balance < -1 && key < node->right->key) {
        node->right = rotateRight(node->right);
        return rotateLeft(node);
    }

    return node;
}

AVLTree::TreeNode* AVLTree::minValueNode(TreeNode* node) {
    TreeNode* current = node;
    while (current->left != nullptr) {
        current = current->left;
    }
    return current;
}

AVLTree::TreeNode* AVLTree::remove(TreeNode* node, int key) {
    if (node == nullptr) {
        return node;
    }

    if (key < node->key) {
        node->left = remove(node->left, key);
    } else if (key > node->key) {
        node->right = remove(node->right, key);
    } else {
        if ((node->left == nullptr) || (node->right == nullptr)) {
            TreeNode* temp = (node->left != nullptr) ? node->left : node->right;

            if (temp == nullptr) {
                temp = node;
                node = nullptr;
            } else {
                *node = *temp;
            }

            delete temp;
        } else {
            TreeNode* temp = minValueNode(node->right);
            node->key = temp->key;
            node->fileRecord = temp->fileRecord;
            node->right = remove(node->right, temp->key);
        }
    }

    if (node == nullptr) {
        return node;
    }

    node->height = 1 + std::max(getHeight(node->left), getHeight(node->right));

    int balance = getBalance(node);

    if (balance > 1 && getBalance(node->left) >= 0) {
        return rotateRight(node);
    }

    if (balance < -1 && getBalance(node->right) <= 0) {
        return rotateLeft(node);
    }

    if (balance > 1 && getBalance(node->left) < 0) {
        node->left = rotateLeft(node->left);
        return rotateRight(node);
    }

    if (balance < -1 && getBalance(node->right) > 0) {
        node->right = rotateRight(node->right);
        return rotateLeft(node);
    }

    return node;
}

void AVLTree::display(TreeNode* node, int level) {
    if (node != nullptr) {
        display(node->right, level + 1);
        std::cout << std::string(level * 4, ' ') << node->key << "(" << node->fileRecord << ")" << std::endl;
        display(node->left, level + 1);
    }
}

void AVLTree::insert(int key, int fileRecord) {
    root = insert(root, key, fileRecord);
}

void AVLTree::remove(int key) {
    root = remove(root, key);
}

bool AVLTree::search(int key, int& fileRecord) {
    TreeNode* current = root;
    while (current != nullptr) {
        if (key == current->key) {
            fileRecord = current->fileRecord;
            return true;
        } else if (key < current->key) {
            current = current->left;
        } else {
            current = current->right;
        }
    }
    return false;
}

void AVLTree::display() {
    display(root, 0);
}

class FileManager {
private:
    std::string fileName;

public:
    FileManager(const std::string& name) : fileName(name) {}
    void createBinaryFileFromText(const std::string& textFileName);
    int searchRecordInFile(int key, AVLTree& avl);
    // Добавьте остальные методы управления файлом по вашему усмотрению
};

void FileManager::createBinaryFileFromText(const std::string& textFileName) {
    // Реализовать создание двоичного файла записей из текстового файла
}

int FileManager::searchRecordInFile(int key, AVLTree& avl) {
    int fileRecord = -1;
    avl.search(key, fileRecord);
    if (fileRecord != -1) {
        // Реализовать поиск записи в файле по адресу fileRecord
    }
    return fileRecord;
}

int main() {
    AVLTree avl;
    FileManager fileManager("data.bin");

    // Ручной ввод элементов дерева
    int n;
    std::cout << "Введите количество элементов в дереве: ";
    std::cin >> n;

    for (int i = 0; i < n; ++i) {
        int key, fileRecord;
        std::cout << "Введите ключ элемента " << i + 1 << ": ";
        std::cin >> key;
        std::cout << "Введите ссылку на запись в файле для элемента " << i + 1 << ": ";
        std::cin >> fileRecord;
        avl.insert(key, fileRecord);
    }

    // Вывод дерева
    std::cout << "Дерево:" << std::endl;
    avl.display();

    // Поиск элемента
    int searchKey;
    std::cout << "Введите ключ для поиска: ";
    std::cin >> searchKey;
    int searchResult = -1;
    if (avl.search(searchKey, searchResult)) {
        std::cout << "Элемент с ключом " << searchKey << " найден. Ссылка на запись в файле: " << searchResult << std::endl;
    } else {
        std::cout << "Элемент с ключом " << searchKey << " не найден." << std::endl;
    }

    // Удаление элемента
    int removeKey;
    std::cout << "Введите ключ для удаления: ";
    std::cin >> removeKey;
    avl.remove(removeKey);
    std::cout << "Дерево после удаления элемента с ключом " << removeKey << ":" << std::endl;
    avl.display();

    return 0;
}
