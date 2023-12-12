from enum import Enum, auto

class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme

    def __str__(self):
        return f"Token({self.token_type}, '{self.lexeme}')"

class TokenType(Enum):
    # ... (как в предыдущем коде)

# Пример лексического анализатора
    def tokenize_input(input_string):
        tokens = []
        current_token = ""
        i = 0

        while i < len(input_string):
            if input_string[i].isspace():
                i += 1
            elif input_string[i:i+2] == '!=':
                tokens.append(Token(TokenType.RELATIONAL_OP_NOT_EQUAL, '!='))
                i += 2
            elif input_string[i:i+2] == '==':
                tokens.append(Token(TokenType.RELATIONAL_OP_EQUAL, '=='))
                i += 2
            elif input_string[i] in {'<', '>', '=', ';', ',', ':'}:
                tokens.append(Token(TokenType(input_string[i]), input_string[i]))
                i += 1
            elif input_string[i:i+2] == '<=':
                tokens.append(Token(TokenType.RELATIONAL_OP_LESS_THAN_EQUAL, '<='))
                i += 2
            elif input_string[i:i+2] == '>=':
                tokens.append(Token(TokenType.RELATIONAL_OP_GREATER_THAN_EQUAL, '>='))
                i += 2
            elif input_string[i:i+2] == '&&':
                tokens.append(Token(TokenType.MULTIPLICATION_OP_LOGICAL_AND, '&&'))
                i += 2
            elif input_string[i:i+2] == '||':
                tokens.append(Token(TokenType.ADDITION_OP_CONCATENATION, '||'))
                i += 2
            elif input_string[i] in {'+', '-', '*', '/', '!'}:
                tokens.append(Token(TokenType(input_string[i]), input_string[i]))
                i += 1
            elif input_string[i] == '(':
                tokens.append(Token(TokenType.LEFT_PAREN, '('))
                i += 1
            elif input_string[i] == ')':
                tokens.append(Token(TokenType.RIGHT_PAREN, ')'))
                i += 1
            elif input_string[i] == '{':
                tokens.append(Token(TokenType.COMPOUND_BEGIN, '{'))
                i += 1
            elif input_string[i] == '}':
                tokens.append(Token(TokenType.COMPOUND_END, '}'))
                i += 1
            elif input_string[i] == ':':
                tokens.append(Token(TokenType.COLON, ':'))
                i += 1
            elif input_string[i] == '%':
                tokens.append(Token(TokenType.DATA_TYPE_PERCENT, '%'))
                i += 1
            elif input_string[i] == '!':
                tokens.append(Token(TokenType.DATA_TYPE_EXCLAMATION, '!'))
                i += 1
            elif input_string[i] == '$':
                tokens.append(Token(TokenType.DATA_TYPE_DOLLAR, '$'))
                i += 1
            elif input_string[i:i+4] == 'read':
                tokens.append(Token(TokenType.INPUT_OP_READLN, 'read'))
                i += 4
            elif input_string[i:i+6] == 'writeln':
                tokens.append(Token(TokenType.OUTPUT_OP_WRITELN, 'writeln'))
                i += 6
            elif input_string[i].isalpha():
                identifier = ''
                while i < len(input_string) and (input_string[i].isalpha() or input_string[i].isdigit()):
                    identifier += input_string[i]
                    i += 1
                tokens.append(Token(TokenType.IDENTIFIER, identifier))
            else:
                print(f"Error: Unexpected character '{input_string[i]}' at position {i}")
                return None

        return tokens

    # Пример парсера для анализа программы
    def parse_program(tokens):
        if len(tokens) < 7 or tokens[0].token_type != TokenType.PROGRAM_BEGIN or \
        tokens[1].token_type != TokenType.PROGRAM_VAR or tokens[2].token_type != TokenType.IDENTIFIER or \
        tokens[3].token_type != TokenType.COLON or tokens[4].token_type != TokenType.DATA_TYPE_PERCENT or \
        tokens[5].token_type != TokenType.SEMICOLON or tokens[-1].token_type != TokenType.PROGRAM_END:
            print("Error: Invalid program structure")
            return

        print("Program parsed successfully!")

# Пример использования лексического анализатора и парсера
    input_code = "program var x: %; begin end."
    tokens = tokenize_input(input_code)

    if tokens:
        parse_program(tokens)
