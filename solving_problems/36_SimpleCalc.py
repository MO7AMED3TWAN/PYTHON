Number1=int(input("Enter First Number : "))
Number2=int(input("Enter Second Number : "))
Operation=input("Enter The Operation : ")
if Operation=='+':
    print("Summation : ",Number1+Number2)

elif Operation=='-':
    print("Subtraction : ",Number1-Number2)
elif Operation=='*':
    print("Multiplcation : ",Number1*Number2)
elif Operation=='/':
    print('Devision : ',Number1/Number2)
elif Operation not in ['+','-','*','/']:
    print("wrong Operation please choise * / + -")
else:
    pass



