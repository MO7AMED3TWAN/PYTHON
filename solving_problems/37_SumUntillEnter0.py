Result=0
while True :
    Number=int(input("Enter Numbers To Summation  Or Zero To Stop : "))
    if Number != 0 :
        Result=Result+Number
    else:
        print(f"Result Of Summation Is : {Result}")
        break