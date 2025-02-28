# Conversion from Diophantine Equations to Deterministic Finite Automata

This project provides Python scripts that convert Diophantine equations (equations with integer solutions) to Deterministic Finite Automata (DFA). The implementation is based on the paper "Diophantine Equations, Presburger Arithmetic and Finite Automata" by Alexandre Boudet and Hubert Comon.

## Theoretical Background

Diophantine equations are polynomial equations for which only integer solutions are sought. These equations play an important role in number theory and computational theory. In this project, we convert Diophantine equations to Deterministic Finite Automata (DFA) to investigate the existence and properties of solutions to the equations.

The conversion idea is as follows:
- Construct a DFA that receives bit sequences corresponding to each variable in the equation as input
- The states of the DFA correspond to the evaluation values of the equation
- Input paths that ultimately reach the state 0 correspond to solutions of the original equation

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/diophantine-equation-to-automaton.git
cd diophantine-equation-to-automaton
```

2. Create and activate a virtual environment:
```
python -m venv myenv
source myenv/bin/activate  # For Linux
# or
myenv\Scripts\activate  # For Windows
```

3. Install the required packages:
```
pip install automata-lib networkx pygraphviz
```

Note: To install pygraphviz, Graphviz must be installed on your system.

## Usage

To run the script:

```
python diophantine_equation_to_automaton.py
```

When executed, you will be prompted to enter:
1. The number of variables
2. The coefficient for each variable
3. The constant term of the equation

After input, the program will:
- Display the entered equation
- Generate the corresponding DFA
- Save the DFA diagram as a PNG file
- Display a minimum-length word accepted by the DFA (one solution to the equation)

## Example

For example, if you input the equation `1*x_1 + 2*x_2 = 3`:

```
Enter the number of variables: 2
Enter 2 coefficients:
1
2
Enter a constant: 3
Your equation is: 1*x_1 + 2*x_2 = 3
```

The program will generate the corresponding DFA and save it as `1*x_1 + 2*x_2 = 3.png`. It will also display one solution to this equation.

## Dependencies

- [automata-lib](https://caleb531.github.io/automata/): A library for working with finite automata
- networkx: A library providing graph theory algorithms
- pygraphviz: A Python interface to Graphviz (used for DFA visualization)

## References

- Alexandre Boudet and Hubert Comon, "Diophantine Equations, Presburger Arithmetic and Finite Automata"
