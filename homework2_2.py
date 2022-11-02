from datetime import datetime

time = datetime.now()
year = time.year


class Human(object):

    def __init__(self, name, surname, age, height, weight, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender

    def user_age(self):
        date = year + (100 - self.age)
        return date

    def present_m(self):
        print(f"Your name is {self.name} {self.surname}, {self.age}y.o, {self.gender}, {self.height}cm\n"
              f"your optimal weight is {self.men_optimal_weight()}kg and you will turn 100y.o in {self.user_age()}")

    def present_w(self):
        print(f"Your name is {self.name} {self.surname}, {self.age}y.o, {self.gender}, {self.height}cm"
              f"your optimal weight is {self.women_optimal_weight()}kg and you will turn 100y.o in {self.user_age()}")

    def men_optimal_weight(self):
        weight_m = 50 + (0.91 * (self.height - 152.4))
        return weight_m

    def women_optimal_weight(self):
        weight_w = 45.5 + (0.91 * (self.height - 152.4))
        return weight_w


class Student(Human):
    def __init__(self, st_name, st_surname, st_age, st_height, st_weight, st_gender):
        super().__init__(st_name, st_surname, st_age, st_height, st_weight, st_gender)
        self.marks = []

    def avg_marks(self):
        average = sum(self.marks) / len(self.marks)
        return average

    def add_mark(self, grade):
        self.marks.append(grade)

    def present(self):
        print(f"{super().present_m()}, my marks are {self.marks} and my average mark is {self.avg_marks()}")

user_1 = Student("Mihran", "Demirchyan", 19, 173, 72, "male")
user_2 = Student("Vanessa", "Grigoryan", 25, 158, 57, "female")
# user_1 = Human(input(""), input(""), int(input()), float(input()), int(input()), input()) kareli e naev senc

user_1.add_mark(7)
user_1.add_mark(10)
user_1.add_mark(9)
# print(user_1.marks)
user_2.add_mark(9)
user_2.add_mark(2)
user_2.add_mark(8)
user_2.add_mark(7)

user_1.present()
user_2.present()
