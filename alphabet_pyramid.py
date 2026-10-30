for i in range(1, 6):
    for j in range(65, 65+i):
        print(chr(j), end="")
    for j in range(64+i-1, 64, -1):
        print(chr(j), end="")
    print()