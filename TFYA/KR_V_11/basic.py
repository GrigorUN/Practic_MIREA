
# Токены
TT_PLUS         = 'PLUS'
TT_INT          = 'INT'
TT_FLOAT        = 'FLOAT'
TT_STRING       = 'STRING'
TT_MINUS        = 'MINUS'
TT_MUL          = 'MUL'
TT_DIV          = 'DEL'
TT_POW          = 'POW'
TT_LPAREN       = 'LPAREN'
TT_RPAREN       = 'RPAREN'
TT_LSQUARE      = 'LSQUARE'
TT_RSQUARE      = 'RSQUARE'
TT_IDENTIFIER   = 'IDENTIFIER'
TT_KEYWORD      = 'KEYWORDS'
TT_EQ           = 'ASSIGN'
TT_EE           = 'EE' #равно
TT_NE           = 'NE' # не равно
TT_LT           = 'LT'
TT_GT           = 'GT'
TT_LTE          = 'LTE'
TT_GTE          = 'GTE'
TT_COMMA        = 'COMMA'
TT_ARROW        = 'ARROW'
TT_NEWLINE      = 'NEWLINE'
TT_EOF          = 'EOF'

# Функция, возвращающая следующий символ из входного текста
def get_next_char():
    global input_text
    if input_text:
        return input_text[0]
    return None

# Функция, потребляющая обработанный символ из входного текста
def consume_char():
    global input_text
    if input_text:
        input_text = input_text[1:]

# Открываем текстовый файл для чтения
with open("./example.txt", "r") as file:
    input_text = file.read()

# Определение структур данных для хранения лексем
class Token:
    def __init__(self, token_category, token_value):
        self.token_category = token_category
        self.token_value = token_value

class LexemeTable:
    def __init__(self):
        self.lexemes = []

    def add_token(self, token):
        self.lexemes.append(token)
        print(f"Категория токена: {token.token_category}")
        print(f"Значение токена: {token.token_value}")

# Инициализация таблицы лексем
lt = LexemeTable()

# Функция для проверки, является ли идентификатор ключевым словом
def is_keyword(identifier):
    keywords = ["FOR", "TO", "STEP", "IF", "ELSE", "WHILE", "BEGIN", "END.", "NEXT", "VAR", "READLN", "WRITLN", "PROGRAM"]
    return identifier in keywords

# Функция для обработки лексем и добавления их в таблицу
def add_token(token):
    lt.add_token(token)

# Функция лексического анализа
def lex_analyzer():
    tokens = []

    while input_text:
        current_char = get_next_char()

        if current_char.isspace(): # Пропускаем пробелы
            while current_char.isspace():
                consume_char()
                current_char = get_next_char()
            continue # Пропускаем текущую итерацию
        
        if current_char == ':':
            consume_char()
            if get_next_char() == '=':
                consume_char()
                token = Token("операторы присваивания", ":=")
                add_token(token)
            add_token(token)
        elif current_char == '"':
            consume_char()
            token = Token("двойные кавычки", '"')
            add_token(token)
        elif current_char == '&':
            consume_char()
            if get_next_char() == '&':
                consume_char()
                token = Token("логическое 'и'", "&&")
                add_token(token)
        elif current_char == '|':
            consume_char()
            if get_next_char() == '|':
                consume_char()
                token = Token("логическое 'или'", "||")
                add_token(token)
        elif current_char == '!':
            consume_char()
            token = Token("логическое 'не'", '!')
            add_token(token)
        elif current_char.isalpha():
            identifier = current_char
            consume_char()
        elif current_char == '(':
            consume_char()
            token = Token("открывающаясь скобка", '(')
            add_token(token)
        elif current_char == ')':
            consume_char()
            token = Token("закрывающаясь скобка", ')')
            add_token(token)
        elif current_char == ';':
            consume_char()
            token = Token("точка с запятой", ';')
            add_token(token)
        elif current_char == '<':
            consume_char()
            if get_next_char() == '=':
                consume_char()
                token = Token("знак небольше", "'<=' ")
                add_token(token)
            else:
                token = Token("знак меньше", '<')
                add_token(token)
        elif current_char == '>':
            consume_char()
            if get_next_char() == '=':
                consume_char()
                token = Token("знак неменьше", "'>=' ")
                add_token(token)
            else:
                token = Token("знак больше", '>')
                add_token(token)
            add_token(token)
        elif current_char == '+':
            consume_char()
            token = Token("плюс", '+')
            add_token(token)
        elif current_char == '-':
            consume_char()
            token = Token("минус", '-')
            add_token(token)
        elif current_char == '*':
            consume_char()
            token = Token("умножение", '*')
            add_token(token)
        elif current_char == '/':
            consume_char()
            token = Token("деление", '/')
            add_token(token)

            while get_next_char().isalnum() or get_next_char() == '_':
                identifier += get_next_char()
                consume_char()
            if is_keyword(identifier):
                token = Token("ключевые слова", identifier)
            else:
                token = Token("идентификаторы", identifier)
            add_token(token)

        elif current_char.isdigit() or current_char == '-':
            number = current_char
            consume_char()
            while get_next_char().isdigit() or get_next_char() in '.eE+-':
                number += get_next_char()
                consume_char()
            token = Token("десятичные числа", number)
            add_token(token)
        else:
            consume_char()
            print("Категория токена: ошибка") # Нераспознанный символ
            print(f"Значение токена: ({current_char})")
            print("Неизвестный токен")

# Вызываем лексический анализатор
lex_analyzer()
