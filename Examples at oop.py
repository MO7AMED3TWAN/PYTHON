print("====__====1==__=====")
class students():
    def __init__(self,name):
        self.name=name
        self.marks=[]            
        print(f"WELCOME {name} TO THE SCHOOL")
    def marks(self):
        return self.marks
    def addmark (self, *mark):
        for item in mark:
            self.marks.append(item)
            
    # @property
    def avg (self):
        return sum (self.marks) /len(self.marks)

std1=students("AHMED")
std1.addmark(19,20,17,14,19,20)
print(std1.marks)
print(std1.avg())

print("========2=======")
class animal1():
    def __init__(self,name):
        self.name=name.title()
        print(f"Animal's Name IS {self.name}")
    def eat (self,food):
        print(f"{self.name} eat {self.food}")
animal_1=animal1("dog")
print("-------")
class animal2(animal1):
    def __init__(self,name,food):
        self.food=food.title()
        super().__init__(name)
        print(f"{self.name} Is Your Animal And Eat {self.food}")
    
animal_2=animal2("cat","fish") """

""" ##class modifiers ()        
class circle ():
    def __init__(self,r=1,name="circle"):
        self.r=r
        self.__pi=22/7#private 
        self._name=name#protected
    def getpi(self):
        return self.__pi
    def area(self):
        return self.__pi*self.r **2 
    def perimeter(self):
        return 2*self.__pi*self.r
cir_1=circle()
cir_2=circle(2)
print(cir_1._name)
cir_1._name="circle new"
print(cir_1._name)
print(cir_1.area())
print(cir_2.area())
 


