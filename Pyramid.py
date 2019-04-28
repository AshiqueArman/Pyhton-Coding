n = int(input("Rows : "))           #taking input from user

for x in range(0, n):               #number of rows. Means how tall the pyramid will be.
    for y in range(0, n - 1 - x):   #loop for giving required spaces for the formation of pyramid
        print(end=" ")
    for z in range(0, x + 1):       #loop for printing the stars
        print("*", end=" ")
    print()                         #going to a new row
