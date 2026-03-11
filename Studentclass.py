
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation



student1 = Student("Jim", "Business", 3.4 , True)
student2 = Student("Pam", "Business", 2.4 , False)

students = [student1, student2]
for student in students:
    print(f"Student Name: {student.name}, Major: {student.major}, GPA: {student.gpa}, is_on_probation: {student.is_on_probation}")