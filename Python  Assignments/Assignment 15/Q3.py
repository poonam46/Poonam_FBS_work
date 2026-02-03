class Shirt:
    def __init__(self,sid = None,sname = " ",type = "Formal",price = 500, size = " "):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def getData(self):
        return f"Shirt ID : {self.sid}\nShirt Name : {self.sname}\nType : {self.type}\nPrice : {self.price}\nSize : {self.size}"
    
    def __del__(self):
        print("Destructor is called")

s1 = Shirt(1001,"Raymond","Casual",1000,"Large")
print(s1.getData())
print("************************")

s2 = Shirt()
print(s2.getData())

print("************************")
