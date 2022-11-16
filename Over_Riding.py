### Examples On Over Riding ###
class worker:
    def __init__(self,salary):
        self.salary=salary
    def anual_salary(self):
        return self.salary*12

class SalesMan(worker):
    def __init__ (self,salary,comm,salesvalues):
        self.salary=salary
        self.comm=comm
        self.salesvalues=salesvalues
    def anual_salary(self):
        return (self.comm*self.salesvalues) + (self.salary*12) 
#####طيب هنا انا عاوز اوصل للفانكشن بالرقم من انى عامل اوفر رايدينج هتعمل سوبر واسم الفانكشن بس 
#####def anual_salary_witout_comm(self):
#####    return super().anual_salary

#دى بردو طريقة تانيه علشان تستخدم الفانكشن ال ف الاب بعد عمل اوفر رايدينج عليها 
    def anual_salary_without_comm(self):
        return worker.anual_salary(self)
### Client _ Code ###
w=worker(1000)
print("Worker Salary : ",w.anual_salary())
s=SalesMan(2000,0.1,100000)
print("SaleMan Salary : ",s.anual_salary())
print("SaleMan Salary Without Comm : ",s.anual_salary_without_comm())       

### ISINSTANCE() ##
## هنا هنسأل عل الاوبجكت ده هو وارث من ال كلاس ولا لاوبتاخد الاوبجكت ثم الكلاس         
print("isinstance(w,worker) :",isinstance(w,worker))#TRUE     
#print(isinstance(worker,w))#ERROR
print("isinstance(s,worker) :",isinstance(s,worker))#TRUE

### ISSUBCLASS() ###
##هنا بتسأل هل الاول وارث من التانى ولا اى الوضع بالضبط
print("issubclass(SalesMan,worker) : ",issubclass(SalesMan,worker))#TRUE
print("issubclass(worker,SalesMan) : ",issubclass(worker,SalesMan))#FALSE لان العمال مش وارث انما مورِث


