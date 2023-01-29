a = []
no = int(input("Enter the Number : "))
while no != 0:
    a.append(no % 10)
    no //= 10
a = a[::-1]
print("The list is : ", a)
l = len(a)
sum = 0
for i in a:
    sum += i * (10 ** (l-1))
    l -= 1
print("The number is ", sum)