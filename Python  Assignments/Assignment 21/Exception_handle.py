class NumberException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return 'Invalid numbers'
        

class OperatorException(Exception):
    def __init__(self,op):
        self.op = op

    def __str__(self):
        return f'{self.op} is invalid operator'
    
class ZeroDivideException(Exception):
    def __init__(self, num2):
        self.num2 = num2

    def __str__(self):
        return 'Division by zero not allowed'

