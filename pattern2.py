row = int(input("Enter the number of rows : "))
for i in range(1, row+1):
    for j in range(1, 2*(row+1) - 2):
        if j>=i and j <= (2*(row+1) - 2)-i:
            print("*", end=" ")
        else:
            print(" ", end=" ")     
    print("\n")