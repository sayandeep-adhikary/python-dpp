def checkP(s):
    i = 0
    j = len(s) - 1
    while(i <= j):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
s = input("Enter the number : ")
if checkP(s):
    print(f"{s} is PALINDROME")
else:
    print(f"{s} is NOT PALINDROME")
