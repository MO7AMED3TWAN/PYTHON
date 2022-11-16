No_Pennies=int(input("Enter Numbers Of Pennies : "))
No_Nickels=int(input("Enter Numbers Of Nickels : "))
No_Dimes=int(input("Enter Numbers Of Dimes : "))
No_Quarters=int(input("Enter Numbers Of Quarters : "))
No_Dollars=int(input("Enter Numbers Of Dollars : "))
Result_Penny=(No_Pennies*1)+(No_Nickels*5)+(No_Dimes*10)+(No_Quarters*25)+(No_Dollars*100)
Result_Dollar=Result_Penny/100
print(f"Result By Penny = {Result_Penny}")
print(f"Result By Dollars = {Result_Dollar}")




