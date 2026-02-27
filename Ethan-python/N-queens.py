

# .Q..
# ...Q
# Q...
# ..Q.

# [1,3,0,2]

N = int(input("how many queens do you want? "))

def print_queens(position: list[int]):
    """
    convert position like [1,3,0,2]
    into board positions
    .Q..
    ...Q
    Q...
    ..Q.
    """
    queens = []
    for i in range(N):
        row = ["."] * N
        row[position[i]] = "Q"
        queens.append("".join(row))
    for row in queens:
        print(row)
    print("\n\n")
    
def check_position(row: int, col: int, position: list[int]):
    for i in range(row):
        if position[i] == col:
            return False
    for i in range(row):
        if abs(position[i] - col) == abs(row - i):
            return False
    return True
    
position = []
solution_count = 0
def find_queens(row: int):
    global solution_count
    if row == N:
        print_queens(position)
        solution_count += 1
        return True
    for col in range(N):
        if check_position(row, col, position) == True:
            position.append(col)
            find_queens(row + 1)
            position.pop()

find_queens(0)
print(f"there are {solution_count} solutions to having {N} queens")
        
        
        
    