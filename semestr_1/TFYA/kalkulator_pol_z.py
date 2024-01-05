def evaluate_postfix(expression):
    stack = []  # Стек для хранения операндов

    # Разбиваем входное выражение на токены
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            # Если токен - число, помещаем его в стек
            stack.append(int(token))
        else:
            # Если токен - оператор, извлекаем два операнда из стека
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Выполняем операцию, соответствующую оператору
            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            elif token == "/":
                result = operand1 / operand2
            # Результат операции помещаем обратно в стек
            stack.append(result)

    # В конце, стек должен содержать только один элемент, который и будет результатом
    return stack[0]

# Получаем входное выражение от пользователя
input_expression = input("Введите обратную польскую запись: ")
# Вызываем функцию для вычисления и выводим результат
result = evaluate_postfix(input_expression)
print("Результат:", result)
