class Student:
    def __init__(self, name):
        self.name = name
        self.note = self.Notebook()

    def show(self):
        print(self.name, end="")
        self.note.show()

    class Notebook:
        def __init__(self):
            self.model = "HP"
            self.cpu = "i7"
            self.ram = "16"

        def show(self):
            print(f" =>, {self.model}, {self.cpu}, {self.ram}")


student1 = Student("Roman")
student2 = Student("Vladimir")


student1.show()
student2.show()
