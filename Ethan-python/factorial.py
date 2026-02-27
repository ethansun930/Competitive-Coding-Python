def factorial1(n):
    if n < 0:
        return "Not Defined"
    if n == 0:
        return 1
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans
def factorial2(n):
    if n < 0:
        return "Not Defined"
    if n == 0:
        return 1
    if n == 1:
        return 1
    for i in range(1, n + 1):
        return n * factorial2(n - 1)