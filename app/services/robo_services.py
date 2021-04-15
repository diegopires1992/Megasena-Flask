from time import sleep
from selenium import webdriver



class RobotMegaSena():

    url = "https://www.google.com/search?q=caixa+mega+sena"
    driver = webdriver.Firefox()

    def __init__(self):
        self.url = self.url
        self.driver = self.driver
        self.number = "UHlKbe"
    
    def navigate(self):
        self.driver.get(self.url)

    def _get_box(self):
        return self.driver.find_elements_by_class_name(self.number)
    
    def get_all_number(self):
        boxes = self._get_box()
        return [int(box.text) for box in boxes]



# teste = RobotMegaSena()
# teste.navigate()
# resultado = teste.get_all_number()
# print(resultado)