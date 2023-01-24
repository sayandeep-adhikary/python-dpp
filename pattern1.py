row = int(input("Enter the number of rows : "))
a = 1
for i in range(0, row):
    for j in range(0, i+1):
        print(a, end=" ")
        a = a + 1
    print("\n")