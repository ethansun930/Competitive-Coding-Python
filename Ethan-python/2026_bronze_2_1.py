def all_distinct(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] == a[j]:
                return False
    return True
T = int(input())
answers = []
for i in range(T):
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    while all_distinct(a) == False:
        for i in range(len(a) - 1):
            if a[i] == a[i + 1]:
                a[i + 1] += K
                a.sort()
                ans += 1
    answers.append(ans)
for ans in answers:
    print(ans)
        