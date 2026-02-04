# OOP
#string = "Hello"
#print(string.upper())

class Car:
    def drive(self):
        print("Driven")
    
    def milege(self,cm):
        return cm+1 
    def __init__(self,name,year):
        self.name = name
        self.year = year

        #print(name)
    def get_name(self):
        return self.name
    def get_year(self):
        return(self.year)
    def set_year(self,year):
        self.year = year
    



ford = Car("taurus",2023)
##print(type(ford))
##ford.drive()
lexus = Car("LS430",2005)
#print(ford.milege(100))
print(lexus.get_name(), lexus.get_year())
print(ford.get_name(), ford.get_year())
ford.set_year(2025)
print(ford.get_year())