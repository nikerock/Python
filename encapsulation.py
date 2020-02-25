"""
Encapsulation public _protected __private
"""
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary

    def info(self):
        output = "Name: {}\nAge: {}\nSalary: {}".format(self.name, self._age, self.__salary)
        return output
    def _update_salary(self, salary):
        self.__salary = salary

obj = Employee("User1", 23, 20000)
print(obj.info())
obj._age = 27
obj._update_salary(25000)
print(obj.info())