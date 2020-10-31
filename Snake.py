import arcade
import random


X = "X"
line0 = [X,X,X,X,X,X,X,X,X,X,X,X]
line1 = [X,X,X,X,X,X,X,X,X,X,X,X]
line2 = [X,X,X,X,X,X,X,X,X,X,X,X]
line3 = [X,X,X,X,X,X,X,X,X,X,X,X]
line4 = [X,X,X,X,X,X,X,X,X,X,X,X]
line5 = [X,X,X,X,X,X,X,X,X,X,X,X]
line6 = [X,X,X,X,X,X,X,X,X,X,X,X]
line7 = [X,X,X,X,X,X,X,X,X,X,X,X]
line8 = [X,X,X,X,X,X,X,X,X,X,X,X]
line9 = [X,X,X,X,X,X,X,X,X,X,X,X]
line10 = [X,X,X,X,X,X,X,X,X,X,X,X] 
line11 = [X,X,X,X,X,X,X,X,X,X,X,X]
line12 = [X,X,X,X,X,X,X,X,X,X,X,X]


empty = "X"
snake = ["O"]
snakecords = []
part = "O"
apple = "a"
applecords = []

screen = [line0,
          line1,
          line2,
          line3,
          line4,
          line5,
          line6,
          line7,
          line8,
          line9,
          line10,
          line11,
          line12]

def start():
    for line in screen:
        print(line)
    print("\n")


def on_key_release(self, key, key_modifiers):
        if key == arcade.key.UP_ARROW:
            move(x, y +1 )






def Snake():
    snake.append(part)

def move(x, y):
    if len(snakecords) == 0:
        pass
    else:
        screen[snakecords[0]][snakecords[1]] = empty
        snakecords.clear()
        print(snakecords)
    screen[y][x] = snake[0]
    snakecords.append(y)
    snakecords.append(x)
    start()
def AppleSpawn():
    screen[applecords[0],applecords[1]] = empty
    x = random.randint(0,11)
    y = random.randint(0,11)
    applecords.append(y, x)
    screen[x][y] = apple
    start()
    return(applecords)




start()



move(0,0)
move(3,3)
move(5,5)
print(snakecords)
move(6, 4)

    




        

