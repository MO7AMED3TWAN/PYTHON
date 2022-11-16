print("1 to N\n")
Number = int(input("Enter A Number For Counter : "))
Counter=0
Counter+=1
print(Counter)
while True:
    Counter+=1
    if Counter < Number:
        print(Counter)
    else:
        print(Number)
        break

print("\nN to 1\n") 
Number = int(input("Enter A Number For Counter : "))
Counter=Number
print(Counter)

while True:
    Counter-=1
    if Counter == 1:
        print(Counter)
        break
    else:
        print(Counter)


print("\nSum of Odd Numbers 1 to N\n")
Number = int(input("Enter A Number For Counter : "))
Counter=0
Counter+=1
SumOfOdd=Counter
while True:
    Counter+=1
    if (Counter < Number) and (Counter%2 == 1):
        SumOfOdd+=Counter
    elif Counter < Number:
        pass
    else:
        break
print(f"Sum Of Odd Numbers Is : {SumOfOdd}")


print("\nSum of Even Numbers 1 to N\n")
Number = int(input("Enter A Number For Counter : "))
Counter=0
SumOfEven=Counter
while True:
    Counter+=1
    if (Counter <= Number) and (Counter%2 == 0):
        print(Counter)
        SumOfEven+=Counter
    elif Counter < Number:
        pass
    else:
        break
print(f"Sum Of Even Numbers Is : {SumOfEven}")
