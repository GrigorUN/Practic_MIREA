from TFYA.KR_V_11.FINALS.Lexer import LexicalAnalyzer, Tokens, Token

def main():
    filename = "d.dnm"  # Замените на имя вашего входного файла
    identifiersTable = set()  # Ваша таблица идентификаторов

    lexical_analyzer = LexicalAnalyzer(filename, identifiersTable)

    try:
        lexical_analyzer.analysis()
        print("Лексемы:")
        for token in lexical_analyzer.lexeme_table:
            print(token)

        print("\nТаблица идентификаторов:")
        for identifier in identifiersTable:
            print(identifier)

    except Exception as e:
        print(f"Ошибка: {e} в файле {lexical_analyzer.error.filename}, "
              f"строка: {lexical_analyzer.current.line_number}, позиция: {lexical_analyzer.current.pos_number}")

if __name__ == "__main__":
    main()
