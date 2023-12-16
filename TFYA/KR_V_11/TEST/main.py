# main.py
from LexicalAnalizer import LexicalAnalyzer
from SyntacticalAnalyzer import SyntacticalAnalyzer
from SemanticalAnalyzer import IdentifiersTable

def analyze_program(path_to_program, print_info=True):
    identifiers_table = IdentifiersTable()
    lexer = LexicalAnalyzer(path_to_program, identifiers_table)
    lexer.analysis()

    if lexer.current.state != lexer.states.ERR:
        if print_info:
            print("Result of Lexical Analyzer:")
            for i in lexer.lexeme_table:
                print(f"{i.token_name} {i.token_value}")

        syntax_analyzer = SyntacticalAnalyzer(lexer.lexeme_table, identifiers_table)
        syntax_analyzer.PROGRAMM()
        identifiers_table.check_if_all_described()  # проверка что все Id описаны

        if print_info:
            print(identifiers_table)

        print("+---------+")
        print("| SUCCESS |")
        print("+---------+")

if __name__ == "__main__":
    PRINT_INFO = True
    PATH_TO_PROGRAM = "fourth_program.poullang"
    analyze_program(PATH_TO_PROGRAM, PRINT_INFO)
