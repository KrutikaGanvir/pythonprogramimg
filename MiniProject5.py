#--------------------------MiniProject NO. 5-----------------------------

#-----------Create a online stuednt class with students enrolment----------------
class OnlineCourse:
    def __init__(self, course_name, instructor, fees, duration):
        self.course_name = course_name
        self.instructor = instructor
        self.fees = fees
        self.duration = duration
        self.students = []

    def enroll_student(self,student_name):
        self.students.append(student_name)
        print(student_name, "enrolled successfully")    

    def display(self):
        print("Course:" ,self .course_name)
        print("Instructor:",self.instructor )
        print("feesL:",self.fees )
        print("duration:",self.duration )
        print("Enrolled Students:",self.students )

course1 = OnlineCourse(
    "Python Programming", "Sonu Mam", 5000, "3 Months"
)

course1.enroll_student("Amit")
course1.enroll_student("Sneha")
course1.enroll_student("Riya")
course1.display()