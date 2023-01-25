import math
x1 = int(input("Enter x1 : "))
y1 = int(input("Enter y1 : "))
x2 = int(input("Enter x2 : "))
y2 = int(input("Enter y2 : "))
ans = math.sqrt(((x1-x2) ** 2) + ((y1-y2) ** 2))
print(f"Distance between ({x1},{y1}) and ({x2},{y2}) is : %0.3f" %ans)
