# This file implements the conversion from a diophantine equation to a deterministic finite automaton.
# This implementation is based on the paper "Diophantine Equations, Presburger Arithmetic and Finite Automata" by Alexandre Boudet and Hubert Comon.
from typing import Set, List
from automata.fa.dfa import DFA


def generate_binary_strings(n: int) -> Set[str]:
    binary_strings = {format(i, f"0{n}b") for i in range(2**n)}
    return binary_strings


def diophantine_equation_to_automaton(
    n: int, coefficients: List[int], constant: int
) -> DFA:
    sink_state = "\u22A5"
    states = {constant, sink_state}  # Initialize the set of states
    input_symbols = generate_binary_strings(n)  # Generate the set of input symbols
    transitions = {}  # Initialize the set of transitions
    initial_state = constant  # Initialize the initial state
    final_states = set()
    set_for_loop = {constant}  # Initialize the set for while loop with the constant
    while set_for_loop:
        k = set_for_loop.pop()  # Pop an element from the set
        if k == 0:
            final_states.add(k)
        transitions[k] = {}  # Initialize the set of transitions for the current state
        for input_symbol in input_symbols:
            sum = 0  # Initialize sum for each input_symbol
            for i, char in enumerate(input_symbol):
                sum += int(char) * coefficients[i]  # Multiply and add to sum
            if (k - sum) % 2 == 0:
                if (k - sum) // 2 not in states:
                    set_for_loop.add((k - sum) // 2)
                    states.add((k - sum) // 2)
                transitions[k][input_symbol] = (k - sum) // 2
            else:
                transitions[k][input_symbol] = sink_state
    transitions[sink_state] = {
        input_symbol: sink_state for input_symbol in input_symbols
    }
    return DFA(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states,
    )


def main():
    # Receive the number of variables
    n = int(input("Enter the number of variables: "))

    # Receive n coefficients and store them in a list
    coefficients = []
    print(f"Enter {n} coefficients:")
    for _ in range(n):
        coefficients.append(int(input()))

    # Receive the constatnt
    constant = int(input("Enter a constant: "))

    # Generate and print the equation in the form of a_1*x_1 + a_2*x_2 + ... + a_n*x_n = constant
    equation = (
        " + ".join([f"{coeff}*x_{i+1}" for i, coeff in enumerate(coefficients)])
        + f" = {constant}"
    )
    print("Your equation is:", equation)
    automaton = diophantine_equation_to_automaton(n, coefficients, constant)
    automaton.show_diagram(path=equation + ".png")
    print(automaton.random_word(automaton.minimum_word_length()))


if __name__ == "__main__":
    main()
