l = int(input("Enter the lower limit : "))
h = int(input("Enter the upper limit : "))
print(f"The odd numbers between {l} and {h} are : ")
while (l <= h):
    if(l%2 != 0):
        print(l, end=" ")
    l = l + 1
        
# for i in range(l, h+1):
#     if(i%2 != 0):
#         print(i, end=" ")