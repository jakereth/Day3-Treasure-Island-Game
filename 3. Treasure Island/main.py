print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

one = input("You wake up one an island!\nYou see another smaller island in the distance as well.\nYou can either swim or explore your island!\n'swim' or 'explore'?")
one = one.lower()

if one == "swim" :
    print("You chose to swim for some reason???\nSurprise, surprise, you were eaten by a shark, Game Over!")

else: 
    two = input("You explored the island and found both a dungeon and a map with a trail to follow!\nWould you like to follow the map or enter the dungeon? 'Map' or 'Dungeon'")
    two = two.lower()

    if two == 'dungeon' :
        print("You went into the dungeon and discovered a booby trap!\nUnfortunately you are not Indiana Jones and were crushed by a boulder, Game Over!")
    
    else: 
        print("You followed the map like a smart person!\nUpon arriving at the destination you see three paths with signs!")
        print("The left path says horribly tragic certain death!")
        print("The straight path says extremely safe path, nothing to worry about, this leads to the treasure!")
        print("The right path says 'Follow this path for certain ...' it looks like they ran out of ink.")
        three = input("Which path do you choose? 'left' 'straight' 'right'")
        three = three.lower()

        if three == 'left' :
            print("Well I don't know why you picked the certain tragic death path!\nYou fell into a pit with spikes... and snakes... and fire... and an annoying guy monologuing while you die, Game Over!")
        elif three == 'right' :
            print("Bold move picking the mystery path, unfortunately it seems the rest of the sign was supposed to say 'certain death', Game Over!")
        else: 
            print("WOW you did it! You chose the correct path, I wonder why anybody wouldn't pick the sign that assures safety and treasure!")
            print("Anyways, you did it, you reach into the treasure chest filled with coins!!! YOU ARE RICH!!.... UH OH... \nUpon further inspection, those are chocolate coins, better luck next time!")
              