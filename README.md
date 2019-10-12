# roman_converter
A Python code to convert a Roman numeral to a number and vice versa.

---

Input on the command line: a positive integer or a Roman numeral. If the input is an integer, the output is its corresponding Roman numeral. If the input is a Roman numeral, the output is its corresponding decimal value. If the input is invalid, a ValueError is raised.

---

The function `Arabic_to_Roman(num)` converts an integer to a Roman numeral. The algorithm loops over the symbols ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I') and corresponding values (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1). In each step, the quotient and remainder of the integer with the value is calculated. The quotient determines if and how many times the corresponding symbol needs to be added to the output string. The remainder becomes the new integer in the next step.

---

The function `Roman_to_Arabic(numeral_string)` converts a Roman numeral to an integer. The algorithm works as follows:

1. Loop over the symbols ('I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M') and corresponding values (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000).
2. In each step, while the string ends with the symbol, slice it off and add the corresponding value to the output integer.
If the string is empty, the loop can be stopped.

The string is not a valid Roman numeral if
* at some step the Roman symbol isn't larger than the intermediate result;
* the loop ended and there are still characters in the string left.

In these cases a ValueError is raised.

---

#### Examples:

```
>>> ./roman_converter.py MDCLIX
1659
>>> ./roman_converter.py 1024
MXXIV
>>> ./roman_converter.py -2
ValueError: -2 is not a valid input
>>> ./roman_converter.py DACLIX
ValueError: DACLIX is not a valid input
>>> ./roman_converter.py IVI
ValueError: IVI is not a valid input
```
