print("welcome to the list generator!")
starting_value = int(input("what do you want your starting value to be?"))
ending_value = int(input("what do you want your ending value to be?"))
increment_amount = int(input("what do you want your increment to be?"))
print("here is your list.")
for i in range(starting_value, ending_value, increment_amount):
    print(i)