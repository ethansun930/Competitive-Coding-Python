def find_row_of_pascals_triangle(n):
    if n == 0:
        return [1]
    ans = [""] * (n + 1)
    previous_row = find_row_of_pascals_triangle(n - 1)
    for i in range(n + 1):
        if i == 0 or i == (n):
            ans[i] = 1
        else:
            ans[i] = previous_row[i - 1] + previous_row[i]
    return ans
def find_number_in_pascals_triangle(row, index):
    return (find_row_of_pascals_triangle(row)[index - 1])
def find_n_rows_of_pascals_triangle(n):
    ans = [""] * n
    for i in range(n):
        ans[i] = find_row_of_pascals_triangle(i)
    return ans
def choose(a, b):
    return (find_row_of_pascals_triangle(a)[b])
print(choose(5, 2))