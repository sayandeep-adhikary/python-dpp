def oddSum(n):
    ans = 0
    for i in range(1, n+1):
        if i&1:
            ans += i
    return ans

a = int(input("Enter the nth term : "))
print(f"Sum of all Odd Numbers between 1 and {a} is : " + str(oddSum(a)))