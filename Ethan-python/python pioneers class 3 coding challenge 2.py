fruit_basket = []
print("welcome to the fruit basket organizer!")
print("the basket can hold up to 5 fruits.")
for i in range(5):
    fruit = input("enter a fruit to the basket or type stop to finish. ")
    if fruit == "stop" or fruit == "Stop":
        break
    fruit_basket.append(fruit)
    print("your current basket is:",fruit_basket)
    if i == 4:
        print("the basket is full!")
fruit = ""
print("your final fruit basket contains:" )
for fruits in fruit_basket:
    print(fruits)
while True:
    fruit = input("enter a item that you want to search for in your basket. ")
    basket = "no"
    for fruits in fruit_basket:
        if fruits == fruit:
            basket = "yes"
    if basket == "yes" and fruit_basket.count(fruit)>1 :
        print(fruit, "is in your basket and you have", fruit_basket.count(fruit), fruit + "s in the basket")
    elif basket == "yes" and fruit_basket.count(fruit)==1 :
        print(fruit, "is in your basket and there is 1", fruit, "in your basket")
    elif basket == "no":
        print(fruit, "is not in your basket.")
    search = input("keep searching? ")
    if search == "no" or search == "No":
        break   
    if not (search == "yes" or search == "Yes"):
        print("i don't understand you!")
        break
print("bye! please come again!")