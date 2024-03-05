import math

class Polynomial:
    def __init__(self, degree, coef):
        if not isinstance(degree, int) or degree < 0:
            raise ValueError("Степень многочлена должна быть неотрицательным целым числом.")
        if not isinstance(coef, list) or len(coef) != degree + 1:
            raise ValueError("Некорректные коэффициенты многочлена.")
        self.degree = degree
        self.coef = coef

    def derivative(self):
        new_coef = [i * self.coef[i] for i in range(1, self.degree + 1)]
        return Polynomial(self.degree - 1, new_coef)

    def antiderivative(self, const=0):
        new_coef = [const] + [self.coef[i] / (i + 1) for i in range(self.degree + 1)]
        return Polynomial(self.degree + 1, new_coef)

    def __str__(self):
        terms = [f"{self.coef[i]}x^{i}" for i in range(self.degree, 0, -1)] + [str(self.coef[0])]
        return " + ".join(terms)

    def __repr__(self):
        return f"Polynomial({self.degree}, {self.coef})"

class Vector:
    def __init__(self, x, y, z):
        if not all(isinstance(coord, (int, float)) for coord in [x, y, z]):
            raise TypeError("Координаты вектора должны быть числами.")
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __rmul__(self, scalar):
        return Vector(scalar * self.x, scalar * self.y, scalar * self.z)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

degree = 3
coef = [6, 1, 3, 2]
poly = Polynomial(degree, coef)

vec1 = Vector(1, 2, 3)
vec2 = Vector(4, 5, 6)

print("Class Polynomial:\nМногочлен:", poly, 
      "\nПроизводная:", poly.derivative(), 
      "\nПервообразная:", poly.antiderivative(5))

print("\nClass Vector:\nВектор 1:", vec1, 
      "\nВектор 2:", vec2, 
      "\nВектор 1 == Вектор 2:", vec1 == vec2, 
      "\nСумма векторов:", vec1 + vec2, 
      "\nРазность векторов:", vec1 - vec2, 
      "\nУмножение вектора на число:", 2 * vec1, 
      "\nМодуль вектора 1:", vec1.magnitude())

