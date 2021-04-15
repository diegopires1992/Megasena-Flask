from random import randint

class DrawNumber():
    def __init__(self,quantity_number):
        self.quantity = quantity_number
    

    def numbers(self):
        return [randint(1,60) for number in range(self.quantity)]



teste = DrawNumber(6)
retorno = teste.numbers()
print(retorno)