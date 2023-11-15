from ply import lex

tokens = (
    'BEGIN_OBJECT',
    'END_OBJECT',
    'BEGIN_ARRAY',
    'END_ARRAY',
    'COMMA',
    'COLON',
    'LITERAL',
    'STRING',
    'NUMBER',
)

t_BEGIN_OBJECT = r'\{'
t_END_OBJECT = r'\}'
t_BEGIN_ARRAY = r'\['
t_END_ARRAY = r'\]'
t_COMMA = r','
t_COLON = r':'
t_LITERAL = r'true|false|null'


# Регулярное выражение для строк (захватывает символы в двойных кавычках)
def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Убираем двойные кавычки
    return t


# Регулярное выражение для чисел (целые и с плавающей запятой), ? - 0/1, + - 1/inf, * - 0/inf
def t_NUMBER(t):
    r'[+-]?[0-9]+(\.[0-9]+([eE][+-]?[0-9]+)?)?'
    t.value = float(t.value) if '.' in t.value or 'e' in t.value or 'E' in t.value else int(t.value)
    return t


# Пропуск пробелов и переводов строк
t_ignore = ' \t\n'


# Обработка ошибок
def t_error(t):
    print(f"Unrecognized: {t.value[0]}")
    t.lexer.skip(1)


# Создание лексического анализатора
lexer = lex.lex()

if __name__ == "__main__":
    data = '''
    {
    "name": "Misha",
    "age": 26,
    "children": [
    "Masha",
    "Oleg"
    ],
    "married": true
    }
    '''

    lexer.input(data)

    tokenlist = []

    while True:
        token = lexer.token()
        if not token:
            break
        tokenlist.append((token.type, token.value))

    print("Tokenlist:")
    for token in tokenlist:
        print(f"({token[0]}, '{token[1]}')")