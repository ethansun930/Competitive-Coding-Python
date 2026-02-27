from math import sqrt
sum = 0

for i in range(1, 300):
    s = 212 + i * (i + 1)
    x = int(sqrt(s))
    if x * x == s:
        print(i)
        sum += i
print(sum)
        

    