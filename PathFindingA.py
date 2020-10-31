import random
grid = [x[:] for x in [["."] * 10 ]* 10]

length = 9
NonNeighbors = []
startPos = [0,0]
Steps = 0
Canadites = []
Canadites.append(startPos)


def neighbors(currentpos, currentl):
    X = currentpos[1]
    Y = currentpos[0]
    Rlist = []
    if [X + 1, Y] not in NonNeighbors:
        if [X + 1, Y] not in Canadites:
            if X <= length & Y <= length:
                Rlist.append([X + 1, Y])
                grid[X+ 1][Y]= currentl
                Canadites.append(currentl)
    if [X + 1, Y + 1] not in NonNeighbors:
         if [X + 1, Y + 1] not in Canadites:
            if X <= length & Y <= length:
                Rlist.append([X + 1, Y + 1])
                grid[X+ 1][Y+ 1] = currentl
                Canadites.append(currentl)
    if [X, Y + 1] not in NonNeighbors:
        if [X, Y + 1] not in Canadites:
            if X <= length & Y <= length:
                Rlist.append([X, Y + 1])
                grid[X][Y + 1] = currentl
                Canadites.append(currentl)
    NonNeighbors.extend(Rlist)
    update()
    return (Rlist, currentl)

def update():
    for i in grid:
        print(i)
    print("\n")


def walls(amount):
    for i in range(amount):
        x, y = random.randint(0,9), random.randint(0,9)
        grid[y][x] = "X"
        NonNeighbors.append([x, y])
        print("\n")


def start():
    while grid[x][y] != []
start()


    

  