print(r'''
        |
                                      --====|====--
                                            |  

                                        .-"""""-. 
                                      .'_________'. 
                                     /_/_|__|__|_\_\
                                    ;'-._       _.-';
               ,--------------------|    `-. .-'    |--------------------,
                ``""--..__    ___   ;       '       ;   ___    __..--""``
                 jgs      `"-// \\.._\             /_..// \\-"`
                             \\_//    '._       _.'    \\_//
                              `"`        ``---``        `"`
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

player = input("You are at a crossroad. Where do you want to go?\n Type left or right").strip().casefold()
if player == "right":
    print("Fall into a hole. Game Over!")
elif player == "left":
    print("You've come to a lake. There is an island in the middle of the lake\n ")
    player_progress = input("Type 'wait' to  wait for a boat. Type 'swim' to swim across").strip().casefold()
    if player_progress == "wait":
        print( "You arrive at the island unharmed.\n There is a house with 3 doors. One red, one yellow and one blue. which colour do you choose?")
        house = input("Type 'red' or 'yellow' or 'blue': ").strip().casefold()
        if house == "red":
            print("You are trapped! Game Over!")
        elif house == "yellow":
            print("You won!")
        else:
            print("You lost! Game Over!" )
    else:
        print("Fall into a hole. Game Over")
else:
    print(" Enter left or right")
