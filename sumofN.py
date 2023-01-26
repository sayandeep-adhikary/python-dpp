def addSum(a):
    if a == 0:
        return 0
    return a + addSum(a-1)
a = int(input("Enter the nth term : "))
print(addSum(a))