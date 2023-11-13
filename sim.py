from grid4 import grid, SIZE, INPUT

r = 0
c = 0

def isValidMove(r1, c1, r2, c2):
    deltas = sorted([abs(r1 - r2), abs(c1 - c2), abs(grid[r1][c1] - grid[r2][c2])])
    if deltas == [0, 1, 2]:
        return True
    return False

ind = 0
for time, move in INPUT:
    # find all and wait
    cur = grid[r][c]
    sames = []
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == cur and (i != SIZE - 1 - r and j != SIZE - 1 - c):
                sames.append((i, j))
    
    n = len(sames)
    diff = float(time)/n

    if grid[SIZE - 1 - r][SIZE - 1 - c] != cur:
        grid[SIZE - 1 - r][SIZE - 1 - c] += diff

    for i, j in sames:
        grid[i][j] -= diff

    # move
    newr = int(move[1]) - 1
    newc = ord(move[0]) - ord('a')

    if isValidMove(r, c, newr, newc):
        r = newr
        c = newc
    else:
        print(f"ILLEGAL MOVE: ({time}, {move})  (move {ind})")
        break
    ind += 1

# print result
print(f"Final coords: ({r}, {c})")
print("=================================================")

SPACING = 7
for i in range(SIZE):
    string = ""
    for j in range(SIZE):
        string += (f"{'%g'%(round(grid[i][j], SPACING - 5))}").ljust(SPACING)
    print(string)