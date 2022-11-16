from cmath import sqrt
from numpy import diagonal


Length=int(input("Enter The length of Rectangle : "))
Weidth=int(input("Enter The weidth of Rectangle : "))
Diagonal=int(input("Enter The Value Of Diagonal : "))
AreaOfRectangle=Length*Weidth
print(f"Area Of Rectangle Is : {AreaOfRectangle}")

print("---Area Through Diagonal---")
AreaOfRectangle=Length*sqrt(Diagonal*Diagonal-Length*Length)
print(f"Area Of Rectangle is : {AreaOfRectangle}")



