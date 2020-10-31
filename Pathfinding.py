
import random
grid = [x[:] for x in [["."] * 10 ]* 10]

openPos = []
closedPos = []
prevPoints = []

nodeStart = [0,0]


def update():
    for i in grid:
        print(i)


def walls(amount):
    for i in range(amount):
        x, y = random.randint(0,9), random.randint(0,9)
        grid[y][x] = "X"
        closedPos.append([y,x])
        print("\n")


def CheckNearbyCells(cell):
    #Defining some variables
    RList = []
    Y = cell[0]
    X = cell[1]
    Y1 = Y + 1
    X1 = X + 1
    

    #Checking all points around the point we put in
    if grid[X1][Y] != "X":
        #if [X1, Y] not in closedPos:
        grid[(X1)][(Y)] = "@"
        closedPos.append([X1, Y])
        RList.append([X1, Y])
        prevPoints.append([X1, Y])
    if grid[X1][Y1] != "X":
        #if [X1, Y1] not in closedPos:
        grid[(X1)][Y1] = "@"
        closedPos.append([X1, Y1])
        RList.append([X1, Y1])
        prevPoints.append([X1, Y])
    if grid[X][Y1] != "X":
        #if [X, Y1] not in closedPos:
        grid[(X)][(Y1)] = "@"
        closedPos.append([X, Y1])
        RList.append([X, Y1])
        prevPoints.append([X1, Y])
    update()
    #Calling Update to update the screen
    print("\n")
    #Returning the list of points retaining to the original point
    return(RList)


walls(15)
update()

print("\n")

CheckNearbyCells([0,0])
"""
for i in prevPoints:
    if i != closedPos:
        CheckNearbyCells(i)
    if i == [9,9]:
        break
"""



#Bug List
#Fix it so that it can travel past the first 2 lines x

































"""
def iteration(possibleValues):
    possibleValues = []
    firstTime = True
    if firstTime == True:
        possibleValues.append([0,0])
        for i in range(len(possibleValues)):
            print(possibleValues)
            for x in possibleValues[i]:
                subValues = []
                subValues.append(x)
                subValues.append(x+1)

            possibleValues.append(subValues)
    return(possibleValues)

newValue = iteration([])
for i in range(10):
    iteration(newValue)

numSolutions = False
while numSolutions == False:
    for i in grid:
        for j in i:
            print(grid[i][j+1])
"""



                

                

        


