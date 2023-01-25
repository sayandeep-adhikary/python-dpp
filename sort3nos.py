a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
print("The Sorted List is : ")
if a > b and a > c:
    max = a
else:
    if b > a and b > c:
        max = b
    else:
        max = c
        
        
if a < b and a < c:
    min = a
else:
    if b < a and b < c:
        min = b
    else:
        min = c
        
        
mid = (a+b+c) - max - min
print(min, mid, max)