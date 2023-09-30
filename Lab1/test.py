import math
import matplotlib.pyplot as plt
import numpy as np

def is_intersecting(k, b):
    #проверка пересечения прямой с горизонтальными границами прямоугольника
    y1 = k * 1 + b
    y2 = k * 2 + b

    if (math.isclose(y1, 3, rel_tol = 1e-9) and math.isclose(y2, 4, rel_tol = 1e-9)) or \
       (math.isclose(y2, 3, rel_tol = 1e-9) and math.isclose(y1, 4, rel_tol = 1e-9)):
        return True
    else:
        return False

def count_intersection_points(k, b):
    count = 0 #количество точек пересечения

    #проверка пересечения прямой с вертикальными границами прямоугольника
    x1 = (3 - b) / k if k != 0 else None
    x2 = (4 - b) / k if k != 0 else None

    if x1 is not None and 1 <= x1 <= 2:
        count += 1

    if x2 is not None and 1 <= x2 <= 2:
        count += 1

    return count

#ввод коэффициентов k и b
k = float(input("Введите значение k: "))
b = float(input("Введите значение b: "))

#создание массива значений x для построения графика прямой
x = np.linspace(0, 3, 400)
y = k * x + b

#построение графика прямой
plt.plot(x, y, label = f'y = {k}x + {b}', color = 'blue')

#построение прямоугольника
plt.fill([1, 2, 2, 1], [3, 3, 4, 4], 'r', alpha = 0.3, label = 'Прямоугольник [1, 2] x [3, 4]')

#установка оси и меток
plt.xlim(0, 3)
plt.ylim(0, 7)
plt.xlabel('x')
plt.ylabel('y')

#проверка на пересечение и колличества точек пересечения
if is_intersecting(k, b):
    intersection_count = count_intersection_points(k, b)
    plt.title(f"Количество точек пересечения: {intersection_count}")
    print("\nКоличество точек пересечения:", intersection_count)
else:
    plt.title("Прямая не пересекается с прямоугольником")
    print("\nПрямая не пересекается с прямоугольником")

plt.legend()
plt.grid(True)
plt.show()





