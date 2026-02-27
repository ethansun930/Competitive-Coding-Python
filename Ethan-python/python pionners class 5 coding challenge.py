print("welcome to the random number guessing place! ")
one_to_what_number = int(input("what do you want the range you are guessing in to be? (it will be one to the number you want) "))
import random
random_number = random.randint(1,one_to_what_number)
amount_of_guesses = 0
while True:
    guess = int(input("what is your guess?"))
    amount_of_guesses += 1
    if guess < random_number:
        print("too low")
    elif guess > random_number:
        print("too high")
    elif guess == random_number:
        print("correct!")
        break
print(f"it took you {amount_of_guesses} guesses to get the random number correctly!")
print("bye! please play again!")