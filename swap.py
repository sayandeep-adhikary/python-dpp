a = int(input("Enter a number : "))
b = int(input("Enter another number : "))
print("Using a Third Variable :")
print("Before Swap")
print("a = ", a)
print("b = ", b)
c = a
a = b 
b = c
print("After Swap")
print("a = ", a)
print("b = ", b)
print("Without Using a Third Variable :")
print("Before Swap")
print("a = ", a)
print("b = ", b)
(a,b) = (b,a)
print("After Swap")
print("a = ", a)
print("b = ", b)
print("Using Bitwise operator")
print("Before Swap")
print("a = ", a)
print("b = ", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("After Swap")
print("a = ", a)
print("b = ", b)