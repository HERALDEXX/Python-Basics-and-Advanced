class Student:
    def __init__(self, name, age, student_id, major, year):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.major = major
        self.year = year

    def study(self):
        print(f"{self.name} is studying for their {self.major} major.")

student1 = Student("Alice", 20, "S12345", "Computer Science", "4th")

student1.study()

