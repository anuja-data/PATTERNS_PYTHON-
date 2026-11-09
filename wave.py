n = 4

for i in range(n):
    for j in range(13):
        if (j+i) % 4 == 0 or (j-i) % 4 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()