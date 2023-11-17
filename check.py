from collections import Counter

with open("submitted.txt", "r") as f:
    s = f.read()
    #print(s)
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.replace(",", "")
    print(s)
    
    arr = s.split()
    times = []
    moves = []
    print(len(arr))
    for i in range(0, len(arr), 2):
        times.append(int(arr[i]))
        moves.append(arr[i + 1])
    
    print(sum(times))
    print(len(times))
    print(times)
    print(len(moves))
    print(moves)

    print(Counter(moves))

    for i in range(len(times)):
        print(f'({times[i]}, "{moves[i]}"), ')