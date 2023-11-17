from grid4 import grid, SIZE, INPUT
RED = '\033[91m'
YELLOW = '\033[92m'
ENDC = '\033[0m'

#clear file
with open("dyno.txt", "w") as f:
    pass

r = 0
c = 0

def isValidMove(r1, c1, r2, c2):
    deltas = sorted([abs(r1 - r2), abs(c1 - c2), abs(grid[r1][c1] - grid[r2][c2])])
    if deltas == [0, 1, 2]:
        return True
    return False

def translate(move):
    newr = int(move[1]) - 1
    newc = ord(move[0]) - ord('a')
    return (newr, newc)

ind = 0
totalTime = 0
while True:
    # find all and wait
    cur = grid[r][c]
    sames = []
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == cur and (i != SIZE - 1 - r or j != SIZE - 1 - c):
                sames.append((i, j))
    
    n = len(sames)

    print(f"n = {n}")

    if ind < len(INPUT):
        time, move = INPUT[ind]
        READINPUT =  True
    else:
        iii = input("Next move: ")
        time, move = iii.split()
        time = float(time)
        READINPUT = False
        
    diff = float(time)/n


    newr, newc = translate(move)
    if grid[r][c] == grid[newr][newc] and time > 0:
        with open("hi.txt", "w") as ff:
            ff.write("unecessary sink")

    if grid[SIZE - 1 - r][SIZE - 1 - c] != cur:
        grid[SIZE - 1 - r][SIZE - 1 - c] += diff

    for i, j in sames:
        grid[i][j] -= diff



    if isValidMove(r, c, newr, newc):
        r = newr
        c = newc
        totalTime += time
        ind += 1
        with open("dyno.txt", "a") as f:
            f.write(f"({'%g'%time}, {move}), ")
    else:
        print(RED + f"ILLEGAL MOVE: ({time}, {move})  (move {ind})" + ENDC)
        if grid[SIZE - 1 - r][SIZE - 1 - c] != cur:
            grid[SIZE - 1 - r][SIZE - 1 - c] -= diff

        for i, j in sames:
            grid[i][j] += diff
        if READINPUT:
            break

    # print result
    print("")
    print(f"Total time: {totalTime}")
    print("      a      b      c      d      e      f      g      h    ")
    print("   ======================================================")

    SPACING = 7
    for i in range(SIZE):
        string = f"{i + 1} |   "
        for j in range(SIZE):
            if (i, j) == (r, c):
                string += RED + (f"{'%g'%(round(grid[i][j], SPACING - 5))}").ljust(SPACING) + ENDC
            elif grid[r][c] == grid[i][j] and (r, c) != (SIZE - 1 - i, SIZE - 1 - j):
                string += YELLOW + (f"{'%g'%(round(grid[i][j], SPACING - 5))}").ljust(SPACING) + ENDC
            else:
                string += (f"{'%g'%(round(grid[i][j], SPACING - 5))}").ljust(SPACING) 
        print(string)
