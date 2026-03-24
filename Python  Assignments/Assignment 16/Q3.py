class Shirt:
    charges = 10

    def __init__(self,sid = None,sname = " ",type = "Formal",price = 500, size = " "):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def getData(self):
        return f"Shirt ID : {self.sid}\nShirt Name : {self.sname}\nType : {self.type}\nPrice : {self.price}\nSize : {self.size}"
    
    def calculateAmt(self):
        if self.size == 'small':
            self.price = self.price
            print("Final Price : ",self.price)
        elif self.size == 'medium':
            amt = (self.price * Shirt.charges) / 100
            self.price += amt
            print("Final Price : ",self.price)
        elif self.size == 'large':
            amt = (self.price * (Shirt.charges * 2)) / 100
            self.price += amt
            print("Final Price : ",self.price)
        elif self.size == 'xlarge':
             amt = (self.price * (Shirt.charges * 3)) / 100
             self.price += amt
             print("Final Price : ",self.price)

    def __del__(self):
        print("Destructor is called")

s1 = Shirt(1001,"Raymond","Casual",1000,"small")
print(s1.getData())
s1.calculateAmt()
print("************************")

s2 = Shirt()
print(s2.getData())

print("************************")

s3 = Shirt(1001,"Raymond","Casual",1000,"large")
print(s3.getData())
s3.calculateAmt()
print("************************")
