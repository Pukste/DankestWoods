import mysql.connector


#
# Opening database connection.
#
def open_database(hostname, user, password):
    return mysql.connector.connect(
        host=hostname, user=user, passwd=password, db="peligame", buffered=True)


#
# Returns player location.
#
def location(db):
    cur = db.cursor()
    cur.execute("select location from player where id = 1")
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
    cur.execute("select itemid from item where location = " + str(id))
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
    cur2 = db.cursor()
    cur2.execute("update item owner = NULL where itemid = ??")


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
    cur.execute("select location from item where itemid = '" + item + "'")
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
    new_location = str(row[0])
    cur2 = db.cursor()
    cur2.execute("update player set location = " + new_location + " where id = 1")
    return 1


#
# Command: pick up
#
def cmd_pick(db, item):
    cur1 = db.cursor()
    cur1.execute("update item set owner = 1 where itemid = '" + item + "'")
    cur2 = db.cursor()
    cur2.execute("update item set location = NULL where itemid = '" + item + "'")


#
# Command: inventory
#
def cmd_inventory(db):
    cur = db.cursor()
    cur.execute("select itemid from item where owner = 1")
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
    cur.execute("update item set owner = 1 where itemid =(insert item id for water here)")
    cur2 = db.cursor()
    cur2.execute("update item set owner = NULL where itemid =(empty water bottle)")


#
# Function: merge(unfinished)
#
def create_potion(db):
    cur = db.cursor()
    cur.execute("update item set owner = NULL where itemid =(magic mushroom)")
    cur2 = db.cursor()
    cur2.execute("update item set owner = NULL where itemid =(water)")
    cur3 = db.cursor()
    cur3.execute("update item set owner = 1 where itemid =(potion of transformation)")


#
# Command: inspect
#
def inspect(db, item):
    cur = db.cursor()
    cur.execute("select description from item where itemid = '" + item + "'")
    return (cur.fetchone())[0]


#
# Command: drop
#
def cmd_drop(db, itemdb, location):
    cur1 = db.cursor()
    cur1.execute("update item set location = " + str(location) + " where itemid = '" + item + "' and owner = 1")
    cur2 = db.cursor()
    cur2.execute("update item set owner = NULL where itemid = '" + item + "' and owner = 1")
    return cur2.rowcount


#
# Function: trade
#
def trade(db):
    cur = db.cursor()
    cur.execute("update item set owner = NULL where itemid =??")
    cur2 = db.cursor()
    cur2.execute("update item set owner = 1 where itemid =??")


#
# Function: trading with shaman
#
def create(db):
    cur = db.cursor()
    cur.execute("update item set owner = NULL where itemid =??")
    cur2 = db.cursor()
    cur2.execute("update item set owner = 1 where itemid =??")


#
# Function: drinking the potion of endless memory
#
def drink(db):
    cur = db.cursor()
    cur.execute("update item set owner = NULL where itemid =??")


#
# Command; rotate
#
def rotate(db):
    cur = db.cursor()
    cur.execute("update item set owner = NULL where itemid =??")
    cur2 = db.cursort()
    cur2.execute("update item set owner = 1 where itemid =??")
