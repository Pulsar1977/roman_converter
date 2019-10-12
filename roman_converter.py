#!/usr/bin/env python3
import sys

"""
    A Python code to convert a Roman numeral to a number and vice versa.
"""

def main():
    input_string = sys.argv[1]
    if input_string.isdecimal():
        print(Arabic_to_Roman(int(input_string)))
    else:
        print(Roman_to_Arabic(input_string))


def Roman_to_Arabic(numeral_string):
    """
        Input: string containing Roman symbols
        Ouput: numeric decimal value, or ValueError if the string is invalid

        Sum all the values that appear in the string, from right to left.
        Slice the symbols off from the end of the string,
        and add the corresponding values to the result.
        If the string is empty, the loop can be stopped.

        The string is not a valid Roman numeral if
          a) at some step the Roman symbol isn't larger than the intermediary result;
          b) the loop ended and there are still characters in the string left.
    """
    symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    result = 0
    for symb, val in zip(symbols, values):
        if result >= val:
            raise ValueError(f'{numeral_string} is not a valid input')
        elif numeral_string == '':
            break
        while numeral_string.endswith(symb):
            numeral_string, _, _ = numeral_string.rpartition(symb)
            result += val
    else:
        if numeral_string != '':
            raise ValueError(f'{numeral_string} is not a valid input')
    return result


def Arabic_to_Roman(num):
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    n = num

    numeral_string = ''
    for symb, val in zip(symbols, values):
        k, n = divmod(n, val)
        numeral_string += symb*k
    return numeral_string


if __name__ == "__main__":
    main()
