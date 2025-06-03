class student:
    def __init__(self):
        self.id = input("Enter student id: ")
        self.name = input("Enter student name: ")
        self.marks = input("Enter student marks: ")
    def display(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)
        print("Student Marks:", self.student_marks)
obj = student()
obj1 = student()
obj.display()
obj1.display()

