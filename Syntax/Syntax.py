class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme

    def __str__(self):
        return f"Token({self.token_type}, '{self.lexeme}')"

from enum import Enum, auto

class TokenType(Enum):
    IDENTIFIER = auto()
    NUMBER = auto()
    FLOAT_NUMBER = auto()
    LOGICAL_CONST = auto()
    LETTER = auto()
    WORD = auto()
    RELATION_OP = auto()
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    SEMICOLON = auto()
    KEYWORD = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    COMMENT = auto()
    HEXADECIMAL = auto() 
    BINARY = auto()
    OCTAL = auto()
    COMMA = auto()
    PERIOD = auto()
    COLON = auto()
    
class State(Enum):
    H = 1
    DECIMAL_NUMBER = 2
    IDENTIFIER = 3
    DATA_TYPE = 4
    HEXADECIMAL = 5
    BINARY = 6
    OCTAL = 7
    ERROR = 8

lexeme_table = {
    TokenType.IDENTIFIER: 'TI',
    TokenType.NUMBER: 'TN',
    TokenType.FLOAT_NUMBER: 'TN',
    TokenType.LOGICAL_CONST: 'TL',
    TokenType.LETTER: 'TW',
    TokenType.WORD: 'TW',
    TokenType.RELATION_OP: 'TO',
    TokenType.LEFT_PAREN: 'TP',
    TokenType.RIGHT_PAREN: 'TP',
    TokenType.SEMICOLON: 'TS',
    TokenType.KEYWORD: 'TK',
    TokenType.LEFT_BRACE: 'TB',
    TokenType.RIGHT_BRACE: 'TB',
    TokenType.LEFT_BRACKET: 'TB',
    TokenType.RIGHT_BRACKET: 'TB',
    TokenType.COMMA: 'TC',
    TokenType.PERIOD: 'TP',
    TokenType.COLON: 'TC'
}

number_tables = {
    'DECIMAL': [],
    'FLOAT_NUMBER': [],
    'HEXADECIMAL': [],
    'BINARY': [],
    'OCTAL': []
}

keyword_table = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'read': 'READ',
    'write': 'WRITE',
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOL',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'true': 'TRUE',
    'false': 'FALSE'
}

operator_table = {
    '+': 'ADD_OP',
    '-': 'ADD_OP',
    'or': 'ADD_OP',
    '*': 'MUL_OP',
    '/': 'MUL_OP',
    'and': 'MUL_OP',
    'not': 'UNARY_OP',
    '<>': 'RELATION_OP',
    '=': 'RELATION_OP',
    '<': 'RELATION_OP',
    '<=': 'RELATION_OP',
    '>': 'RELATION_OP',
    '>=': 'RELATION_OP'
    # ... другие операторы, если есть ...
}

identifier_table = {}

new_lexeme_table = {
    'IDENTIFIER': TokenType.IDENTIFIER,
    'NUMBER': TokenType.NUMBER,
    'LOGICAL_CONST': TokenType.LOGICAL_CONST,
    'if': TokenType.KEYWORD,
    'else': TokenType.KEYWORD,
    'while': TokenType.KEYWORD,
    'for': TokenType.KEYWORD,
    'read': TokenType.KEYWORD,
    'write': TokenType.KEYWORD,
    'int': TokenType.KEYWORD,
    'float': TokenType.KEYWORD,
    'bool': TokenType.KEYWORD,
    'and': TokenType.KEYWORD,
    'or': TokenType.KEYWORD,
    'not': TokenType.KEYWORD,
    'true': TokenType.KEYWORD,
    'false': TokenType.KEYWORD,
    '(': TokenType.LEFT_PAREN,
    ')': TokenType.RIGHT_PAREN,
    '[': TokenType.LEFT_BRACKET,
    ']': TokenType.RIGHT_BRACKET,
    '{': TokenType.LEFT_BRACE,
    '}': TokenType.RIGHT_BRACE,
    ',': TokenType.COMMA,
    ';': TokenType.SEMICOLON,
    '.': TokenType.PERIOD,
    ':': TokenType.COLON,
    '0b': TokenType.BINARY,
    '0o': TokenType.OCTAL,
    '0x': TokenType.HEXADECIMAL
}


tokens = ['IDENTIFIER', '+', 'NUMBER', '<', 'NUMBER', 'or', 'LOGICAL_CONST']
current_token_index = 0

def lexeme():
    global current_token_index
    if current_token_index < len(tokens):
        return tokens[current_token_index]
    else:
        return None  # Возвращает None, если достигнут конец списка лексем

def get_next_token():
    global current_token_index
    if current_token_index < len(tokens):
        current_token = tokens[current_token_index]
        current_token_index += 1
        return current_token
    else:
        return None  # Возвращает None, если достигнут конец списка лексем

def is_letter(char):
    return 'A' <= char <= 'Z' or 'a' <= char <= 'z'

def is_digit(char):
    return '0' <= char <= '9'

def error(message):
    print(f"Error: {message}")
    exit(1)  # Завершение выполнения программы с кодом ошибки 1

def identifier():
    lex = lexeme()
    if lex in keyword_table:
        print(Token(keyword_table[lex], lex))
    elif lex.isalpha():
        print(Token(TokenType.IDENTIFIER, lex))
    else:
        error("201 - Expected an identifier")

    get_next_token()
    
def number():
    lex = lexeme()
    if lex.startswith(('0x', '0X')):
        hexadecimal()
    elif lex.startswith(('0b', '0B')):
        binary()
    elif lex.startswith(('0o', '0O')):
        octal()
    elif lex.isdigit():
        decimal()
    else:
        error("101 - Expected a number")

    # Проверки на дополнительные ошибки
    if lex.endswith(('e', 'E', '.', 'b', 'B')):
        error("103 - Expected number continuation after " + lex[-1])
    elif 'e' in lex or 'E' in lex:
        if '.' not in lex:
            error("105 - Expected a dot in a floating-point number after 'e' or 'E'")
        elif lex.count('e') + lex.count('E') > 1:
            error("112 - Multiple 'e' or 'E' in number")
        elif lex.endswith(('e', 'E')):
            error("106 - Expected continuation after 'e' or 'E'")
    elif lex.endswith(('d', 'D')):
        error("107 - Expected absence of 'd' or 'D' after number")
    elif lex.endswith(('h', 'H', 'o', 'O')):
        error("104 - Expected continuation after 'h', 'H', 'o', or 'O'")


def binary():
    lex = lexeme()[:-1]  # Убираем символ обозначения двоичного числа (B/b)
    if all(bit in ('0', '1') for bit in lex):
        number = int(lex, 2)
        number_tables['BINARY'].append(number)  # Добавляем число в таблицу двоичных чисел
        lexeme_table[TokenType.BINARY] = 'TN'  # Обновляем таблицу лексем
    else:
        error("Invalid binary number format")  # Если есть символы, отличные от 0 и 1, вызываем ошибку
    get_next_token()  # Переход к следующей лексеме

def octal():
    lex = lexeme()  # получаем текущую лексему
    if lex.startswith('0o') or lex.startswith('0O'):
        if all(digit in '01234567' for digit in lex[2:]):
            number = int(lex, 8)
            number_tables['OCTAL'].append(number)  # Добавляем в таблицу восьмеричных чисел
            lexeme_table[TokenType.OCTAL] = 'TN'  # Обновляем таблицу лексем
        else:
            error("Incorrect octal number format")  # В противном случае, ошибка формата числа
    else:
        error("Incorrect octal number format")
    get_next_token()  # Переход к следующей лексеме

def decimal():
    lex = lexeme()
    if lex.isdigit():
        number = int(lex)
        number_tables['DECIMAL'].append(number)
        lexeme_table[TokenType.DECIMAL] = 'TN'
    else:
        error("Incorrect decimal format")
    get_next_token()

def hexadecimal():
    lex = lexeme()[:-1]  # Убираем символ обозначения шестнадцатеричного числа (H/h)
    valid_hex_chars = '0123456789ABCDEFabcdef'
    if lex.startswith(('0x', '0X')):
        if all(char in valid_hex_chars for char in lex[2:]):
            number = int(lex, 16)
            number_tables['HEXADECIMAL'].append(number)  # Добавляем число в таблицу шестнадцатеричных чисел
            lexeme_table[TokenType.HEXADECIMAL] = 'TN'  # Обновляем таблицу лексем
        else:
            error("Invalid hexadecimal format")  # Если есть недопустимые символы, вызываем ошибку
    else:
        error("Invalid hexadecimal format")
    get_next_token()  # Переход к следующей лексеме

def logical_constant():
    lex = lexeme()
    if lex == 'True' or lex == 'False':
        lexeme_table[lex] = TokenType.LOGICAL_CONST  # Добавляем логическую константу в таблицу лексем
    else:
        error("Expected boolean constant True or False")  # Если лексема не является логической константой, вызываем ошибку

def multi_line_comment():
    if lexeme() == '/*':
        get_next_token()
        while lexeme() != '*/':
            if lexeme() is None:
                error("Reached end of file before closing comment")  # Если достигнут конец файла до закрытия комментария, вызываем ошибку
            get_next_token()
        get_next_token()  # Переходим к следующей лексеме после закрывающего тега '*/'
    else:
        error("Expected comment to start '/*'")  # Если не начат комментарий '/*', вызываем ошибку
       
def real():
    numerical_string()
    if lexeme() in {'E', 'e'}:
        get_next_token()
        if lexeme() in {'+', '-'}:
            get_next_token()
        numerical_string()
    else:
        error("106 - Expected 'e' or 'E'")

def numerical_string():
    if lexeme().isdigit():
        while lexeme().isdigit():
            get_next_token()
        if lexeme() == '.':
            get_next_token()
            while lexeme().isdigit():
                get_next_token()
        if lexeme() in {'E', 'e'}:
            error("105 - Unexpected '.' after 'e'")
    else:
        error("112 - Expected a digit")

def program():
    if lexeme() == '{':
        get_next_token()
        while lexeme() != '}':
            if lexeme() == ';':
                get_next_token()
            elif lexeme() == 'IDENTIFIER' or lexeme() == 'NUMBER':
                description()
            else:
                error("202 - Expected ';' or description/operator")
        if lexeme() == '}':
            get_next_token()
        else:
            error("204 - Missing closing curly brace '}'")
    else:
        error("203 - Missing opening curly brace '{'")

def description():
    data_type()
    if lexeme() == 'IDENTIFIER':
        identifiers_list()
    
def assignment():
    identifier()
    if lexeme() == 'as':
        get_next_token()
        expression()  # Обработка выражения для присваивания
    else:
        error("209 - Expected 'as'")

# Добавление проверок в функцию `conditional()`
def conditional():
    if lexeme() == 'if':
        get_next_token()
        expression()  # Обработка условия
        if lexeme() == 'then':
            get_next_token()
            program_operator()  # Обработка блока кода
            if lexeme() == 'else':
                get_next_token()
                program_operator()  # Обработка блока кода else
            else:
                error("210 - Missing 'else' after if-then block")
        else:
            error("210 - Missing 'then' after condition")
    else:
        error("215 - Condition not met 'if'")

def fixed_loop():
    if lexeme() == 'for':
        get_next_token()
        assignment()  # Обработка инициализации
        if lexeme() == 'to':
            get_next_token()
            expression()  # Обработка условия цикла
            if lexeme() == 'do':
                get_next_token()
                program_operator()    
            else:
                error("Missing 'do' after loop condition")  # Если отсутствует do после условия цикла, вызываем ошибку
        else:
            error("Missing 'to' after initialization")  # Если отсутствует to после инициализации, вызываем ошибку
    else:
        error("'for' condition not met")  # Если не выполнено условие 'for', вызываем ошибку

# Добавление проверок в функцию `conditional_loop()`
def conditional_loop():
    if lexeme() == 'while':
        get_next_token()
        expression()  # Обработка условия цикла
        if lexeme() == 'do':
            get_next_token()
            program_operator()  # Обработка блока кода
        else:
            error("213 - Missing 'do' after loop condition")
    else:
        error("216 - 'while' condition failed")

# Добавление проверок в функцию `input_op()`
def input_op():
    if lexeme() == 'read':
        get_next_token()
        if lexeme() == '(':
            get_next_token()
            while lexeme() != ')':
                if lexeme() == 'IDENTIFIER':
                    # Добавить идентификатор в таблицу ввода данных
                    identifier_table[lexeme()] = TokenType.IDENTIFIER
                    get_next_token()
                    if lexeme() == ',':
                        get_next_token()
                    elif lexeme() != ')':
                        error("218 - Syntax error: missing ')'")  # Ошибка в синтаксисе
                else:
                    error("218 - ID expected")  # Ожидается идентификатор
            get_next_token()  # Переходим к следующей лексеме после ')'
        else:
            error("218 - Syntax error: missing '('")  # Ошибка в синтаксисе
    else:
        error("218 - Error: Read operation 'read' was expected")  # Ошибка: ожидалась операция чтения 'read'
        
# Добавление проверок в функцию `output_op()`
def output_op():
    if lexeme() == 'write':
        get_next_token()
        if lexeme() == '(':
            get_next_token()
            while lexeme() != ')':
                expression()  # Обработка выражения для вывода
                if lexeme() == ',':
                    get_next_token()
                elif lexeme() != ')':
                    error("218 - Syntax error: missing ')'")  # Ошибка в синтаксисе
            get_next_token()  # Переходим к следующей лексеме после ')'
        else:
            error("218 - Syntax error: missing '('")  # Ошибка в синтаксисе
    else:
        error("218 - Error: 'write' operation expected")  # Ошибка: ожидалась операция записи 'write'

# Добавление проверок в функцию `variable_declaration()`
def variable_declaration():
    data_type()
    identifiers_list()

# Добавление проверок в функцию `data_type()`
def data_type():
    if lexeme() in ['int', 'float', 'bool']:
        lexeme_table[lexeme()] = TokenType.DATA_TYPE
        get_next_token()
    else:
        error("207 - Data type is not as expected")  # Если тип данных не соответствует ожидаемым, вызываем ошибку

# Добавление проверок в функцию `identifiers_list()`
def identifiers_list():
    identifier()
    while lexeme() == ',':
        get_next_token()
        if lexeme() == 'IDENTIFIER':
            get_next_token()
        else:
            error("205 - Expected IDENTIFIER after ',' in identifiers_list")

# Добавление проверок в функцию `program_operator()`
def program_operator():
    if lexeme() == '{':
        compound()
    elif lexeme() == 'IDENTIFIER':
        assignment()
    elif lexeme() == 'if':
        conditional()
    elif lexeme() == 'for_fixed':
        fixed_loop()
    elif lexeme() == 'for':
        conditional_loop()
    elif lexeme() == 'input':
        input_op()
    elif lexeme() == 'output':
        output_op()
    else:
        error("218 - None of the conditions are met")  # Если ни одно из условий не выполнено, вызываем ошибку


# Добавление проверок в функцию `compound()`
def compound():
    if lexeme() == '[':
        get_next_token()
        while lexeme() not in [']', 'EOF']:
            program_operator()
            if lexeme() in [':', 'NEWLINE']:
                get_next_token()
            else:
                error("203 - Missing ':' or newline")
        if lexeme() == ']':
            get_next_token()
            if lexeme() not in [':', 'NEWLINE']:
                error("203 - Missing ':' or newline after last operator in compound")
        else:
            error("208 - Missing closing square bracket ']'")
    else:
        error("208 - Missing opening square bracket '['")

# Добавление проверок в функцию `term()`
def term():
    factor()
    while lexeme() in MUL_OP:
        get_next_token()
        factor()

# Добавление проверок в функцию `operand()`
def operand():
    term()
    while lexeme() in ADD_OP:
        get_next_token()
        term()

# Добавление проверок в функцию `expression()`
def expression():
    operand()
    while lexeme() in RELATION_OP:
        get_next_token()
        operand()

# Добавление проверок в функцию `factor()`
def factor():
    if lexeme() == 'IDENTIFIER':
        identifier()
    elif lexeme() == 'NUMBER':
        number()
    elif lexeme() == 'LOGICAL_CONST':
        logical_constant()
    elif lexeme() == 'UNARY_OP':
        get_next_token()
        factor()
    elif lexeme() == '(':
        get_next_token()
        expression()
        if lexeme() == ')':
            get_next_token()
        else:
            error("217 - Missing closing bracket ')'")  # Если нет закрывающей скобки ')', вызываем ошибку
    else:
        error("218 - Unidentified token")  # Если неопознанная лексема, вызываем ошибку


def tokenize_input(input_string):
    tokens = []
    current_token = ""
    i = 0
    while i < len(input_string):
        if input_string[i].isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
        elif input_string[i:i+2] == '//':
            if current_token:
                tokens.append(current_token)
                current_token = ""
            end_of_line = input_string.find('\n', i+2)
            if end_of_line == -1:
                end_of_line = len(input_string)
            i = end_of_line if end_of_line != -1 else len(input_string)
        elif input_string[i:i+2] == '/*':
            if current_token:
                tokens.append(current_token)
                current_token = ""
            end_comment = input_string.find('*/', i+2)
            if end_comment == -1:
                error("218 - Error: Unclosed multiline comment")
            i = end_comment + 2
        elif input_string[i] in {'{', '}', ';', '(', ')'}:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(input_string[i])
        else:
            current_token += input_string[i]
            if current_token.startswith(('0o', '0O')):
                octal_number = current_token[2:]
                if all(d in '01234567' for d in octal_number):
                    tokens.pop()
                    tokens.append("Token(TokenType.OCTAL, '" + current_token + "')")
                    current_token = ""
        i += 1
    
    if current_token:
        tokens.append(current_token)

    return tokens

def handle_keywords(tokens):
    i = 0
    while i < len(tokens) - 1:
        if tokens[i].startswith("Token(TokenType.KEYWORD"):
            next_token = tokens[i + 1]
            if next_token.startswith("Token(TokenType.LETTER"):
                tokens[i + 1] = "Token(TokenType.IDENTIFIER, '" + next_token.lexeme + "')"
        i += 1
    
    return tokens

def process_tokens(tokens):
    identifier_expected = False  # Флаг для ожидания идентификатора после ключевых слов
    for token in tokens:
        if not token.startswith("Token(TokenType.COMMENT"):
            if identifier_expected and token.isalpha():
                print(Token(TokenType.IDENTIFIER, token))
        
                identifier_expected = False
            elif token.isdigit():
                print(Token(TokenType.NUMBER, token))
                identifier_expected = False
            elif token.startswith(('0x', '0X')):
                print(Token(TokenType.HEXADECIMAL, token))
                identifier_expected = False
            elif token.startswith(('0b', '0B')):
                print(Token(TokenType.BINARY, token))
                identifier_expected = False
            elif token.startswith(('0o', '0O')) and all(d in '01234567' for d in token[2:]):
                print(Token(TokenType.OCTAL, token))
                identifier_expected = False
            elif token in operator_table:
                print(Token(operator_table[token], token))
                identifier_expected = False
            elif len(token) == 1 and token.isalpha():
                print(Token(TokenType.LETTER, token))
                identifier_expected = True
            elif token.isalpha():
                if token == 'true':
                    print(Token(TokenType.LOGICAL_CONST, token))
                    identifier_expected = False
                elif token == 'false':
                    print(Token(TokenType.LOGICAL_CONST, token))
                    identifier_expected = False
                elif token in keyword_table:
                    print(Token(TokenType.KEYWORD, token))
                    identifier_expected = True
                else:
                    print(Token(TokenType.IDENTIFIER, token))
                    identifier_expected = False
            elif '.' in token and token.replace('.', '').isdigit():
                print(Token(TokenType.FLOAT_NUMBER, token))
                identifier_expected = False
            elif token.startswith("Token"):
                print(token) 
                    
                if token.startswith("Token"):
                    print(token)
                elif token in new_lexeme_table:
                    print(Token(new_lexeme_table[token], token))
                    identifier_expected = False
                else:
                    print(Token(TokenType.IDENTIFIER, token))
                    identifier_expected = False
            else:
                error("302 - Usage of undeclared variable: " + token)

def handle_identifiers(tokens):
    i = 0
    while i < len(tokens) - 1:
        if tokens[i].startswith("Token(TokenType.KEYWORD") and tokens[i+1].isalnum():
            tokens[i+1] = "Token(TokenType.IDENTIFIER, '" + tokens[i+1] + "')"
        elif tokens[i] == "Token(TokenType.IDENTIFIER" and tokens[i+1] not in identifier_table:
            error("302 - Usage of undeclared variable: " + tokens[i+1])
        i += 1
    
    return tokens

def analyze_input(input_string):
    tokens = tokenize_input(input_string)
    tokens = handle_identifiers(tokens)
    process_tokens(tokens)


input_data = [
"""
int x;
x = 5;
y = 10;  // Использование необъявленной переменной 'y'
"""
]

for statement in input_data:
    analyze_input(statement)


"int x; int y; x = 123; y = 456; // Example"
"{ int x; int y; x = 5; y = 10; }"
"0 0xFF 0b1010 0765 true <= // Some comments" 
"<>  =  <  <=  >  >= +  -  or *  / and not" 
"true false" 
"Q A W S E D R F T G Y H U J I K O L P Z X C V B N M"
"q a w s e d r f t g y h u j i k o l p z x c v b n m"
"0 1 2 3 4 5 6 7 8 9" 
"( ) { } [ ] ; , ."

"int x;",
"float y;",
"x = 5;",
"y = 10.5;"

"""
int x;
int y;
x = 5;
y = 10.0;
    
if (x < y) {
x = x + 1;
} else {
y = y - 1;
}
"""

"""
int x;
x = 0;

for (x = 0; x < 5; x = x + 1) {
    x = x + 1;
}
"""


"input_string = "
"analyze_input(input_string)"


"input_data = []"
"for statement in input_data:"
"analyze_input(statement)"