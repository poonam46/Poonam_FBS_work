class Distance:
    def __init__(self,km,m,cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self,other):
        cm = self.cm + other.cm
        m = cm // 100
        self.cm = cm % 100

        m = m + self.m + other.m
        km = m // 1000
        self.m = m % 1000

        self.km = km + self.km + other.km

        return self
    
    def __sub__(self,other):
        cm = self.cm - other.cm
        m = 0
        km = 0
        if cm < 0:
            cm += 100
            m -= 1

        m = self.m - other.m + m
        if m < 1000:
            m += 1000
            km -= 1

        km = self.km - other.km + km

        self.km = km
        self.m = m
        self.cm = cm
        
        return self
    
    def __str__(self):
        return f"{self.km} : {self.m} : {self.cm}"
    
    
    def __del__():
        print("Destructor is called...")

d1 = Distance(2,500,80)
d2 = Distance(1,750,50)

print(d1 + d2)

print(d1 - d2)