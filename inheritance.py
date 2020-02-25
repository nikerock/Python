#singl/ simple inheritance
class A:
    def method_1(self):
        print("class A method")

class B(A):
    def method_2(self):
        print("Class B method")

#multi level inheritance
class A:
    def method_1(self):
        print("class A method")

class B(A):
    def method_2(self):
        print("Class B method")

class C(B):
    def method_3(self):
        print("Class C Method")


#herirecal inheritance
class A:
    def method_1(self):
        print("class A method")

class B(A):
    def method_2(self):
        print("Class B method")

class C(A):
    def method_3(self):
        print("Class C Method")