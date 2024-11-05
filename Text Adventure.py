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

x = 2
y = 2

while (True):

    playerposition = rooms_exits[x][y]
    #print(playerposition)

    print ("What now?")
    command = input()

    if(command == "north"):
        if rooms_exits[x][y][NORTH]:
            print ("You moved North...")
            y = y - 1
        else:
            print ("You can't move North...")
    elif(command == "south"):
        if rooms_exits[x][y][SOUTH]:
            print ("You moved South...")
            y = y + 1
        else:
            print ("You can't move South...")
    elif(command == "west"):
        if rooms_exits[x][y][WEST]:
            print ("You moved West...")
            x = x - 1
        else:
            print ("You can't move West...")
    elif(command == "east"):
        if rooms_exits[x][y][EAST]:
            print ("You moved East...")
            x = x + 1
        else:
            print ("You can't move East...")
    elif(command == "up"):
        if rooms_exits[x][y][NORTH]:
            print ("You moved North...")
            y = y - 1
        else:
            print ("You can't move North...")
    elif(command == "down"):
        if rooms_exits[x][y][SOUTH]:
            print ("You moved South...")
            y = y + 1
        else:
            print ("You can't move South...")
    else:
        print("I don't understand " + command + " !")