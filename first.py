# class Car:
#     description = "This is car class"
#
#     def __init__(self, name, year, colour):
#         self.car_name = name
#         self.car_year = year
#         self.car_colour = colour
#
#
#
#     def present(self):
#         print(f"This is {self.car_name} {self.car_colour} car produced in {self.car_year}")
#
#     def get_age(self, current_year):
#         return current_year - self.car_year
#
#     def set_year(self, new_year):
#         if type(new_year) is int:
#             self.car_year = new_year
#         else:
#             raise ValueError("Wrong value for car_year")
#
# car_1 = Car(name = "Masseratti", year = 2019, colour = "Black")
# #or
# car_1 = Car("Masseratti", 2019, "Black")
#
# car_2 = Car(name = "Mercedes", year = 2022, colour = "White")
# car_3 = Car(name = "Toyota", year = 2022, colour = "Red")
#
# car_1.present()
# #or
# Car.present(car_1)
# car_2.present()
# car_3.present()
#
# print(car_1.get_age(2022))
#
# car_1.set_year(1800)
# print(car_1.get_age(2022))
#
#
#
# print(car_1.car_name, car_1.car_year, car_1.car_colour)
# print(car_2.car_name, car_2.car_year, car_2.car_colour)
#
# #••••••••••••••
# class Cv:
#     description = "This is CV"
#
#     def __init__(self, name, surname, email, age):
#         self.cv_name = name
#         self.cv_surname = surname
#         self.cv_email = email
#         self.cv_age = age
#
#
# cv_1 = Cv(name="Mihran", surname="Demirchian", email="mirdem@gmail.com", age="19")
#
# print(cv_1.cv_name, cv_1.cv_surname, cv_1.cv_email, cv_1.cv_age, sep="\n")
#
# #•••••••••••••
# class Rectangle:
#
#     def __init__(self, a, b):
#         self.rect_a = a
#         self.rect_b = b
#
#     def get_area(self):
#          return self.rect_a * self.rect_b
#     def get_parametre(self):
#         return self.rect_a * 2 + self.rect_b * 2
#
#
# rectangle_1 = Rectangle(2, 4)
#
# print(rectangle_1.get_area())
# print(rectangle_1.get_parametre())
#
#
# #••••••••••••
#
# class Shoes:
#     description = "These are shoes"
#
#     def present(self):
#         print(f"These are {self.shoes_type}, in {self.shoes_colour} colour and they cost {self.shoes_price}")
#
#
#     def __init__(self, type, colour, price):
#         self.shoes_type = type
#         self.shoes_colour = colour
#         self.shoes_price = price
#
#
# shoes_1 = Shoes(type="Derby", colour="Black", price=1000)
# shoes_2 = Shoes(type="Oxford", colour="Grey", price=950)
#
# shoes_1.present()
#
#
# #•••••••••••
# class Car:
#     description = "This is a car"
#
#     def __init__(self, name, year, colour, hp):
#         self.car_name = name
#         self.car_year = year
#         self.car_colour = colour
#         self.car_hp = hp
#
#     def present(self):
#         print(f"Your car is {self.car_colour} {self.car_name}, which was realised in {self.car_year} and has {self.car_hp} hp")
#
# car_1 = Car(name="Rolce Royce culinan", year=2021, colour="Black Metallic", hp=468)
#
# car_1.present()
#
#
# #••••••••••••••
#
# class Fruit:
#
#     description = "These are fruits"
#
#     def __init__(self, name, colour, price, kg):
#         self.fruit_name = name
#         self.fruit_colour = colour
#         self.price_kg = price
#         self.fruit_kg = kg
#     def present(self):
#         print(f"You have chosen {self.fruit_kg}kg of {self.fruit_colour} {self.fruit_name}")
#
#     def get_price(self):
#         return self.fruit_kg * self.price_kg
#
#
# fruit_ = Fruit(name="Apple", colour="red", price=230 , kg=3)
#
#
# fruit_.present()
# print("And they will cost --> ", fruit_.get_price())


#•••••••••••••

# class Dict:
#     description = "Convertation of string"
#
#     def __init__(self, string, dict_of_string):
#         self.string_name = string
#         self.dict_name = dict_of_string
#
#     def convertation(self) -> dict:
#         for i in self.string_name:
#             if i not in self.dict_name:
#                 self.dict_name[i] = 1
#             else:
#                 self.dict_name[i] += 1
#         print(self.dict_name)
#
# convert_ = Dict(string="python", dict_of_string={})
#
#
# convert_.convertation()











