class Complexnumber:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __add__(self,other):
        self.real = self.real + other.real
        self.imag = self.imag + other.imag

        return self

    def __sub__(self,other):
        self.real = self.real - other.real
        self.imag = self.imag - other.imag

        return self
    
    def displayAdd(self):
        return f"{self.real}+{self.imag}i"

    def displaySub(self):
        return f"{self.real}-{self.imag}i"

    def __del__(self):
        print("Destructor is called...")


c1 = Complexnumber(6,8)
c2 = Complexnumber(4,3)

c3 = c1 + c2
print(c3.displayAdd())

c4 = c1 - c2
print(c4.displaySub())