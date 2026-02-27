list = [""]*10000
def fibonacci1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if list[n] != "":
        return list[n]
    list[n] = fibonacci1(n - 1) + fibonacci1(n - 2)
    return list[n]
def fibonacci2(n):
    import math
    phi = (1 + math.sqrt(5))/2
    return int(((phi**n - (1 - phi)**n)/math.sqrt(5)))
print(fibonacci1(6))