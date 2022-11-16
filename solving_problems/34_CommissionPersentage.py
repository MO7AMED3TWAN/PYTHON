TotalSales=int(input("Enter Your TotalSales : "))
if TotalSales>=1000000:
    Commission=TotalSales*0.01
elif TotalSales>=500000 and TotalSales<1000000:
    Commission=TotalSales*0.02
elif TotalSales>=100000 and TotalSales<500000:
    Commission=TotalSales*0.03
elif TotalSales>=50000 and TotalSales<100000:
    Commission=TotalSales*0.05
else:
    Commission=TotalSales*0
print(f"Commission is : {Commission}")



