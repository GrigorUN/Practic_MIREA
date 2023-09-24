# Функция для проверки, является ли токен оператором
def is_operator(token):
    return token in "+-*/"

# Функция для определения приоритета оператора
def precedence(token):
    if token in "+-":
        return 1
    if token in "*/":
        return 2
    return 0  # Приоритет 0 для чисел и скобок

# Функция для преобразования инфиксного выражения в постфиксное
def infix_to_postfix(expression):
    output = []  # Список для хранения выходного постфиксного выражения
    stack = []   # Стек для временного хранения операторов и скобок
    
    # Разбиваем входное выражение на токены (числа, операторы и скобки)
    for token in expression.split():
        if token.isdigit():
            output.append(token)  # Если токен - число, добавляем его в выход
        elif token == "(":
            stack.append(token)   # Если токен - "(", помещаем его в стек
        elif token == ")":
            # Если токен - ")", извлекаем операторы из стека и добавляем их в выход,
            # пока не встретим "("
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()  # Удаляем "(" из стека
        elif is_operator(token):
            # Если токен - оператор, извлекаем операторы из стека и добавляем их в выход,
            # пока приоритет текущего оператора не станет меньше операторов в стеке
            while stack and is_operator(stack[-1]) and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)  # Помещаем текущий оператор в стек
    
    # После обработки всех токенов, извлекаем оставшиеся операторы из стека и добавляем их в выход
    while stack:
        output.append(stack.pop())
    
    # Возвращаем постфиксное выражение, объединив элементы списка через пробел
    return " ".join(output)

# Получаем входное алгебраическое выражение от пользователя
input_expression = input("Введите алгебраическое выражение: ")
# Вызываем функцию для преобразования и выводим результат
postfix_expression = infix_to_postfix(input_expression)
print("Обратная польская запись:", postfix_expression)
