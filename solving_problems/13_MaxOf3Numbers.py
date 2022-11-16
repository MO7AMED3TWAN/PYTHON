Number1=int(input("Enter the First Number : "))
Number2=int(input("Enter the Second Number : "))
Number3=int(input("Enter the Third Number : "))

if Number1>Number2 and Number1>Number3:
    print("First Number Is The Biggest !!")
elif (Number1>Number2 or Number2>Number1) and (Number3>Number1 or Number3>Number2):
    print("Third Number Is the Biggest !!")
else:
    print("Second Number Is the Biggest !!")