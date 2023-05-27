#q1
#flow chart 
'''
                    +-------------------+
                    |      start()      |
                    +-------------------+
                            |
                   +--------v--------+
                   |  bear_room()    |
                   +--------|--------+
                            |
                   +--------v--------+
                   |  gold_room()    |
                   +--------|--------+
                            |
                   +--------v--------+
                   | cthulhu_room()  |
                   +--------|--------+
                            |
                   +--------v--------+
                   |      dead()      |
                   +-------------------+


                   If you choose the left door, you enter the bear room (bear_room()), where you have multiple choices to either take honey, taunt the bear, or open the door. Depending on your choices, you can either reach the gold room (gold_room()) or end up dead (dead()).

If you choose the right door, you encounter Cthulhu (cthulhu_room()). Here, you have the option to flee or eat your head. If you flee, you go back to the starting point (start()), and if you eat your head, you end up dead (dead()).
'''

#q2
from sys import exit

score = 0  # Global variable to track the player's score

def start():
    global score

    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input("> ")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

def bear_room():
    global score

    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    
    bear_moved = False
    
    while True:
        choice = input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
            score += 10
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def gold_room():
    global score

    print("This room is full of gold. How much do you take?")
    
    choice = input("> ")
    
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        score += 50
    else:
        dead("You greedy bastard!")

def cthulhu_room():
    global score

    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")
    
    if "flee" in choice:
        print("You managed to escape Cthulhu's grasp.")
        score += 20
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    global score

    print(why, "Good job!")
    print("Your score:", score)
    exit(0)

# Start the game
start()


#q3
def gold_room():
    print("This room is full of gold. How much do you take?")

    while True:
        choice = input("> ")
        
        try:
            how_much = int(choice)
        except ValueError:
            print("Man, learn to type a whole number.")
            continue
        
        if how_much < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
        else:
            print("You greedy bastard!")
            exit(0)
