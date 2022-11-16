Number=int(input("Enter A Positive Number : "))
while True :
    if Number <=0:
        print("Factorial Must Be Positive Number !!")
        Number=int(input("PlEASE ENTER A POSITIVE NUMBER : "))
    else :
        Counter=Number+1
        Factorial=1
        while True:
            Counter-=1
            if Counter>1:
                Factorial=Factorial*Counter
            else:
                print(f"Factorial Value Is : {Factorial}")
                break
        break



