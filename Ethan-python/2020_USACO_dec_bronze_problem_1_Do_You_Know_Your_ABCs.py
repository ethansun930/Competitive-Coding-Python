values = list(map(int, input().split()))
values.sort()
print(values[6] - values[5], end = " ")
print(values[6] - values[4], end = " ")
print(values[6] - values[0] - values[1], end = " ")
#a, b, c, a + b, a + c, b + c, a + b + c or a, b, a + b, c, a + c, b + c, a + b + c
