class Book:
    def __init__(self,bid = None,bname = " ",price = 150,author = " "):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def getData(self):
        return f"Book ID : {self.bid}\nBook Name : {self.bname}\nPrice : {self.price}\nAuthor : {self.author}"
    
    def __del__(self):
        print("Destructor is called")

b1 = Book(101,"Shyamachi Aai",200,"Sane Guruji")
print(b1.getData())
print("************************")

b2 = Book()
print(b2.getData())

print("************************")