Age=int(input("Enter Ur Age : "))
if Age >=18 and Age <=45:
    print("Valid Age !!")
else:print("Invalid Age !!")    

print("LOOOOOOOOOOP")

while True:
    Age=int(input("Enter Ur Age : "))
    Result = (Age >=18) and (Age <=45)
    if Result == True :
        print("Valid Age !!")
        break
    else : continue
