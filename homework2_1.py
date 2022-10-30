import typing
class Dict:
    description = "Work with dictionaries"

    def __init__(self, string, dict, empty_string, dups):
        self.string_name = string
        self.dict_name = empty_string
        self.dict_ = dict
        self.dups = dups

    def convertation(self):
        for i in self.string_name:
            if i not in self.dict_name:
                self.dict_name[i] = 1
        print(self.dict_name)


    def without_duplicates(self):
        for key, value in self.dups.items():
            if value not in self.dict_name.values():
                self.dict_name[key] = value
        print(self.dict_name)



    def highest(self):
        for i in self.dict_:
            dict_2 = self.dict_[i]
            if dict_2 > 13:
                return i


convert_ = Dict("python", {}, {}, {})
duplicates = Dict({}, {}, {}, {"BMW": "m6", "Mercedes": "cls", "Ford": "F150", "BMW": "m6"})
highest_dict = Dict({}, {"num_1": 10, "num_2": 21, "num_3": 13, "num_4": 32, "num_5": 40}, {}, {})

Dict.convertation(convert_)
Dict.without_duplicates(duplicates)
Dict.highest(highest_dict)





class Circle:

     def __init__(self, p, radius):
         self.p = p
         self.r = radius

     def area_of_circle(self) -> typing.Union[int, float]:
         return self.p * self.r**2

     def perimeter_of_circle(self) -> typing.Union[int, float]:
         return 2 * self.p * self.r


area_perimeter = Circle(3.14, 20)

print("The area of circle will be: ", area_perimeter.area_of_circle())
print("The perimeter of circle will be: ", area_perimeter.perimeter_of_circle())