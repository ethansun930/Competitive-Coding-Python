# this is a adventure game created by ethan. every name listed will get a different result: ethan, grace, cui and kai. everyone else will get the else statement.
brave_traveler_name = input("welcome to this magical world, what is your first name?")
brave_traveler_place = input("where do you choose to fight the planet's evil wizard: clouds, or forests?")
if brave_traveler_name == "ethan":
    if brave_traveler_place == "clouds": 
        print("you defeated the wizard and saved the planet!") 
        print("you won!")
    elif brave_traveler_place == "forests":
        print("the town looked at you and made a random asumption that you were to weak!")
        print("you lose")     
elif brave_traveler_name == "grace":
    if brave_traveler_place == "clouds":
        print("you fought with the wizard but you forgot your wand at your cavern and fainted to one of the wizard's spells!")
        print("you lost")
    elif brave_traveler_place == "forests":
        print("the wizard almost won but then got stuck in poison ivy!")
        print("you won!")
elif brave_traveler_name == "kai":
    if brave_traveler_place == "clouds":
        print("the town mistakened you for a theif named kai and so didn't allow you into clouds!")
        print("you lose!")
    elif brave_traveler_place == "forests":
        print("you tied with the wizard, but then you fought a second round!")
        print("you won!")
elif brave_traveler_name == "cui":
    if brave_traveler_place== "clouds":
        print("you and the wizard fought for three whole days! you almost gave up!")
        print("you won!")
    if brave_traveler_place == "forests":
        print("the wizard turned the forest into maze and so you got lost!")
        print("you lost!")
else:
    if brave_traveler_place == "clouds":
        print("the wizard made the clouds start moving and you fell down back in to the village!")
        print("you lost!")
    elif brave_traveler_place == "forests":
        print("the wizard forgot it's most powerful spell!")
        print("you won!")