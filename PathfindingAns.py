import random
grid = [x[:] for x in [[-1] * 20] * 20]

def obsticals(amount):
  for _ in range(amount):
    x,y = random.randint(0,len(grid[0]) - 1), random.randint(0,len(grid)- 1)
    grid[x][y] = 'X'

def pg():
  for g in grid:
    [print("%2s" % x, end = " ") for x in g]
    print()


def step(steps, candidates):
  new_candidates = []
  for point in candidates:
    x,y = point
    if grid[x][y] != -1:
      # we've already visisted this point
      continue
    if grid[x][y] == 'Q':
      # Done!
      break

    if x > 0: # we can look to the left
      if grid[x - 1][y] == -1:
        new_candidates.append((x - 1, y))
    if x < len(grid[0]) - 1: # We can look to the right
      if grid[x + 1][ y] == -1:
        new_candidates.append((x + 1, y))
    if y > 0: # We can look up
      if grid[x][y - 1] == -1:
        new_candidates.append((x, y - 1))
    if y < len(grid) - 1: # We can look down
      if grid[x][y + 1] == -1:
        new_candidates.append((x, y + 1))
      
    grid[x][y] = steps
  return (steps + 1, new_candidates)

s = 0
candidates = [(random.randint(0,len(grid[0]) - 1), random.randint(0,len(grid)- 1))]
grid[random.randint(0,len(grid[0]) - 1)][ random.randint(0,len(grid)- 1)] = 'Q'
obsticals(10)
while True:
  s, candidates = step(s, candidates)
  pg()
  input()



  