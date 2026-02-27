def is_palindrome_or_one_letter_away(a):
    count = 0
    for i in range(len(a)//2):
        if a[i] != a[len(a) - i - 1]:
            count += 1
        if count == 2:
            return False
    return True
