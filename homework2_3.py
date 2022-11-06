# class Country:
#     def __init__(self, country_name, continent, *args, **kwargs):
#         self.country_name = country_name
#         self.continent = continent
#         super().__init__(*args, **kwargs)
#
#     def present(self):
#         return f"The country is {self.country_name} which is located in {self.continent}."
#
#
# class Brand:
#     def __init__(self, brand_name, date, *args, **kwargs):
#         self.brand_name = brand_name
#         self.date = date
#         super().__init__(*args, **kwargs)
#
#     def present(self):
#         return f"Brand is well-known {self.brand_name}, which has started its career in {self.date}."
#
#
# class Season:
#     def __init__(self, season_name, *args, **kwargs):
#         self.season_name = season_name
#         self.temperature = []
#         super().__init__(*args, **kwargs)
#
#     def add_of_temp(self, temp_1):
#         self.temperature.append(temp_1)
#
#     def avg_temperature(self):
#         average = sum(self.temperature) / len(self.temperature)
#         return average
#
#     def present(self):
#         return f"The most appropriate season is {self.season_name} and the average temperature " \
#                f"for {self.season_name} is {self.avg_temperature()}."
#
#
# class Product(Country, Brand, Season):
#     def __init__(self, product_name, product_type, product_price, *args, **kwargs):
#         self.product_name = product_name
#         self.product_type = product_type
#         self.product_price = product_price
#         super().__init__(*args, **kwargs)
#
#     def present(self):
#         print(f"{Country.present(self)} {Brand.present(self)} {Season.present(self)} "
#               f"We are introducing our new product which name is {self.product_name}, "
#               f"the type of our product is {self.product_type}"
#               f" and it costs {self.product_price}$")
#
#
# pr = Product(product_name="Belvin Calfskin Slipper", product_type="shoes", product_price=800, country_name="USA",
#              continent="North America", brand_name="Ralph Lauren", date=1967, season_name="Summer")
#
# pr.add_of_temp(30)
# pr.add_of_temp(33)
# pr.add_of_temp(28)
# pr.add_of_temp(40)
#
# print(Product.__mro__)
#
# pr.present()


class Hotel:
    def __init__(self, hotel_name, place, mid_room_price, luxe_room_price, *args, **kwargs):
        self.hotel_name = hotel_name
        self.place = place
        self.mid_room_price = mid_room_price
        self.luxe_room_price = luxe_room_price
        self.mid_rooms = {"room1": "free", "room2": "free", "room3": "free"}
        self.luxe_rooms = {"room1": "free", "room2": "free", "room3": "free"}
        super().__init__(*args, **kwargs)

    def available_rooms(self):
        check = True
        while check:
            for key, value in self.mid_rooms.items():
                if value == "free":
                    return "All the rooms are available!"
                else:
                    return "There are some not available rooms, sorry!"

    def room_booking(self):
        check = True
        while check:
            for key, value in self.mid_rooms.items():
                if value == "free":
                    return f"You have booked {key} of mid rooms"
            for key, value in self.luxe_rooms.items():
                if value == "free":
                    return f"You have booked {key} of luxe rooms"

    def present(self):
        return f"Our hotel is well-known {self.hotel_name} in {self.place}. As all hotels, we have both middle rooms " \
               f"and luxe rooms.\n For mid rooms you'll have to pay {self.mid_room_price}€ " \
               f"and for luxe rooms {self.luxe_room_price}€."


class Taxi:
    def __init__(self, taxi_name, car_types, price_for_tour, *args, **kwargs):
        self.taxi_name = taxi_name
        self.car_types = car_types
        self.price_for_tour = price_for_tour
        super().__init__(*args, **kwargs)

    def discount(self, percent):
        return self.price_for_tour - (self.price_for_tour * percent / 100)

    def present(self):
        return f"We offer you our taxi service {self.taxi_name}, cars of our service are {self.car_types}\n" \
               f"and price for trip will cost {self.price_for_tour}€." \
               f"And also here are discounts about 10% and after that your trip will cost {self.discount(percent=10)}"


class Tour(Hotel, Taxi):
    def __init__(self, tour_name, price_luxe, price_mid, *args, **kwargs):
        self.tour_name = tour_name
        self.price_luxe = price_luxe
        self.price_mid = price_mid
        super().__init__(*args, **kwargs)

    def for_all_luxe(self):
        self.price_luxe = self.luxe_room_price + self.price_for_tour
        return self.price_luxe

    def for_all_mid(self):
        self.price_mid = self.mid_room_price + self.price_for_tour
        return self.price_mid

    def present(self):
        print(f"{Hotel.present(self)}\n {Taxi.present(self)}\nAt the end i would like to mention that "
              f"for all luxe staff price is {self.for_all_luxe()}€ and for mid is {self.for_all_mid()}€, thank you "
              f"for choosing us!!!")


all_options = Tour(tour_name="Arctic ventures", price_luxe="", price_mid="", hotel_name="Alyeska Resort",
                   place="Alyeska", mid_room_price=250, luxe_room_price=400,
                   taxi_name="Boko", car_types="Volvo", price_for_tour=680)

all_options.present()
