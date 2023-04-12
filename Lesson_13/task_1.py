# Make a class structure in python representing people at school. Make a base class called Person,
# a class called Student, and another one called Teacher. Try to find as many methods and attributes
# as you can which belong to different classes, and keep in mind which are common and which are not.
# For example, the name should be a Person attribute, while salary should only be available to the teacher.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")


class Student(Person):
    def __init__(self, name, age, gender, grade_level):
        super().__init__(name, age, gender)
        self.grade_level = grade_level
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in {course}.")

    def list_courses(self):
        print(f"{self.name}'s courses:")
        for course in self.courses:
            print(f"- {course}")


class Teacher(Person):
    def __init__(self, name, age, gender, subject, salary):
        super().__init__(name, age, gender)
        self.subject = subject
        self.salary = salary

    def assign_grade(self, student, course, grade):
        print(f"{self.name} assigns {grade} to {student}'s {course} course.")

    def introduce(self):
        super().introduce()
        print(f"I am a {self.subject} teacher with a salary of {self.salary}.")


Student("Maks", 18, "Male", "Bachelor").introduce()
Student("Maks", 18, "Male", "Bachelor").enroll("'Python Розробка'")
Teacher("Illya", 22, "Male", "Python", "5000 dollars").assign_grade("Maks", "'Python Розробка'", "Bachelor")
Teacher("Illya", 22, "Male", "Python", "5000 dollars").introduce()
