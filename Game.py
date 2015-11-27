###############################################################################
#
#  TEXT ADVENTURE
#
# (c) Ryhmä 2: Tuomas Huttunen, Ville Pukki and Aki Sipovaara, 2015
#
###############################################################################

import Gamelogic
import mysql.connector
import getpass

#
# Creating connection to database.
#
host = input("Server: ")
user = input("User: ")
password = getpass.getpass("Password: ")
db = Gamelogic.open_database(host, user, password)

#
#Mainloop
#
# - printing area description
# - printing possible directions of movement
# - printing items in the area
# - printing special events
# - reading and parsing user commands
# - executing command
#

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
    if location == (tähän tulee shamaanin paikka ID) and Gamelogic.potion_taken(db) == 0:
        if Gamelogic.shaman_met(db) == 0:
            print("The shaman senses you are not whole.\nHe wants you to bring him a pile of Suspicious Herbs.\nThey should restore your memory when brewed into a potion.")
        else:
            print("You should find the herbs to make the potion and restore your memories at the hill")
    # Special event 2: Filling the water bottle
    if location == (joki id) and "Water" not in Gamelogic.cmd_inventory:
        print("Do you want to fill your water bottle?(y/n)")
        answer = input()
        if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
            Gamelogic.fill(db, object)
        else:
            print("")
    # Special event 3: Fixing the boat
    if location == (joki id) and Gamelogic.boat_fixed == 0:
        print("You require a boat to cross the river, but the on left on the shore has a hole in it.\nMaybe someone in the marketplace will have something to fix it.")

    # Special event 4: Trading for the wooden tap
    if location == (tavern ic) and if "Wooden tap" in Gamelogic.inventory:
        print("There is a sign that says wooden taps for sale: Price 1 banana.")
        if Gamelogic.hill_visited == 0:
            print("")
        else:
            print("There was a banana tree a the hills.")

    # Special event 5: Entering the castle
    if location == (castle id) and Gamelogic.castle_entered == 0:
        print("There is a weird looking slot in the door.")
        if "The Sword of All Things Right" in Gamelogic.cmd_inventory:
            print("Your sword looks like it might fit but strangely it doesn't.")
        elif "The Sword of All Things Left" in Gamelogic.cmd_inventory:
            print("Your sword seems to fit, do you want to insert it to the slot?")
        else:
            print("There must be something that fits into it.\nIt looks like a weird looking sword, but you have nothing like it with you.")

    # Special event 6: Game ending and creation of the Potion of Transformation
    if Gamelogic.castle_entered != 0:
        if "Potion of Transformation" in Gamelogic.cmd_inventory:
            print("Do you want to pour the potion into the wizards wine bottle?(y/n)")
            answer = input()
            answer = answer.lower()
            if answer in ['y', 'yes']:
                print("You pour the potion into the wine bottle. A puff a green smoke erupts from the bottle.")
                print("You hear footsteps in the distance. Do you want to hide?(y/n)")
                answer1 = input()
                answer = answer.lower()
                if answer1 in ['y', 'yes']:
                    print("The wizard walks into the room, pours a drink and drinks it.\nA while passes and the wizard seems to feel ill.")
                    print("He doesn't know what is wrong and is helplessly trying\nto find answers in his spell book.\nBut it is simply too late and he is suddenly transformed into a frog.")
                    ending = 1
                elif answer1 in ['n', 'no']:
                    print("The wizard walks into the room instantly spotting you.\nAfter a short consideration he blasts you with some kind of weird arcane energy\nand you transform into solid rock.\nSeems like the wizard has a new statue.\nAfter a smug smile he pours a drink and drinks it.\nA while passes and the wizard seems to feel ill.")
                    print("He doesn't know what is wrong and is helplessly trying\nto find answers in his spell book.\nBut it is simply too late and he is suddenly transformed into a frog.")
                    ending = 1
                else:
                    print("Please input y or n.")
            elif answer in ['n', 'no']:
                print("You hear footsteps in the distance. Do you want to hide?(y/n)")
                answer1 = input()
                answer = answer.lower()
                if answer1 in ['y', 'yes']:
                    print("The wizard walks in and after a short while drinks his wine and goes to bed.\nYou hide the whole night and once the wizard leaves\nyou slowly sneak out of the castle and go into hiding hoping the wizard doesn't find you.")
                    ending = 1
                elif answer1 in ['n', 'no']:
                    print("The wizard walks into the room instantly spotting you.\nAfter a short consideration he blasts you with some kind of weird arcane energy\nand you transform into solid rock.\nSeems like the wizard has a new statue.")
                    ending = 1
                else:
                    print("Please input y or n.")
            else:
                print("Please input y or n.")
        else:
            if Gamelogic.castle_entered == 1:
                print("After walking a while in the castle you find a room with a spell book\nSeems like the wizard has carelessly left it open.")
                answer = input("Read the book?(y)")
                answer = answer.lower()
                if answer in ['y', 'yes']:
                    print("\nPotion of Transformation:\n\n1 Magic Mushroom\n1 litre of water\nAlchemist Table\nAdd water into the mixer\nLight a fire under the mixer\nAdd blue powder\nWait till water turns clear\nSlice and add the mushroom\nWait 1 minute\nPour the mixture into a bottle\n\nHmm.. Seems like everything but the mushroom and water is here.\nWonder if this would work.")
            elif "Magic_Mushroom" and "Water" in Gamelogic.cmd_inventory:
                answer = input("Do you want to make the Potion of Transformation?(y/n)")
                answer = answer.lower()
                if answer in ['y', 'yes']:
                    Gamelogic.merge(??)
                    print("Magic Mushroom removed from inventory\nWater removed from inventory\nPotion of Transformation added to inventory")
                elif answer in ['n', 'no']:
                    print("")
                else:
                    print("Please input y or n.")
            else:
                print("Need to find the Magic Mushroom and water to create the potion.")
    # Input and parsing
    print("")
    cmd = input("> ")
    if cmd == "":
        continue
    cmdlist = cmd.split()
    if len(cmdlist) == 1:
        verb = cmdlist[0]
        object = ""
    elif len(cmdlist) == 2:
        verb = cmdlist[0]
        object = cmdlist[1]
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
        elif statement:
            if Gamelogic.inspect(db, object, location) == 0:
                print("No item selected.")
        else:
            print()
    # Command: drop
    elif verb == "drop"
        if object == "":
            print("No item selected.")
        elif Gamelogic.cmd_drop(db, object, location) == 0:
            print(object, "can't be dropped.")
        else:
            print(object, "dropped.")

    # Command: end
    elif verb == "end":
        ending = 1

    # Unknown command.
    else:
        print("Invalid command...")

print("The game has ended. Thank you for playing!")
