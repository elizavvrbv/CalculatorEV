from RationalOperations import main_terminal as rational_terminal
from ComplexOperations import main_terminal as complex_terminal
from CalculatorType import type


def main():
    t = type()
    if t == 1:
        complex_terminal()
    elif t == 2:
        rational_terminal()
    print("Пока!")


if __name__ == '__main__':
    main()
