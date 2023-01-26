def countDigit(n):
    if n == 0:
        return 0
    return 1 + countDigit(n//10)

a = int(input("Enter a number : "))
print(f"There are {countDigit(a)} digits in {a} ")