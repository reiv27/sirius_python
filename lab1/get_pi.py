from math import log
from fractions import Fraction
from decimal import Decimal


def get_pi(n: int):
    result = 0
    N = int(n * log(10, 16)) + 10
    
    for i in range(N):
        t = Fraction(1, 16**i) * (Fraction(4, 8 * i + 1) - Fraction(2, 8 * i + 4) -
                                  Fraction(1, 8 * i + 5) - Fraction(1, 8 * i + 6))
        result += t
    return str(Decimal(result.numerator)/Decimal(result.denominator))