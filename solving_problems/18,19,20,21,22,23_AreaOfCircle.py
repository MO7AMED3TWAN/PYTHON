from numpy import pi#لاستعاء قيمة الباى 
print("----Area Of Circle Through Diagonal----")
Diagonal=int(input("Enter The Value Of Diagonal : "))
Area_1=pi*(Diagonal**2)
print("Area Of Circle :"," ",round(Area_1,2))#لتقريب الرقم بخانتين عشريتين فقط 

print("\n","----Area Of Circle Through Diameter----")
Diameter=2*Diagonal
print(f"The Value Of Diameter Is : {Diameter}")
Area_2=(pi*Diameter**2)/4
print(f"Area Of Circle : {Area_2}")

print("\n","----Area Of Circle Through Circumference----")
Circumference=int(input("Enter The Circumference : "))
Area_3=(Circumference**2)/(4*pi)
print(f"Area Of Circle : {Area_3}")




