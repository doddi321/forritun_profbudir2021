from typing import TextIO


class Distribution:
    def __init__(self, file_obj: TextIO = None) -> None:
        if file_obj:
            dictionary = self.__get_dictionary_from_file(file_obj)
            self.set_distribution(dictionary)
        else:
            self.set_distribution({})        

    def __get_dictionary_from_file(self, file_obj: TextIO) -> dict:
        dictionary = {}
        for line in file_obj:
            for nr_str in line.split():
                nr = int(nr_str)
                dictionary[nr] = dictionary.get(nr, 0) + 1
        return dictionary

    def set_distribution(self, distribution: dict):
        self.__distribution = distribution
    
    def __get_total(self):
        total = 0 
        for key, value in self.__distribution.items():
            total += key * value 

        # return sum(key * value for key, value in self.__distribution.items())
        return total

    def average(self):
        if (len(self.__distribution)) > 0:
            total = self.__get_total()
            return total / sum(self.__distribution.values())
        return 0

    def __str__(self) -> str:
        string = ''
        for key, value in sorted(self.__distribution.items()):
            string += f'{key}: {value}\n'
        return string

    def __ge__(self, other: "Distribution"):
        return self.average() >= other.average()

    def __add_dictionary(self, dictionary: dict):
        for key, value in dictionary.items():
            self.__distribution[key] = self.__distribution.get(key, 0) + value



    def __add__(self, other: "Distribution"):
        new_dictionary = self.__distribution.copy()
        distribution = Distribution()
        distribution.set_distribution(new_dictionary)
        distribution.__add_dictionary(other.__distribution)
        return distribution 
        