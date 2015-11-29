###############################################################################
#
#  TEXT ADVENTURE
#
# (c) Ryhmä 2: Tuomas Huttunen, Ville Pukki and Aki Sipovaara, 2015
#
###############################################################################

import Gamelogic
# import mysql.connector
import getpass
import textwrap

#
# Creating connection to database.
#
host = input("Server: ")
user = input("User: ")
password = getpass.getpass("Password: ")
db = Gamelogic.open_database(host, user, password)


#
# Mainloop
#
# - printing area description
# - printing possible directions of movement
# - printing items in the area
# - printing special events
# - game ending done by special event 6 with multiple choice ending.
# - reading and parsing user commands
# - executing command
#

#
# Creating a textwrap as an alternative print function.
# It will automatically start a new line if the last word goes over 80 characters.
#
def wrap(text):
    print(textwrap.fill(text, 80))


# Possible ASCII here if can be arsed.
# Start message
wrap("Starting text etc.. here(won't be in the loop, hence shown only once at the start of the game)")

ending = 0
while ending == 0:

    # Get location and print area description
    location = Gamelogic.location(db)
    description = Gamelogic.description(db, location)
    print("\n", description)

    # Printing possible directions of movement
    direction = Gamelogic.direction(db, location)
    if len(direction) > 0:
        print("Possible directions of movement:", direction)

    # Print items in the area
    items = Gamelogic.items(db, location)
    if len(items) > 0:
        print("Items in the area:, items")

    # Special event 1: Making and drinking the potion
    if location == 4:
        if "Suspicious Herbs" in Gamelogic.cmd_inventory(db):
            print("Do you want to trade the herbs for the potion?(y/n)")
            while True:
                answer = input()
                answer = answer.lower()
                if answer == 'y' or 'n' or 'no' or 'yes':
                    break
                print("Please input y or n.")
            if answer in ['y', 'yes']:
                Gamelogic.create(db)
                print("Suspicious Herbs removed from inventory.\nPotion of Endless Memory added to inventory.")
            else:
                print("")
        if "Potion of Endless Memory" in Gamelogic.cmd_inventory(db):
            print("Do you want to drink the Potion of Endless Memory?(y/n)")
            while True:
                answer = input()
                answer = answer.lower()
                if answer == 'y' or 'n' or 'no' or 'yes':
                    break
                print("Please input y or n.")
            if answer in ['y', 'yes']:
                Gamelogic.drink(db)
                print("Potion of Endless Memory removed from inventory.")
            else:
                print("")
        if "Potion of Transformation" in Gamelogic.cmd_inventory(db):
            print("Do you want to drink the Potion of Transformation?(y/n)")
            while True:
                answer = input()
                answer = answer.lower()
                if answer == 'y' or 'n' or 'no' or 'yes':
                    break
                print("Please input y or n.")
            if answer in ['y', 'yes']:
                print("Potion of Transformation removed from inventory.")
                wrap(
                    "You start feeling ill and pass out. You wake up with feeling teRIBBITle. "
                    "You have no idea what is going on. RIBBIT!  And then you realise, you've turned "
                    "into a frog. RIBBIT!")
                ending = 1
            else:
                print("")
        if "Potion of Transformation" and "Potion of Endless Memory" in Gamelogic.cmd_inventory(db):
            print("Do you want to drink the Potion of Endless memory(a) or Potion of Transformation(b)?(a/b/neither)")
            while True:
                answer = input()
                answer = answer.lower()
                if answer == 'a' or 'b' or 'neither' or 'none' or 'n' or 'no':
                    break
                print("Please input a, b or neither.")
            if answer == 'a':
                Gamelogic.drink(db)
                print("Potion of Endless Memory removed from inventory.")
            elif answer == 'b':
                print("Potion of Transformation removed from inventory.")
                wrap(
                    "You start feeling ill and pass out. You wake up with feeling teRIBBITle. "
                    "You have no idea what is going on. RIBBIT! And then you realise,"
                    "you've turned into a frog. RIBBIT!")
                ending = 1
            else:
                print("")
        if Gamelogic.potion_taken(db) == 0:
            if Gamelogic.shaman_met(db) == 0:
                wrap(
                    "The shaman senses you are not whole.  He wants you to bring him a pile of Suspicious Herbs. "
                    "They should restore your memory when brewed into a potion.")
            else:
                print("You should find the herbs to make the potion and restore your memories at the hill")
    # Special event 2: Filling the water bottle
    if location == 7 and "Water" not in Gamelogic.cmd_inventory(db):
        print("Do you want to fill your water bottle?(y/n)")
        answer = input()
        answer = answer.lower()
        if answer in ['y', 'yes']:
            Gamelogic.fill(db)
        else:
            print("")
    # Special event 3: Fixing the boat
    if location == 7 and Gamelogic.boat_fixed == 0:
        wrap(
            "You require a boat to cross the river, but the on left on the shore has a hole in it."
            "Maybe someone in the tavern will have something to fix it.")

    # Special event 4: Trading for the wooden tap
    if location == 3:
        if "Banana" in Gamelogic.cmd_inventory(db):
            print("Do you want to trade the banana for a wooden tap?(y/n)")
            while True:
                answer = input()
                answer = answer.lower()
                if answer == 'y' or 'n' or 'no' or 'yes':
                    break
                print("Please input y or n.")
            if answer in ['y', 'yes']:
                Gamelogic.trade(db)
                print("Banana removed from inventory.\n1 Wooden Tap added to inventory.")
            else:
                print("")
        else:
            print("There is a sign that says wooden taps for sale: Price 1 banana.")
            if Gamelogic.hill_visited == 0:
                print("")
            else:
                print("There was a banana tree a the hills.")

    # Special event 5: Entering the castle
    if location == 8 and Gamelogic.castle_entered == 0:
        print("There is a weird looking slot in the door.")
        if "The Sword of All Things Right" in Gamelogic.cmd_inventory(db):
            print("Your sword looks like it might fit but strangely it doesn't.")
        elif "The Sword of All Things Left" in Gamelogic.cmd_inventory(db):
            print("Your sword seems to fit, do you want to insert it to the slot?(y/n)")
            while True:
                answer = input()
                answer = answer.lower()
                if answer == 'y' or 'n' or 'no' or 'yes':
                    break
                print("Please input y or n.")
            if answer in ['y', 'yes']:
                Gamelogic.open_direction(db, 8, 10, "south")
                Gamelogic.open_direction(db, 10, 8, "north")
                print("")
            else:
                print("")
        else:
            wrap("There must be something that fits into it.\nIt looks like a"
                 "weird looking sword, but you have nothing like it with you.")

    # Special event 6: Game ending and creation of the Potion of Transformation
    if location == 10:
        if "Potion of Transformation" in Gamelogic.cmd_inventory(db):
            print("Do you want to pour the potion into the wizards wine bottle?(y/n)")
            while True:
                answer = input()
                answer = answer.lower()
                if answer == 'y' or 'n' or 'no' or 'yes':
                    break
                print("Please input y or n.")
            if answer in ['y', 'yes']:
                print("You pour the potion into the wine bottle. A puff a green smoke erupts from the bottle.")
                print("You hear footsteps in the distance. Do you want to hide?(y/n)")
                while True:
                    answer1 = input()
                    answer1 = answer.lower()
                    if answer1 == 'y' or 'n' or 'no' or 'yes':
                        break
                    print("Please input y or n.")
                if answer1 in ['y', 'yes']:
                    wrap("The wizard walks into the room, pours a drink and drinks it."
                         " A while passes and the wizard seems to feel ill.")
                    wrap("He doesn't know what is wrong and is helplessly trying to find answers in his spell book."
                         "But it is simply too late and he is suddenly transformed into a frog.")
                    ending = 1
                else:
                    wrap("The wizard walks into the room instantly spotting you. After a short consideration"
                         "he blasts you with some kind of weird arcane energy and you transform into solid rock. "
                         "Seems like the wizard has a new statue. After a smug smile he pours a drink and drinks it. "
                         "A while passes and the wizard seems to feel ill."
                         "He doesn't know what is wrong and is helplessly trying to find answers in his spell "
                         "book. But it is simply too late and he is suddenly transformed into a frog.")
                    ending = 1

            else:
                print("You hear footsteps in the distance. Do you want to hide?(y/n)")
                while True:
                    answer1 = input()
                    answer1 = answer.lower()
                    if answer1 == 'y' or 'n' or 'no' or 'yes':
                        break
                    print("Please input y or n.")
                if answer1 in ['y', 'yes']:
                    wrap("The wizard walks in and after a short while drinks his wine and goes to bed."
                         "You hide the whole night and once the wizard leaves you slowly sneak out of the castle"
                         "and go into hiding hoping the wizard doesn't find you.")
                    ending = 1
                else:
                    wrap(
                        "The wizard walks into the room instantly spotting you. After a short consideration he blasts"
                        "you with some kind of weird arcane energy and you transform into solid rock. "
                        "Seems like the wizard has a new statue.")
                    ending = 1

        else:
            if Gamelogic.castle_entered == 1:
                print(
                    "After walking a while in the castle you find a room with a spell book."
                    " Seems like the wizard has carelessly left it open.")
                print("Read the book?(y/n)")
                while True:
                    answer = input()
                    answer = answer.lower()
                    if answer == 'y' or 'n' or 'no' or 'yes':
                        break
                    print("Please input y or n.")
                if answer in ['y', 'yes']:
                    print(
                        "\nPotion of Transformation:\n\n1 Magic Mushroom\n1 litre of water\nAlchemist Table\nAdd"
                        "water into the mixer\nLight a fire under the mixer\nAdd blue powder\nWait till"
                        " water turns clear\nSlice and add the mushroom\nWait 1 minute\nPour "
                        "the mixture into a bottle\n\nHmm.. Seems like everything but "
                        "the mushroom and water is here.\nWonder if this would work.")
                else:
                    print("")
            elif "Magic_Mushroom" and "Water" in Gamelogic.cmd_inventory(db):
                print("Do you want to make the Potion of Transformation?(y/n)")
                while True:
                    answer = input()
                    answer = answer.lower()
                    if answer == 'y' or 'n' or 'no' or 'yes':
                        break
                    print("Please input y or n.")
                if answer in ['y', 'yes']:
                    Gamelogic.create_potion(db)
                    wrap(
                        "Magic Mushroom removed from inventory\nWater removed from inventory\n"
                        "Potion of Transformation added to inventory")
                else:
                    print("")

            else:
                print("Need to find the Magic Mushroom and water to create the potion.")
    # Input and parsing
    print("")
    cmd = input("> ").lower()
    if cmd == "":
        continue
    cmd_list = cmd.split()
    if len(cmd_list) == 1:
        verb = cmd_list[0]
        object = ""
    elif len(cmd_list) == 2:
        verb = cmd_list[0]
        object = cmd_list[1]
    else:
        print("Please input one or two words only.")

    # Command: move
    if verb == "move":
        if object == "north" or verb == "east" or verb == "south" or verb == "west":
            if Gamelogic.cmd_move(db, location, object) == 0:
                print("Can't go that way.")

    # Command: Pick up
    elif verb == "pick":
        if object == "":
            print("No item selected.")
        else:
            object_location = Gamelogic.object_location(db, object)
            if object_location is None or object_location != location:
                print(object, "not found.")
            else:
                Gamelogic.cmd_pick(db, object)
                print(object, "picked up.")

    # Command: inspect
    elif verb == "inspect":
        if object == "":
            print("No item selected.")
        elif Gamelogic.inspect(db, object) == 0:
            print("No such item.")
        else:
            Gamelogic.inspect(db, object)
    # Command: rotate
    elif verb == "rotate":
        if object == "sword":
            Gamelogic.rotate(db)
            print("Sword of All Things Right removed from inventory.")
            print("Sword of All Things Left added to inventory")
        else:
            print("Can't be rotated.")

    # Command: drop
    elif verb == "drop":
        if object == "":
            print("No item selected.")
        elif Gamelogic.cmd_drop(db, object, location) == 0:
            print(object, "can't be dropped.")
        else:
            print(object, "dropped.")
    # Command: help
    elif verb == "help":
        print("Commands:\nMove () North, South, East, West\n"
              "Drop (item) Drops a specific item\nPick (item) Picks up an item\nInspect (item) Inspects an item\n"
              "Rotate (item)\nEnd (ends the game)")

    # Command: end
    elif verb == "end":
        while True:
            answer = input("Are you sure you want to quit?(y/n)")
            answer = answer.lower()
            if answer == 'y' or 'n' or 'no' or 'yes':
                break
            print("Please input y or n.")
        if answer in ['y', 'yes']:
            while True:
                answer = input("Do you want to save the game?(y/n)")
                answer = answer.lower()
                if answer == 'y' or 'n' or 'no' or 'yes':
                    break
                print("Please input y or n.")
            if answer in ['y', 'yes']:
                db.commit()
            ending = 1
        else:
            print("")
    # Unknown command.
    else:
        print("Invalid command...")

print("The game has ended. Thank you for playing!")
