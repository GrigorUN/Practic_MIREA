#ЦИФРЫ

DIGITS ='0123456789'
#ERROR
class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name} {self.details}'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end,'Ошибка!', details)

# ПОЗИЦИЯ ОШИБКИ 
class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self
    
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)
    


#ТОКЕНЫ
TT_PLUS = 'PLUS'
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV= 'DEL'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
# TT_PR = 'PROGRAM'
# TT_VAR = 'VAR'
# TT_BEGIN = 'BEGIN'
# TT_END = 'END'

class Token:
    def __init__(self, type_, value = None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
    


class Lexer:
    def __init__(self, fn, text): #инициализация текста
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self): #переход к след символу
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    #Создание токенов
    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t': #проверка пробелов и табуляции
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            # elif self.current_char == 'program':
            #     tokens.append(Token(TT_PR))
            #     self.advance()
            # elif self.current_char == 'var':
            #     tokens.append(Token(TT_VAR))
            #     self.advance()
            # elif self.current_char == 'begin':
            #     tokens.append(Token(TT_BEGIN))
            #     self.advance()
            # elif self.current_char == 'end':
            #     tokens.append(Token(TT_END))
            #     self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos,"'" + char + "'\n")

        return tokens, None
    

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count +=1
                num_str +='.'
            else: 
                num_str += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else: 
            return Token(TT_FLOAT,float(num_str))
        

#Запуск
def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error
