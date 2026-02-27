import sys

sys.stdin = open("teleport.in", "r")
sys.stdout = open("teleport.out", "w")

a, b, x, y = map(int, input().split())
ans = abs(a - x) + abs(b - y)
ans = min(ans, abs(a - b))
ans = min(ans, abs(a - y) + abs(b - x))
print(ans)