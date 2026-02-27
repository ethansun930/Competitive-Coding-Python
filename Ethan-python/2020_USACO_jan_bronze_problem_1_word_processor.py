x = list(map(int, input().split()))
N = x[0]
K = x[1]
used = 0
x = input().split()
curr = 1
for i in x:
    if curr == 1:
        print(i, end = "")
        curr = 0
        used = len(i)
    elif len(i) + used <= K:
        print(" ", end = "")
        print(i, end = "")
        used += len(i)
    else:
        print("")
        print(i, end = "")
        used = len(i)

    
    