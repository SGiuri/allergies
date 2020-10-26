from math import log2

class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergenes_codes = self.find_list_of_2_power()
        self.allergenes = {
            1: "eggs",
            2: "peanuts",
            4: "shellfish",
            8: "strawberries",
            16: "tomatoes",
            32: "chocolate",
            64: "pollen",
            128: "cats"}

        pass

    def allergic_to(self, item):
        if item in self.lst:
            return True
        return False

        pass

    @property
    def lst(self):
        my_list = []
        for k in self.allergenes_codes:
            if k in self.allergenes.keys():
                my_list.append(self.allergenes[k])
        return my_list

        pass

    def find_list_of_2_power(self):
        if self.score == 0:
            return []
        powers_of_two = [2 ** n for n in range(int(log2(self.score)), -1, -1)]
        copy_of_score = self.score
        my_list_of_powers = []
        for power_of_two in powers_of_two:
            if copy_of_score >= power_of_two:
                copy_of_score -= power_of_two
                my_list_of_powers.append(power_of_two)

        return my_list_of_powers
