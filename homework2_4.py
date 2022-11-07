class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sorted_tuple(self):
        return sorted((self.a, self.b, self.c))

    def __eq__(self, other):
        first = self.sorted_tuple()
        second = other.sorted_tuple()

        for i in range(3):
            if first[i] != second[i]:
                return False

        return True

    def perimeter(self):
        return self.a + self.b + self.c

    def area_of_triangle(self):
        half_p = self.perimeter() / 2
        area = (half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c)) ** 0.5

        return area


triangle_1 = Triangle(5, 8, 7)
triangle_2 = Triangle(7, 5, 8)

print(Triangle.__eq__(triangle_1, triangle_2))
print(Triangle.perimeter(triangle_1))
print(Triangle.perimeter(triangle_2))
print(Triangle.area_of_triangle(triangle_1))
print(Triangle.area_of_triangle(triangle_2))


class Rectangular:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sorted_rects(self):
        return sorted((self.a, self.b))

    def __eq__(self, other):
        first_rect = self.sorted_rects()
        second_rect = other.sorted_rects()

        for i in range(2):
            if first_rect[i] == second_rect[i]:
                return True

        return False

    def __gt__(self, other):
        first_rect = self.sorted_rects()
        second_rect = other.sorted_rects()

        for i in range(2):
            if first_rect[i] > second_rect[i]:
                return True

        return False


rect_1 = Rectangular(7, 10)
rect_2 = Rectangular(8, 6)

print(rect_1.__eq__(rect_2))
print(rect_1.__gt__(rect_2))
