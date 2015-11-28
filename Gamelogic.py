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
    cur.execute("select location from character where id = 1")
    return (cur.fetchone())[0]


#
# Returns area description
#
def description(db, id):
    cur = db.cursor()
    cur.execute("select description from location where id = " + str(id))
    return (cur.fetchone())[0]


#
# Returns possible movement directions
#
def direction(db, id):
    cur = db.cursor()
    cur.execute("select north, east, south, west from location where id = " + str(id))
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
    cur.execute("select item from object where location = " + str(id))
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
    cur.execute("select value from events where id = 1")
    return (cur.fetchone())[0]


#
# Updates the info if the potion has been taken
#
def take_potion(db):
    cur = db.cursor()
    cur.execute("update events set value = 1 where id = 1")


#
# Checks if the shaman has been met
#
def shaman_met(db):
    cur = db.cursor()
    cur.execute("select value from events where id = 2")
    return (cur.fetchone())[0]


#
# Updates the database when the shaman has been met
#
def meet_shaman(db):
    cur = db.cursor()
    cur.execute("update events set value = 1 where id = 2")


#
# Checks if the boat has been fixed
#
def boat_fixed(db):
    cur = db.cursor()
    cur.execute("select value from events where id = 3")
    return (cur.fetchone())[0]


#
# Updates the database when boat is fixed
#
def fix_boat(db):
    cur = db.cursor()
    cur.execute("update events set value = 1 where id = 3")


#
# Checks if the hill have been visited
#
def hill_visited(db):
    cur = db.cursor()
    cur.execute("select value from events where id = 4")
    return (cur.fetchone())[0]


#
# Updates the database when hill has been visited
#
def visited_hill(db):
    cur = db.cursor()
    cur.execute("update events set value = 1 where id = 4")


#
# Checks if the castle has been entered
#
def castle_entered(db):
    cur = db.cursor()
    cur.execute("select value from events where id = 5")
    return (cur.fetchone())[0]


#
# Updates the database when the castle is entered
#
def entered_castle(db):
    cur = db.cursor()
    cur.exevute("update events set value = value + 1 where id = 5")


#
# Returns the location of a given object
#
def object_location(db, item):
    cur = db.cursor()
    cur.execute("select location from object where item = '" + item + "'")
    if cur.rowcount == 0:
        return None
    return (cur.fetchone())[0]


#
#
#
def open_direction(db, leave, go, direction):
    cur = db.cursor()
    cur.execute("update location set " + direction + " = " + str(go) + " " + "where id = " + str(leave))


#
# Command: move (north, east, south, west)
#
# Returns 1 if movement complete, 0 if not
#
def cmd_move(db, location, direction):
    cur1 = db.cursor()
    cur1.execute("select " + direction + " from location where id = " + str(location))
    row = cur1.fetchone()
    if row[0] is None:
        return 0
    new_location = str(rivi[0])
    cur2 = db.cursor()
    cur2.execute("update character set location = " + new_location + " where id = 1")
    return 1


#
# Command: pick up
#
def cmd_pick(db, item):
    cur1 = db.cursor()
    cur1.execute("update object set owner = 1 where item = '" + item + "'")
    cur2 = db.cursor()
    cur2.execute("update object set location = NULL where item = '" + item + "'")


#
# Command: inventory
#
def cmd_inventory(db):
    cur = db.cursor()
    cur.execute("select item from object where owner = 1")
    inventory = []
    result = cur.fetchall()
    for row in result:
        inventory.append(row[0])
    return inventory


#
# Fills the water bottle.
#
def fill(db):
    cur = db.cursor()
    cur.execute("update object set owner = 1 where item =(insert item id for water here)")


#
# Command: merge(unfinished)
#
def create_potion(db):
    cur = db.cursor()
    cur.execute("update object set owner = 0 where item =(magic mushroom)")
    cur2 = db.cursor()
    cur2.execute("update object set owner = 0 where item =(water)")
    cur3 = db.cursor()
    cur3.execute("update object set owner = 1 where item =(potion of transformation)")


#
# Command: inspect
#
def inspect(db, item):
    cur = db.cursor()
    cur.execute("select description from object where item = '" + item + "'")
    return cur.result


#
# Command: drop
#
def cmd_drop(db, item, location):
    cur1 = db.cursor()
    cur1.execute("update object set location = " + str(location) + " where item = '" + item + "' and owner = 1")
    cur2 = db.cursor()
    cur2.execute("update object set owner = NULL where description = '" + item + "' and owner = 1")
    return cur2.rowcount


#
# Function: trade
#
def trade(db):
    cur = db.cursor()
    cur.execute("update object set owner = NULL where item =??")
    cur2 = db.cursor()
    cur2.execute("update object set owner = 1 where item =??")


#
# Function: trading with shaman
#
def create():
    cur = db.cursor()
    cur.execute("update object set owner = NULL where item =??")
    cur2 = db.cursor()
    cur2.execute("update object set owner = 1 where item =??")
