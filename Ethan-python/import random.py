import random
for i in range(20):
    n=0
    for i in range(10):
       mynumber = random.randint(1,100)
    if mynumber <= 50:
        n += 1
print(n)