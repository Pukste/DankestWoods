import mysql.connector


#
# Opening database connection.
#
def open_database(hostname, user, password):
    return mysql.connector.connect(
        host=hostname, user=user, passwd=password, db="game", buffered=True)


#
# Returns player location.
#
def location(db):
    cur = db.cursor()
    cur.execute("select locationid from player where playerid = 1")
    return (cur.fetchone())[0]


#
# Returns area description
#
def description(db, id):
    cur = db.cursor()
    cur.execute("select description from location where locationid = " + str(id))
    return (cur.fetchone())[0]


#
# Returns possible movement directions
#
def direction(db, id):
    cur = db.cursor()
    cur.execute("select north, east, south, west from location where locationid = " + str(id))
    row = cur.fetchone()
    compass = ['north', 'east', 'south', 'west']
    directions = []
    for i in range(0, 4):
        if row[i] is not None:
            directions.append(compass[i])
    return directions


#
# Returns list of items in the area
#
def items(db, id):
    cur = db.cursor()
    cur.execute("select name from item where locationid = " + str(id))
    items = []
    result = cur.fetchall()
    for row in result:
        items.append(row[0])
    return items


#
# Returns info if potion has been taken
#
def potion_taken(db):
    cur = db.cursor()
    cur.execute("select value from events where eventsid = 1")
    return (cur.fetchone())[0]


#
# Updates the info if the potion has been taken
#
def take_potion(db):
    cur = db.cursor()
    cur.execute("update item set playerid = NULL where itemid = 9")
    cur2 = db.cursor()
    cur2.execute("update events set value = 1 where eventsid = 1")


#
# Checks if the shaman has been met
#
def shaman_met(db):
    cur = db.cursor()
    cur.execute("select value from events where eventsid = 2")
    return (cur.fetchone())[0]


#
# Updates the database when the shaman has been met
#
def meet_shaman(db):
    cur = db.cursor()
    cur.execute("update events set value = 1 where eventsid = 2")


#
# Checks if the boat has been fixed
#
def boat_fixed(db):
    cur = db.cursor()
    cur.execute("select value from events where eventsid = 3")
    return (cur.fetchone())[0]


#
# Updates the database when boat is fixed
#
def fix_boat(db):
    cur = db.cursor()
    cur.execute("update events set value = 1 where eventsid = 3")
    cur2 = db.cursor()
    cur2.execute("update item set playerid = NULL where itemid = 4")


#
# Checks if the hill have been visited
#
def hill_visited(db):
    cur = db.cursor()
    cur.execute("select value from events where eventsid = 4")
    return (cur.fetchone())[0]


#
# Updates the database when hill has been visited
#
def visited_hill(db):
    cur = db.cursor()
    cur.execute("update events set value = 1 where eventsid = 4")


#
# Checks if the castle has been entered
#
def castle_entered(db):
    cur = db.cursor()
    cur.execute("select value from events where eventsid = 5")
    return (cur.fetchone())[0]


def open_door(db):
    cur = db.cursor()
    cur.execute("update events set value 1 where eventsid = 6")


def door_opened(db):
    cur = db.cursor()
    cur.execute("select value from events where eventsid =6")
    return (cur.fetchone())[0]


#
# Updates the database when the castle is entered
#
def entered_castle(db):
    cur = db.cursor()
    cur.exevute("update events set value = value + 1 where eventsid = 5")


#
# Returns the location of a given object
#
def object_location(db, item):
    cur = db.cursor()
    cur.execute("select locationid from item where name = '" + item + "'")
    if cur.rowcount == 0:
        return None
    return (cur.fetchone())[0]


#
#
#
def open_direction(db, leave, go, direction):
    cur = db.cursor()
    cur.execute("update location set " + direction + " = " + str(go) + " " + "where locationid = " + str(leave))


#
# Command: move (north, south, west, east)
#
# Returns 1 if movement complete, 0 if not
#
def cmd_move(db, location, direction):
    cur1 = db.cursor()
    cur1.execute("select " + direction + " from location where locationid = " + str(location))
    row = cur1.fetchone()
    if row[0] is None:
        return 0
    new_location = str(row[0])
    cur2 = db.cursor()
    cur2.execute("update player set locationid = " + new_location + " where playerid = 1")
    return 1


#
# Command: pick up
#
def cmd_pick(db, item):
    cur1 = db.cursor()
    cur1.execute("update item set playerid = 1 where name = '" + item + "'")
    cur2 = db.cursor()
    cur2.execute("update item set locationid = NULL where name = '" + item + "'")


#
# Command: inventory
#
def cmd_inventory(db):
    cur = db.cursor()
    cur.execute("select name from item where playerid = 1")
    inventory = []
    result = cur.fetchall()
    for row in result:
        inventory.append(row[0])
    return inventory


#
# Command: inventory in lowercase for comparing with parser
#
def low_inventory(db):
    cur = db.cursor()
    cur.execute("select name from item where playerid = 1")
    inventory = []
    result = cur.fetchall()
    for row in result:
        row = str(row).lower()
        inventory.append(row)
    return inventory


#
# Fills the water bottle.
#
def fill(db):
    cur = db.cursor()
    cur.execute("update item set playerid = 1 where itemid = 11")
    cur2 = db.cursor()
    cur2.execute("update item set playerid = NULL where itemid = 6")


#
# Function: merge(unfinished)
#
def create_potion(db):
    cur = db.cursor()
    cur.execute("update item set playerid = NULL where itemid = 5")
    cur2 = db.cursor()
    cur2.execute("update item set playerid = NULL where itemid = 11")
    cur3 = db.cursor()
    cur3.execute("update item set playerid = 1 where itemid = 10")


#
# Command: inspect
#
def inspect(db, item):
    cur = db.cursor()
    cur.execute("select description from item where name = '" + item + "'")
    if cur.rowcount == 0:
        return None
    return (cur.fetchone())[0]


#
# Command: drop
#
def cmd_drop(db, item, location):
    cur1 = db.cursor()
    cur1.execute("update item set locationid = " + str(location) + " where name = '" + item + "' and playerid = 1")
    cur2 = db.cursor()
    cur2.execute("update item set playerid = NULL where name = '" + item + "' and playerid = 1")
    return cur2.rowcount


#
# Function: trade
#
def trade(db):
    cur = db.cursor()
    cur.execute("update item set playerid = NULL where itemid = 8")
    cur2 = db.cursor()
    cur2.execute("update item set playerid = 1 where itemid = 4")


#
# Function: trading with shaman
#
def create(db):
    cur = db.cursor()
    cur.execute("update item set playerid = NULL where itemid = 3")
    cur2 = db.cursor()
    cur2.execute("update item set playerid = 1 where itemid = 9")


#
# Command; rotate
#
def rotate(db):
    cur = db.cursor()
    cur.execute("update item set playerid = NULL where itemid = 1")
    cur2 = db.cursor()
    cur2.execute("update item set playerid = 1 where itemid = 2")

def trade_mushroom(db):
    cur = db.cursor()
    cur.execute("update item set playerid = 1 where name = 'magic mushroom'")