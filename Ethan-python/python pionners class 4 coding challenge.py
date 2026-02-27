while True:
    animal = input("what animal do you want? ")
    if animal == "dog" or animal == "Dog":
        print("a dog goes woof")
    elif animal == "cat" or animal == "Cat":
        print("a cat goes meow")
    elif animal == "bird" or animal == "Bird":
        print("a bird goes caw")
    elif animal == "lion" or animal == "Lion" or animal == "tiger" or animal =="Tiger":
        print("a", animal, "goes rarrr")
    elif animal == "chicken" or animal == "Chicken":
        print("a chicken goes bak")
    elif animal == "cow" or animal == "Cow":
        print("a cow goes moo")
    else:
        print("a", animal, "goes... I don't know what it makes.")
    exit = input("exit?")
    if exit == "yes" or exit == "Yes":
       print("come again soon!")
       break