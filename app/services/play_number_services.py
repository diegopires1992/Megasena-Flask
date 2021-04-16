import random 

class PlayNumber():
    def __init__(self,quantity_number):
        self.quantity = quantity_number
    
    def numbers(self):
        return random.sample(range(1,60), self.quantity)