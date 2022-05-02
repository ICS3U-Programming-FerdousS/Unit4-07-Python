#!/usr/bin/env python3
# Created by: Ferdous Sediqi
# Created on: May 2, 2022
# In this program we use FOR loop to display numbers from 1000-2000
# Also use if statment to display 5 numbers per line.


def main():
    # variables
    counter = 1000
    # using nested loops to display colors code
    for counter in range(1000, 2001):
        if counter % 5 == 0 and counter != 1000:
            print()
        print(counter, end=" ")


if __name__ == "__main__":
    main()
