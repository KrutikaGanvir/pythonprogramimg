
#clases & object practice questions

# class student:
#     name = "Rahul"

# s1 = student()
# print(s1.name)

#oops

# 1.CREATE A CLASS NAMEED STUDENT AND CREATE ONE OBJECT

# class Student:
#     pass
# student1 = Student()
# print("Student object created successfully")


# Q2. Create a Student class with name and age attributes.

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Student Name:", self.name)
#         print("Student Age:", self.age)

# student1 = Student("Rahul",20)
# student2 = Student("Krutika",21)       
# student1.display()
# student2.display()


# Create a car classs with brand model and price.

class Car:
    def __init__(self,brand, model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)    
        print("model:", self.model)    
        print("Brand:", self.price)  
car1 = Car("Tata", "Nexon" , 900000)
car2 = Car("Hyundi", "Creta" , 1200000)

car1.display()

car2.display()       