class BasicEmployeeDetails:

    def __init__(self, name, age):
        self.e_name = name
        self.e_age = age

    def show_detail(self):
        output = "Name:{}\nAge:{}".format(self.e_name, self.e_age)
        return output


class AdvanceEmployeeDetails(BasicEmployeeDetails):

    def __init__(self, name:str, age:int, salary:int, designation:str):
        self.e_salary = salary
        self.designation = designation
        super().__init__(name, age)

    def show_details(self, secure=True):
        if secure is False:
            output = "Name:{}\nAge:{}\nSalary:{}\nDesignation:{}".format(self.e_name, self.e_age, self.e_salary, self.e_designation)"
            return output
        else:
            return super().show_detail()


