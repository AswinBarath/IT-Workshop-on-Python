class Person:
    def __init__(self, name):
        self.name = name

    def display1(self):
        print('End of the Statement')


class Student(Person):
    def __init__(self, name, usn, branch):
        super().__init__(name)
        self.name = name
        self.usn = usn
        self.branch = branch

    def display2(self):
        print(f'name: {self.name}')
        print(f'usn: {self.usn}')
        print(f'branch: {self.branch}')
        self.display1()


aswin = Student('Ashwin', 31, 'SE')
aswin.display2()
