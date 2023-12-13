import re

# Токены
tokens = [
    ('PROGRAM', r'program'),
    ('VAR', r'var'),
    ('BEGIN', r'begin'),
    ('END', r'end\.'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z_0-9]*'),
    ('OPERATOR', r'!=|==|<|<=|>|>=|\+|-|\|\||\*|/|&&'),
    ('UNARY_OP', r'!'),
    ('TYPE', r'%|!|\$'),
    ('NUMBER', r'\d+'),
    ('ASSIGN', r':='),
    ('SEMICOLON', r';'),
    ('COLON', r':'),
    ('COMMA', r','),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('FOR', r'for'),
    ('TO', r'to'),
    ('STEP', r'step'),
    ('NEXT', r'next'),
    ('IF', r'if'),
    ('ELSE', r'else'),
    ('WHILE', r'while'),
    ('READLN', r'readln'),
    ('WRITELN', r'writeln'),
    ('SKIP', r'[ \t\n]+'),  # Пробелы и переводы строк (игнорируются)
    ('MISMATCH', r'.')     # Любой другой символ
]

def tokenize(code):
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)
    get_token = re.compile(tok_regex).match
    line = 1
    pos = line_start = 0
    mo = get_token(code)
    while mo is not None:
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value} on line {line} at position {pos}')
        else:
            yield kind, value, line, pos
        pos = mo.end()
        mo = get_token(code, pos)
        if '\n' in value:
            line_start = pos
            line += 1

# Пример использования
code = """
program var x, y : %; 
begin 
    x := 10;
    || && 
    y := x + 20; 
end.
"""

# Токенизация кода
for token in tokenize(code):
    print(token)
