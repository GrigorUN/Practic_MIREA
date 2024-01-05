def powerset(s):
    if len(s) == 0:
        return [[]]
    subsets = powerset(s[:-1])
    return subsets + [item + [s[-1]] for item in subsets]

def convert_nfa_to_dfa(states, alphabet, transitions, initial_states, final_states):
    dfa_states = []
    dfa_transitions = {}
    dfa_initial_state = ''
    dfa_final_states = []

    # Create the initial state for the DFA
    dfa_initial_state = 'D(' + ', '.join(initial_states) + ')'
    dfa_states.append(dfa_initial_state)

    powerset_states = powerset(states)

    for subset in powerset_states:
        subset_name = 'D(' + ', '.join(subset) + ')'
        dfa_states.append(subset_name)

        for symbol in alphabet:
            next_state = set()
            for state in subset:
                for transition in transitions:
                    if transition[0] == state and transition[1] == symbol:
                        next_state.add(transition[2])
            if next_state:
                next_state_name = 'D(' + ', '.join(sorted(next_state)) + ')'
                dfa_transitions[(subset_name, symbol)] = next_state_name

                if next_state_name not in dfa_states:
                    dfa_states.append(next_state_name)

    for subset in powerset_states:
        for final_state in final_states:
            if final_state in subset:
                dfa_final_states.append('D(' + ', '.join(subset) + ')')
                break

    return dfa_states, alphabet, dfa_transitions, dfa_initial_state, dfa_final_states

# Ввод данных через консоль
states = input("Введите множество состояний (разделяйте пробелами): ").split()
alphabet = input("Введите алфавит ввода (разделяйте пробелами): ").split()
transitions_input = input("Введите функцию переходов (текущее состояние, входной символ, следующее состояние): ").split()
transitions = [tuple(transitions_input[i:i+3]) for i in range(0, len(transitions_input), 3)]
initial_states = input("Введите множество начальных состояний (разделяйте пробелами): ").split()
final_states = input("Введите множество конечных состояний (разделяйте пробелами): ").split()

# Вызов функции для преобразования
dfa_states, dfa_alphabet, dfa_transitions, dfa_initial_state, dfa_final_states = convert_nfa_to_dfa(
    states, alphabet, transitions, initial_states, final_states)

# Вывод результата
print("\nDFA:")
print("Множество состояний:", ', '.join(dfa_states))
print("Алфавит ввода:", ', '.join(dfa_alphabet))
print("Функция переходов:")
for key, value in dfa_transitions.items():
    print(key[0], "=", key[1], "=", value)
print("Начальные состояния:", dfa_initial_state)
print("Конечные состояния:", ', '.join(dfa_final_states))
