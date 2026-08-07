
# -----------------------------------------MINI PROJECT NO.3-----------------------------------------


#---------------------------- Store and display Hospital Paitent details-------------------------




class HospitalPatient:
  def __init__(self,name ,age, disease,doctor,treament_cost):
     self.name = name
     self.age = age
     self.disease = disease
     self.doctor = doctor
     self.treatment_cost = treament_cost

  def display(self):
     print("Patient Name:", self.name)   
     print("Age:", self.age)   
     print("Disease:", self.disease)   
     print("Doctor:", self.doctor)   
     print("Treatment Cost:", self.treatment_cost)   


patient1 = HospitalPatient(
   "Rahul" , 35, "Fever" , "Dr. Sharma" , 2500
)
patient1.display()