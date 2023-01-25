a = []
ans = 0
while 1:
    i = int(input("Enter a number('0' will end the program!) : "))
    if i == 0:
        break
    else:
        ans += i
        a.append(i)   
for i in range(0, len(a)-1):
    print(a[i], end=" + ")
print(a[len(a) - 1], end=" = ")
print(ans)