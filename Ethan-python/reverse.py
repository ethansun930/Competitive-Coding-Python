def reverse(n):
    for i in range(len(n) - 1, -1, -1):
        print(n[i], end = "")
reverse(input())
