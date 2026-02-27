def exponent(a, b):
    if b < 0:
        return exponent(a, b + 1)/a
    if b == 0:
        return 1
    if b > 0:
        return exponent(a, b - 1) * a