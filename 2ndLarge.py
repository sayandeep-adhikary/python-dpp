a = []
size = int(input("Enter the no of elements : "))
print("Enter the elements : ")
for i in range(0, size):
    x = int(input())
    a.append(x)
print("The list is : ", a)
a.sort()
print(f"2nd smallest element is {a[1]} and 2nd largest element is {a[size - 2]}")