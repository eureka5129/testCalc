
class calcFunc():
    total = None

    def __init__(self):
        self.total = 0

    def addition(self,val):
        self.total = self.total + int(val)
        return self.total
    def subtraction(self,val):
        self.total = self.total - int(val)
        return self.total
    def multiplication(self,val):
        self.total = self.total * int(val)
        return self.total
    def division(self,val):
        self.total = self.total / int(val)
        return self.total
