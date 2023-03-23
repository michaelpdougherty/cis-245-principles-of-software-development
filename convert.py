#!/usr/bin/env python3
# CIS 245 - Principles of Software Development
# Program by Michael Dougherty and Maria Rodriguez
DIGITS = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


def repToDecimal(representation, base):
    value = 0
    i = len(representation) - 1
    for c in representation:
        value += DIGITS[c] * base ** i
        i -= 1
    return value


def test(representation, base, expected, n):
    actual = repToDecimal(representation, base)
    print("--------------")
    print(f"Test #{n}")
    print("--------------")
    print(f"convert {representation} to base {base}")
    print("actual:", actual)
    print("expected:", expected)
    print("passed:", actual == expected)


def main():
    # representation = input("Enter a representation: ")
    # base = int(input("Enter a base between 2 and 16: "))
    # print(f"The number '{representation}' is {repToDecimal(representation, base)} in base {base}.")
    test('10', 2, 2, 1)
    test('10', 10, 10, 2)
    test('A5', 16, 165, 3)
    test('120D70ADD151', 16, 19848934314321, 4)


if __name__ == "__main__":
    main()
