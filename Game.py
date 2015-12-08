###############################################################################
#
#  TEXT ADVENTURE
#
# (c) Ryhmä 2: Tuomas Huttunen, Ville Pukki and Aki Sipovaara, 2015
#
###############################################################################

import Gamelogic
import dialog
# import getpass , not working in pycharm
import textwrap

#
# Creating connection to database.
#
# host = input("Server: ")
# user = input("User: ")
host = 'localhost'
user = 'root'
pswd = input("Password: ")
db = Gamelogic.open_database(host, user, pswd)


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
# Game start
input("Start Game")

ending = 0
while ending == 0:

    # Get location and print area description
    location = Gamelogic.location(db)
    description = Gamelogic.description(db, location)
    wrap(description)

    # Printing possible directions of movement
    direction = Gamelogic.direction(db, location)
    if len(direction) > 0:
        print("Possible directions of movement:", direction)

    # Print items in the area
    items = Gamelogic.items(db, location)
    if len(items) > 0:
        print("Items in the area:", items)

    # Special event 1: Making and drinking the potion
    #if location == 4:
    #    if "Suspicious Herbs" in Gamelogic.cmd_inventory(db):
    #        print("Do you want to trade the herbs for the potion?(y/n)")
    #        while True:
    #            answer = input()
    #            answer = answer.lower()
    #            if answer in ['y', 'yes', 'n', 'no']:
    #                break
    #            print("Please input y or n.")
    #        if answer in ['y', 'yes']:
    #            Gamelogic.create(db)
    #            print("Suspicious Herbs removed from inventory.\nPotion of Endless Memory added to inventory.")
    #        else:
    #            print("")
    #    if Gamelogic.potion_taken(db) == 0:
    #        if Gamelogic.shaman_met(db) == 0:
    #            wrap(
    #                "The shaman senses you are not all there.  He wants you to bring him a pile of dank Suspicious Herbs. "
    #                "They should restore your memory when brewed into a potion.")
    #            Gamelogic.meet_shaman(db)
    #        else:
    #            print("You should find the herbs to make the potion and restore your memories at the hill")

    # Special event 2: Filling the water bottle
    if location == 7 and "Water" not in Gamelogic.cmd_inventory(db):
        print("Do you want to fill your water bottle?(y/n)")
        answer = input()
        answer = answer.lower()
        if answer in ['y', 'yes']:
            Gamelogic.fill(db)
            print("Water added to your inventory.")
        else:
            print("")

    # Updating database on hill visit
    if location == 5 and Gamelogic.hill_visited(db) == 0:
        Gamelogic.visited_hill(db)

    # Special event 3: Fixing the boat
    if location == 7 and Gamelogic.boat_fixed(db) == 0:
        if "Wooden Tap" in Gamelogic.cmd_inventory(db):
            print("Do you want to fix the boat?(y/n)")
            while True:
                answer = input()
                answer = answer.lower()
                if answer in ['y', 'yes', 'n', 'no']:
                    break
                print("Please input y or n.")
            if answer in ['y', 'yes']:
                Gamelogic.fix_boat(db)
                Gamelogic.open_direction(db, 7, 8, "south")
                Gamelogic.open_direction(db, 8, 7, "north")
                print("Boat fixed.\n1 Wooden Tap removed from inventory.")
            else:
                print("")
        else:
            wrap(
                "You require a boat to cross the river, but the one on the shore has a hole in it."
                "Maybe someone in the tavern will have something to fix it.")

    # Special event 4: Trading for the wooden tap
    if location == 3:
        if "Wooden Tap" in Gamelogic.cmd_inventory(db):
            print("")
        else:
            if "Banana" in Gamelogic.cmd_inventory(db):
                print("Do you want to trade the banana for a wooden tap?(y/n)")
                while True:
                    answer = input()
                    answer = answer.lower()
                    if answer in ['y', 'yes', 'n', 'no']:
                        break
                    print("Please input y or n.")
                if answer in ['y', 'yes']:
                    Gamelogic.trade(db)
                    print("Banana removed from inventory.\n1 Wooden Tap added to inventory.")
                else:
                    print("")
            else:
                print("There is a sign that says 'Wooden taps for sale: Price 1 banana.'")
                if Gamelogic.hill_visited(db) == 0:
                    print("Where on earth are you going to find a banana.")
                else:
                    print("There may have been a banana tree on a hill somewhere.")

    # Special event 5: Entering the castle
    if location == 8 and Gamelogic.door_opened(db) == 0:
        print("There is a weird looking slot in the door.")
        if "The Sword of All Things Right" in Gamelogic.cmd_inventory(db):
            print("There is a slot in the castle door.\nYour sword looks like it could fit, "
                  "Do you wish to try inserting it into the slot?(y/n)")
            while True:
                answer = input()
                answer = answer.lower()
                if answer in ['y', 'yes', 'n', 'no']:
                    break
                print("Please input y or n.")
            if answer in ['y', 'yes']:
                print("Strangely your sword doesn't seem to fit at all.\nRidicilous.\nWhy would this thing not fit into this marvelously left aligned slot.")
        elif "The Sword of All Things Left" in Gamelogic.cmd_inventory(db):
            print("Insert your sword into the slot?(y/n)")
            while True:
                answer = input()
                answer = answer.lower()
                if answer in ['y', 'yes', 'n', 'no']:
                    break
                print("Please input y or n.")
            if answer in ['y', 'yes']:
                Gamelogic.open_direction(db, 8, 10, "south")
                Gamelogic.open_direction(db, 10, 8, "north")
                Gamelogic.door_opened(db)
                print("Door unlocked. Wasn't that hard now was it.")
            else:
                print("")
        else:
            wrap("There must be something that fits into it.\nIt's shaped like a"
                 "weird looking sword, but you have no such thing with you.")

    # Special event 6: Game ending and creation of the Potion of Transformation
    if location == 10:
        if "Potion of Transformation" in Gamelogic.cmd_inventory(db):
            print("Do you want to pour the potion into the wizards wine bottle?(y/n)")
            while True:
                answer = input()
                answer = answer.lower()
                if answer in ['y', 'yes', 'n', 'no']:
                    break
                print("Please input y or n.")
            if answer in ['y', 'yes']:
                print("You pour the potion into the wine bottle. A puff of green smoke erupts from the bottle.")
                print("You hear footsteps in the distance. Do you want to hide?(y/n)")
                while True:
                    answer1 = input()
                    answer1 = answer.lower()
                    if answer1 in ['y', 'yes', 'n', 'no']:
                        break
                    print("Please input y or n.")
                if answer1 in ['y', 'yes']:
                    wrap("The wizard walks into the room, pours a drink and takes a sip."
                         " A while passes and the wizard seems to feel ill.")
                    wrap("He starts panicking and is visibly confused, he has no idea what is wrong and"
                         "is helplessly trying to find answers in his spell book."
                         "But it is simply too late and he is suddenly transformed into a frog.")
                    ending = 1
                else:
                    wrap("The wizard walks into the room instantly spotting you. After hasty consideration"
                         "he blasts you with some kind of ghastly arcane energy and you transform into solid rock. "
                         "Seems like the wizard has a new statue. After a smug smile he pours a drink and drinks it. "
                         "A while passes and the wizard seems to feel ill."
                         "He starts panicking and is visibly confused, he has no idea what is wrong "
                         "and is helplessly trying to find answers in his spell "
                         "book. But it is simply too late and he is suddenly transformed into a frog.")
                    ending = 1

            else:
                print("You hear footsteps in the distance. Do you want to hide?(y/n)")
                while True:
                    answer1 = input()
                    answer1 = answer.lower()
                    if answer1 in ['y', 'yes', 'n', 'no']:
                        break
                    print("Please input y or n.")
                if answer1 in ['y', 'yes']:
                    wrap("The wizard walks in and after a little while drinks his wine and goes to bed."
                         "You hide the whole night and once the wizard leaves you slowly sneak out of the castle"
                         "and go into hiding hoping the wizard doesn't find you.")
                    ending = 1
                else:
                    wrap(
                        "The wizard walks into the room instantly spotting you. After hasty consideration he blasts"
                        "you with some kind of ghastly arcane energy and you transform into solid rock. "
                        "It seems like the wizard has a new statue.")
                    ending = 1

        else:
            if Gamelogic.castle_entered(db) == 1:
                wrap(
                    "After walking for a while in the castle you find a room with a spell book in plain sight."
                    " Seems like the wizard has carelessly left it open.")
                print("Read the book?(y/n)")
                while True:
                    answer = input()
                    answer = answer.lower()
                    if answer in ['y', 'yes', 'n', 'no']:
                        break
                    print("Please input y or n.")
                if answer in ['y', 'yes']:
                    print(
                        "\nPotion of Transformation:\n\n1 Magic Mushroom\n1 litre of water\nAlchemist Table\nAdd"
                        "water into the mixer\nLight a fire under the mixer\nAdd blue powder\nWait until"
                        " water turns clear\nSlice and add the mushroom\nWait 1 minute\nPour "
                        "the mixture into a bottle\n\nHmm.. Seems like everything but "
                        "the mushroom and a litre of water are here.\nI wonder if this would actually work.")
                else:
                    print("")
            elif "Magic Mushroom" in Gamelogic.cmd_inventory(db) and "Water" in Gamelogic.cmd_inventory(db):
                print("Do you want to make the Potion of Transformation?(y/n)")
                while True:
                    answer = input()
                    answer = answer.lower()
                    if answer in ['y', 'yes', 'n', 'no']:
                        break
                    print("Please input y or n.")
                if answer in ['y', 'yes']:
                    Gamelogic.create_potion(db)
                    wrap(
                        "Magic Mushroom removed from inventory\nWater removed from inventory\n"
                        "Potion of Transformation added to inventory")
                    continue
                else:
                    print("")

            else:
                print("Need to find the Magic Mushroom and some water to create the potion.")

    # Input and parsing
    print("")
    cmd = input("> ").lower()
    # This section removes the specified characters from the command input
    for char in cmd:
        if char in "';":
            cmd = cmd.replace(char, '')
    # Might cause problems if an input requires any of the characters removed i.e. "Dan's Vial" becomes "Dans vial" and is thus not an exact match anymore
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
        verb = cmd_list[0]
        object = ' '.join(cmd_list[1:len(cmd_list)])
        # print("Please input one or two words only.")

    # Command: move
    if verb in ['go', 'move', 'm', 'g']:
        if object in ['north', 'n'] or object in ['south', 's'] or object in ['west', 'w'] or object in ['east', 'e']:
            if object == 'n':
                object = 'north'
            if object == 's':
                object = 'south'
            if object == 'w':
                object = 'west'
            if object == 'e':
                object = 'east'
            if Gamelogic.cmd_move(db, location, object) == 0:
                print("Can't go that way.")

    # Command: Pick up
    elif verb in ['pick', 'p']:
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
    elif verb in ['inspect', 'ins']:
        if object == "":
            print("No item selected.")
        else:
            if Gamelogic.inspect(db, object) is not None:
                print(Gamelogic.inspect(db, object), "\n\n")
            else:
                print("No such item.")

    # Command: rotate
    elif verb in ['rotate', 'r']:
        if object in ['sword', 'the sword of all things right', 'sword of all things right'] and "The Sword of All Things Right" in Gamelogic.cmd_inventory(db):
            Gamelogic.rotate(db)
            print("Sword of All Things Right removed from inventory.")
            print("Sword of All Things Left added to inventory")
        else:
            print("Nothing to rotate.")

    # Command: inventory (shows items on the player)
    elif verb in ['inventory', 'i']:
        print(Gamelogic.cmd_inventory(db))

    # Command: drop
    elif verb in ['drop', 'd']:
        if object == "":
            print("No item selected.")
        elif Gamelogic.cmd_drop(db, object, location) == 0:
            print(object, "can't be dropped.")
        else:
            print(object, "dropped.")

    # Command: talk
    elif verb in ["talk", "speak"]:
        if object == "":
            print("You talk to yourself.\n")
        elif object == "to shaman" and Gamelogic.location(db) == 4:
            herbs = False
            if "Suspicious Herbs" in Gamelogic.cmd_inventory(db):
                herbs = True
            potion = dialog.talkShaman(herbs)
            if potion:
                Gamelogic.create(db)
            print("")
        elif object == "to trader" and Gamelogic.location(db) == 9:
            memorypotiondrank = False
            if Gamelogic.potion_taken(db) == 1:
                memorypotiondrank = True
            mushroom = dialog.talkTrader(memorypotiondrank)
            if mushroom:
                Gamelogic.trade_mushroom(db)
            print("")
        else:
            print("You talk gibberish.\n")

    # Command: drink (potion)
    elif verb == "drink":
        if object == "":
            print("Choose an item.")
        elif object == "potion of endless memory" and "Potion of Endless Memory" in Gamelogic.cmd_inventory(db):
            Gamelogic.take_potion(db)
            print("Potion of Endless Memory removed from inventory.")
        elif object == "potion of transformation" and "Potion of Transformation" in Gamelogic.cmd_inventory(db):
            print("Potion of Transformation removed from inventory.")
            wrap("You start feeling ill and you pass out. You wake up feeling teRIBBITle. "
                 "You have no idea what is going on. RIBBIT!  And then you realize, you've turned... "
                 "...into a frog. RIBBIT!")
            ending = 1
        else:
            print("No such item")

    # Command: help
    elif verb in ['help', 'h']:
        print("Commands:\nMove () North, South, East, West\nInventory (shows items you have)\n"
              "Drop (item) Drops a specific item\nPick (item) Picks up an item\nInspect (item) Inspects an item\n"
              "Rotate (item)\nEnd (ends the game)")

    # Command: end
    elif verb in ['end', 'e']:
        while True:
            answer = input("Are you sure you want to quit?(y/n)")
            answer = answer.lower()
            if answer in ['y', 'yes', 'n', 'no']:
                break
            print("Please input y or n.")
        if answer in ['y', 'yes']:
            while True:
                answer = input("Do you want to save the game?(y/n)")
                answer = answer.lower()
                if answer in ['y', 'yes', 'n', 'no']:
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

input("The game has ended. Thank you for playing! Press enter to end the game.")
