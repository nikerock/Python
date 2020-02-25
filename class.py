class Employee:
    company_name ="Netmax Technology Pvt LTD."

    def __init__(self, name, age, mobile):
        self.e_name = name
        self.e_age = age
        self.e_mobile = mobile


    def update_mobile(self, mobile):
        self.e_mobile = mobile


    def show_info(self):
        output = "Name:{}\nAge:{}\nMobile:{}".format(self.e_name, self.e_age, self.e_mobile)
        return output


    @classmethod
    def change_company(cls, c_name):
        cls.company_name = c_name

    @classmethod
    def show_company(cls):
        return cls.company_name

    @staticmethod
    def about():
        output = "<{}.{}>".format(__name__,Employee.__name__)
        return output



obj1 = Employee("XYZ", 32, 8956235666)
obj2 = Employee("qwerty", 35, 89562345663)
Obj3 = Employee("asdsa", 37, 9041536789)
print(obj1.show_info())
print(obj2.show_info())
print(Obj3.show_info())

print(obj1.show_company())
print(obj2.show_company())
print(Obj3.show_company())
obj1.change_company("New York Times Ltd")
print(obj1.show_company())
print(obj2.show_company())
print(Obj3.show_company())

print(obj1.about())