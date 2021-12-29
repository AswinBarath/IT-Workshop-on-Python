class Student:
    def greet1(self):
        print('Good Afternoon Sir')


class Guy:
    def greet2(self):
        print('Hi sir')


class Man(Student, Guy):
    def __init__(self, name):
        self.name = name

    def greet3(self):
        print('Hello Gentleman')


person1 = Man('Ashwin')
person1.greet1()
person1.greet2()
person1.greet3()
