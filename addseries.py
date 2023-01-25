n = int(input("Enter the nth term : "))
ans = 0
for i in range(1, n+1):
    ans += 1/(i+1)
    if i != 1:
        print(f"1/{i}", end=" + ")

print(f"1/{n+1} = ", end=" ")
print("%0.3f" %ans)