class SyntacticalAnalyzer:
    def __init__(self, lexeme_table, identifiersTable):
        self.identifiersTable = identifiersTable
        self.lex_get = self.lexeme_generator(lexeme_table)
        self.id_stack = []
        self.current_lex = next(self.lex_get)
        self.relation_operations = {"!=", "==", "<", "<=", ">", ">=", '='}
        self.term_operations = {"+", "-", "||"}
        self.factor_operations = {"*", "/", "&&"}
        self.keywords = {"||": 1, "&&": 2, "!": 3, "program": 4, "var": 5, "begin": 6, "end": 7, ":=": 8, "if": 9,
                         "then": 10, "else": 11, "for": 12, "to": 13, "step": 14, "while": 15, "readln": 16, "writeln": 17,
                         "true": 18, "false": 19, "next": 20, "step": 21}
        
    def equal_token_value(self, word):
        if self.current_lex.token_value != word:
            self.throw_error()
        self.current_lex = next(self.lex_get)

    def equal_token_name(self, word):
        if self.current_lex.token_name != word:
            self.throw_error()
        self.current_lex = next(self.lex_get)

    def throw_error(self):
        raise Exception(
            f"\nError in lexeme: '{self.current_lex.token_value}'")

    def lexeme_generator(self, lexeme_table):
        for i, token in enumerate(lexeme_table):
            yield token

    def PROGRAMM(self):  # <программа>::= program var <описание> begin <оператор> {; <оператор>} end
        self.equal_token_value("program")
        self.equal_token_value("var")
        self.DESCRIPTION()
        self.equal_token_value("begin")
        self.OPERATOR()

        while self.current_lex.token_value == ";":
            self.current_lex = next(self.lex_get)
            self.OPERATOR()

        if self.current_lex.token_value != "end":
            self.throw_error()


    def DESCRIPTION(self):  # <описание>::= {<идентификатор> {, <идентификатор> } : <тип> ;}
        while self.current_lex.token_value != "begin":
            self.IDENTIFIER(from_description=True)
            while self.current_lex.token_value == ",":
                self.current_lex = next(self.lex_get)
                self.IDENTIFIER(from_description=True)
            
            # Теперь ожидаем двоеточие и тип, но без точки с запятой
            self.equal_token_value(":")
            self.TYPE(from_description=True)
            
            # Ожидаем только если не следует begin
            if self.current_lex.token_value != "begin":
                self.equal_token_value(";")


    def IDENTIFIER(self, from_description=False):
        if from_description:
            if self.current_lex.token_name != "IDENT":
                self.throw_error()
            self.id_stack.append(self.current_lex.token_value)
            self.current_lex = next(self.lex_get)
        else:
            self.equal_token_name("IDENT")

    def TYPE(self, from_description=False):
        if from_description:
            if self.current_lex.token_name != "TYPE":
                self.throw_error()
            for item in self.id_stack:
                if item not in self.keywords:
                    self.identifiersTable.put(item, True, self.current_lex.token_value)
            self.id_stack = []
            self.current_lex = next(self.lex_get)
        else:
            self.equal_token_name("TYPE")

    def OPERATOR(
            self):
        if self.current_lex.token_value == "begin":
            self.COMPOSITE_OPERATOR()
        elif self.current_lex.token_value == "if":
            self.CONDITIONAL_OPERATOR()
        elif self.current_lex.token_value == "for":
            self.FIXED_CYCLE_OPERATOR()
        elif self.current_lex.token_value == "while":
            self.CONDITIONAL_CYCLE_OPERATOR()
        elif self.current_lex.token_value == "readln":
            self.INPUT_OPERATOR()
        elif self.current_lex.token_value == "writeln":
            self.OUTPUT_OPERATOR()
        else:
            self.ASSIGNMENT_OPERATOR()

    def COMPOSITE_OPERATOR(self):
        self.equal_token_value("begin")
        self.OPERATOR()

        while self.current_lex.token_value in {"\n", ";"}:
            self.current_lex = next(self.lex_get)
            self.OPERATOR()

        self.equal_token_value("end")

    def CONDITIONAL_OPERATOR(self):
        self.equal_token_value("if")
        if self.current_lex.token_value == "(":
            self.current_lex = next(self.lex_get)  # Пропускаем открывающую скобку
            self.EXPRESSION()
            if self.current_lex.token_value == ")":
                self.current_lex = next(self.lex_get)  # Пропускаем закрывающую скобку
            else:
                self.throw_error()
        else:
            self.throw_error()

        self.OPERATOR()

        if self.current_lex.token_value == "else":
            self.current_lex = next(self.lex_get)
            self.OPERATOR()




    def FIXED_CYCLE_OPERATOR(self):
        self.equal_token_value("for")
        self.ASSIGNMENT_OPERATOR()

        if self.current_lex.token_value == "to":
            self.current_lex = next(self.lex_get)
            end_expression = self.EXPRESSION()

            # Обработка необязательной части "step"
            step_expression = None
            if self.current_lex.token_value == "step":
                self.current_lex = next(self.lex_get)
                step_expression = self.EXPRESSION()

            self.OPERATOR()

            # Вставка логики для обработки "next"
            if self.current_lex.token_value == "next":
                self.current_lex = next(self.lex_get)
            else:
                self.throw_error()

            # Теперь вы можете использовать переменные end_expression и step_expression
            # для обработки логики цикла
        else:
            self.throw_error()


    def CONDITIONAL_CYCLE_OPERATOR(self):
        self.equal_token_value("while")
        self.equal_token_value("(")
        self.EXPRESSION()
        self.equal_token_value(")")
        self.OPERATOR()

    def INPUT_OPERATOR(self):
        self.equal_token_value("readln")
        self.IDENTIFIER()
        while self.current_lex.token_value == ",":
            self.current_lex = next(self.lex_get)
            self.IDENTIFIER()

    def OUTPUT_OPERATOR(self):
        self.equal_token_value("writeln")
        self.EXPRESSION()
        while self.current_lex.token_value == ",":
            self.current_lex = next(self.lex_get)
            self.EXPRESSION()

    def ASSIGNMENT_OPERATOR(self):
        self.IDENTIFIER()
        self.equal_token_value(":=")  # Используем ":=" вместо "="
        self.EXPRESSION()


    def EXPRESSION(self):
        self.OPERAND()
        while self.current_lex.token_value in self.relation_operations:
            self.current_lex = next(self.lex_get)
            self.OPERAND()

    def OPERAND(self):
        self.TERM()
        while self.current_lex.token_value in self.term_operations:
            self.current_lex = next(self.lex_get)
            self.TERM()

    def TERM(self):
        self.FACTOR()
        while self.current_lex.token_value in self.factor_operations:
            self.current_lex = next(self.lex_get)
            self.FACTOR()

    def FACTOR(self):
        if self.current_lex.token_name in {"IDENT", "NUM", "NUM2", "NUM8", "NUM10", "NUM16", "REAL"}:
            self.current_lex = next(self.lex_get)
        elif self.current_lex.token_value in {"true", "false"}:
            self.current_lex = next(self.lex_get)
        elif self.current_lex.token_value == "!":
            self.equal_token_value("!")
            self.FACTOR()
        elif self.current_lex.token_value == "(":
            self.current_lex = next(self.lex_get)
            self.EXPRESSION()
            self.equal_token_value(")")
        else:
            self.throw_error()
