
class DataConvert():

    def __init__(self,data_mega_sena):
        self.data_mega_sena = data_mega_sena    
    
    def convert(self):
        result_convert = [result.games_played.replace("{","").replace("}","").replace(","," ") for result in self.data_mega_sena]
        result_new = []
        for number_string in result_convert[-1:][0].split():
            result_new.append(int(number_string))
        return result_new