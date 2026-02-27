def is_palindrome1(n):
    for i in range(len(n)//2):
        if n[i] != n[len(n) - i - 1]:
           return False
    return True
def is_palindrome2(n):
    left = 0
    right = len(n) - 1
    while left < right:
        if n[left] != n[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome2("noon"))
print(is_palindrome2("cat"))