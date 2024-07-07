#1. Creating a class -> giving it attribute -> and printing the attribute

class Person:
    def __init__(self,name:str,age:int) -> None:
        self.__name=name
        self.__age=age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name=value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self.__age=age
    
    def display_info(self):
        print(f"{self.__name} is {self.__age} years old!")
    

    def __str__(self) -> str:
        return f"Person : {self.__name} , Age : {self.__age}"
    
class Employee(Person):

    def __init__(self, name: str, age: int, id:int) -> None:
        super().__init__(name, age)
        self.__employeeid=id

    @property
    def employee_id(self):
        return self.__employeeid
    
    @employee_id.setter
    def employee_id(self,id):
        self.employeeid=id 

    def display_info(self):
        super().display_info()
        print(f"employee id : {self.__employeeid}")

    @classmethod
    def from_string(cls, emp_string):
        name, age, employee_id = emp_string.split('-')
        return cls(name, int(age), employee_id)
    
    def __str__(self) -> str:
         return f"{self.name} is {self.age} years old and have a employeeid as {self.__employeeid}"


# Create an instance of Person
print()
person = Person("Aashish", 20)
print(person)
person.display_info()
print()

# Modify attributes using setters # Encapsulation Concept

person.name = "Aashish Kumar Singh"
person.age = 21
print(person)
person.display_info()
print()

# Create an instance of Employee

employee = Employee("Aashish Kumar", 20, 1)
print(employee)
employee.display_info()
print()

# Modify attributes using setters

employee.name = "Aashish Kumar Singh"
employee.age = 21
employee.employeeid =2
print(employee)
employee.display_info()
print()



