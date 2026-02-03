class Product:
    def __init__(self,pid = None,pname = " ",price = 100,quantity = 0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def getData(self):
        return f"Product ID : {self.pid}\nProduct Name : {self.pname}\nPrice : {self.price}\nQuantity : {self.quantity}"
    
    def __del__(self):
        print("Destructor is called")

p1 = Product(101,"Notebook",200,6)
print(p1.getData())
print("************************")

p2 = Product()
print(p2.getData())

print("************************")