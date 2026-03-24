class Student:
    def __init__(self,studentid,name,age,percentage):
        self.studentid = studentid
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.studentid = int(input("Enter Student ID : "))
        self.name = input("Enter the Name : ")
        self.age = int(input("Enter the Age : "))
        self.percentage = float(input("Enter the Percentage : "))

    def display(self):
        print(f"Student ID : {self.studentid}\nName : {self.name}\nAge : {self.age}\nPercentage : {self.percentage}") 

    def calculateRank(self):
        if self.percentage >= 90:
            return "A+"
        elif self.percentage >= 75:
            return "A"
        elif self.percentage >= 60:
            return "B"
        elif self.percentage >= 50:
            return "C"
        else:
            return "Fail"
        
    def __str__(self):
         return f"Student ID : {self.studentid}\nName : {self.name}\nAge : {self.age}\nPercentage : {self.percentage}\nRank : {self.calculateRank()}"

class EnggStudent(Student):
    def __init__(self,studentid,name,age,percentage,branch,internalMarks):
        super().__init__(studentid,name,age,percentage)
        self.branch = branch    
        self.internalMarks = internalMarks 

    def accept(self):
        super().accept()
        self.branch = input("Enter the branch name : ")
        self.internalMarks = int(input("Enter the internal marks : "))

    def display(self):
        super().display()
        print(f"Branch : {self.branch}\nInternal Marks : {self.internalMarks}")

    def calculateRank(self):
       avg = (self.percentage + self.internalMarks) / 2

       if avg >= 90:
           return "Distiction"
       elif avg >= 75:
           return "First Class"
       elif avg >= 60:
           return "Second Class"
       elif avg >= 40:
           return "Pass"
       else:
           return "Fail"
       
    def __str__(self):
        return super().__str__() + f"\nBranch : {self.branch}\nInternal Marks : {self.internalMarks}"
    

class MedicalStudent(Student):
    def __init__(self,studentid,name,age,percentage,specialization,marksOfInternship):
        super().__init__(studentid,name,age,percentage)
        self.specialization = specialization    
        self.marksOfInternship = marksOfInternship

    def accept(self):
        super().accept()
        self.specialization = input("Enter the specialization : ")
        self.marksOfInternship = int(input("Enter the marks of intership : "))

    def display(self):
        super().display()
        print(f"Specialization : {self.specialization}\nMarks of Intership : {self.marksOfInternship}")

    def calculateRank(self):
       total = (self.percentage + self.marksOfInternship) / 2

       if total >= 90:
           return "Distiction"
       elif total >= 75:
           return "First Class"
       elif total >= 60:
           return "Second Class"
       elif total >= 40:
           return "Pass"
       else:
           return "Fail"
       
    def __str__(self):
        return super().__str__() + f"\nSpecialization : {self.specialization}\nMarks of Intership : {self.marksOfInternship}"
    
class College:
    def __init__(self,capacity):
        self.capacity = capacity
        self.students = []

    def addStudent(self,student):
        if(len(self.students) < self.capacity):
            self.students.append(student)
            print("Student Added Successfully...")
        else:
            print("College capacity is full...")

    def getStudent(self,studentid):
        for stud in self.students:
            if stud.studentid == studentid:
                return stud
        return None
    
    def removeStudent(self,studentid):
        stud = self.getStudent(studentid)
        if stud:
            self.students.remove(stud)
            print("Student removed successfully...")
        else:
            print("Student not found")

    def __str__(self):
        result = "College Students List : \n"
        for stud in self.students:
            result += str(stud) + "\n\n"
        return result


c = College(3)

s1 = EnggStudent(1, "Rahul", 20, 85,"Computer",90)
s2 = MedicalStudent(2, "Priya", 22, 78, "Cardiology", 95)

c.addStudent(s1)
c.addStudent(s2)

print(c)

student = c.getStudent(1)
if student:
    print("Found Student : \n", student)

print("***************************************************")
c.removeStudent(2)
print(c)
