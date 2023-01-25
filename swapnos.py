a = []
n = input("Enter the number : ")
print("Before Swap : " + n)
for i in n:
    a.append(int(i))
print(a)
(a[0], a[len(a) - 1]) = (a[len(a) - 1], a[0])
print(a)
l = len(a)
ans = 0
for i in a:
    ans += i * (10 ** (l-1))
    l = l - 1
print("After Swap : " + str(ans))