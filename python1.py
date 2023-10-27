import sys

import sys


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def factorize_and_format(integer):
    factors = prime_factors(integer)
    factor_count = {}
    for factor in factors:
        if factor in factor_count:
            factor_count[factor] += 1
        else:
            factor_count[factor] = 1

    output = []
    for factor, exponent in factor_count.items():
        if exponent == 1:
            output.append(str(factor))
        else:
            output.append(f"{factor}^{exponent}")

    return '*'.join(output)


if len(sys.argv) < 2:
    print("Podaj co najmniej jedną liczbę jako argument.")
else:
    for arg in sys.argv[1:]:
        try:
            number = int(arg)
            if number < 1:
                print(f"Nieprawidłowa liczba: {number}")
            else:
                result = factorize_and_format(number)
                print(f"{number} = {result}")
        except ValueError:
            print(f"Podany argument nie jest liczba!: {arg}")
