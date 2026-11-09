n = 5

for i in range(1, n+1):
    print(str(i) * i + " " * (2*(n-i)) + str(i) * i)

for i in range(n-1, 0, -1):
    print(str(i) * i + " " * (2*(n-i)) + str(i) * i)