def power(base, exp):
    # iterative
    # ans = 1
    # for i in range(0, exp):
    #     ans *= base
    # return ans

    # recursive
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
    
        
base = int(input("Enter the base : "))
exp = int(input("Enter the exponent : "))
print(f"{base} ^ {exp} = ", power(base, exp))