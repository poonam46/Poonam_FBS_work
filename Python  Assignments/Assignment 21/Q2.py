# from TV_Exception_handle import *

class Television:
    def __init__(self ):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def acceptDetails(self):
        try:
            self.model_number = int(input("Enter the Model Number : "))
            mno = str(self.model_number)
            if(len(mno) > 4):
                raise ValueError("Model number cannot be more than 4 digits")
            
            self.screen_size = int(input("Enter the screen size : "))
            if(self.screen_size < 12 or self.screen_size > 70):
                raise ValueError("Screen size must be between 12 and 70 inches")
            
            self.price = float(input("Enter the price : "))
            if(self.price < 0 or self.price > 5000):
                raise ValueError("Price must be between 0 and 5000 Rs.")
            
        except Exception as e:
            print("Error : ", e)
            print("Setting all values to 0")
            self.model_number = 0
            self.screen_size = 0
            self.price = 0
        
    def display(self):
        print("Details of TV")
        print(f"Model Number : {self.model_number}\nScreen Size : {self.screen_size}\nPrice : {self.price}")

def main():
    tv = Television()
    tv.acceptDetails()
    tv.display()

main()