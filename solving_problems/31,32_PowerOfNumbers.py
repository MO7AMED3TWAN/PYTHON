#Power 2,3,4 of NUMBER
Number=int(input("Enter A Number : "))
power_2=Number*Number
print(f"Power 2 Is : {power_2}")
power_3=Number*Number*Number
print(f"Power 3 Is : {power_3}")
power_4=Number*Number*Number*Number
print(f"Power 4 Is : {power_4}")

##power X for Number
Number=int(input("Enter A Number : "))
Power=int(input("Enter A Power : "))
Result=1
Counter=0
if Power == 0:
    print(f"Result Is : {Result}")
else :
    while True:
        if Counter < Power :
            Result=Result*Number
            Counter+=1
        else:
            print(f"Result Is : {Result}")
            break






