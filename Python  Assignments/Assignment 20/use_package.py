from SYPackage.SY import SYMARKS 
from TYPackage.TY import TYMarks

class Student:
    def __init__(self, roll_number, name, symarks, tymarks):
        self.roll_number = roll_number
        self.name = name
        self.symarks = symarks
        self.tymarks = tymarks

    def calculate_grade(self):
        total = self.symarks.ComputerTotal + self.tymarks.Theory
        perc = total / 2

        if perc >= 70:
            return "A"
        elif perc >= 60:
            return "B"
        elif perc >= 50:
            return "C"
        elif perc >= 40:
            return "Pass"
        else:
            return "Fail" 
        
    def display(self):
        print("*** Student Result ***")
        print(f"Roll No. : {self.roll_number}\nName : {self.name}\nSY Marks : {self.symarks.ComputerTotal}\nTY Marks : {self.tymarks.Theory}\nGrade : {self.calculate_grade()}")
        


sy = SYMARKS(75,80,90)
ty = TYMarks(72,80)

st = Student(101, "Poonam", sy, ty)
st.display()
