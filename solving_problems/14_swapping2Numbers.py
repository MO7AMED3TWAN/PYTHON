from ast import Num
from ctypes.wintypes import INT


Number1=int(input("Enter First Number : "))
Number2=int(input("Enter Second Number : "))
print(f"Frist Number is : {Number1}")
print(f"Second number is : {Number2}")

print("------After Swapping--12-----")

tempNumber=Number1
Number1=Number2
Number2=tempNumber

print(f"Frist Number is : {Number1}")
print(f"Second number is : {Number2}")
