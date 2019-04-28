n = int(input("Rows : "))

for x in range(0, n):
    for y in range(0, n - 1 - x):
        print(end=" ")
    for z in range(0, x + 1):
        print("*", end=" ")
    print()