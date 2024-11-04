rooms_exits = [
    [(False, False, True, False), (False, True, False, False), (False, True, True, True), (False, True, True, True), (False, False, True, True)],
    [(True, False, True, False), (False, True, True, False), (True, True, True, True), (True, False, False, True), (True, False, True, False)],
    [(True, False, True, False), (True, False, False, False), (True, False, True, False), (False, True, False, False), (True, False, True, True)],
    [(True, False, True, False), (False, True, True, False), (True, True, False, True), (False, True, False, True), (True, False, True, False)],
    [(True, True, False, False), (True, False, False, True), (False, False, False, False), (True, False, False, False), (True, False, False, False)]
]
initialposition = (2,2)

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

while (True):

    x,y = initialposition
    playerposition = rooms[x][y]
    print(playerposition)

    print ("What now?")
    command = input()

    if(command == "north"):
        print ("You moved North...")
    elif(command == "south"):
        print("You moved south...")
    elif(command == "west"):
        print("You moved west...")
    elif(command == "east"):
        print("You moved east...")
    elif(command == "up"):
        print("You moved north...")
    elif(command == "down"):
        print("You moved south...")
    else:
        print("I don't understand " + command + " !")