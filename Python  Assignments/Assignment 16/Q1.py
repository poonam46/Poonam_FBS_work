class Book:
    count = 0

    def __init__(self,bid=None,bname="",price=100,author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def showBook(self):
        print(f"Book ID : {self.bid}\nBook Name : {self.bname}\nPrice : {self.price}\nAuthor : {self.author}\nTotal Count Of Objects : {Book.count}\n")


    def __del__(self):
        print("Destructor is called")

b = Book()
b1 = Book(101,"C",200,"Dennis Richard")
b2 = Book(102,"Python",100,"ABC")
b1.showBook()
b2.showBook()