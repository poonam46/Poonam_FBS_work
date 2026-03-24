class ModelNumberException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Model Number is not greater than 4 digits'
    
class ScreensizeException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Screen size is not smaller than 12 inches and greater than 70 inches'
    

class PriceException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Price is not negative or greater than 5000 Rs.'

