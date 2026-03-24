class Product:
    discount = 10

    def __init__(self,pid = None,pname = " ",price = 100,quantity = 0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def getData(self):
        return f"Product ID : {self.pid}\nProduct Name : {self.pname}\nPrice : {self.price}\nQuantity : {self.quantity}"
    
    def countDiscount(self):
        dis_amt = (self.price * Product.discount) / 100
        self.price -= dis_amt
        print(f"Discounted Price = {self.price}")

    
    def __del__(self):
        print("Destructor is called")

p1 = Product(101,"Notebook",200,6)
print(p1.getData())
p1.countDiscount()
print("************************")

p2 = Product()
print(p2.getData())
p2.countDiscount()
print("************************")