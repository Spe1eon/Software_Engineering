import math
import matplotlib.pyplot as plt
import numpy as np

def is_lying(k, b):
  #проверка принадлежности прямой горизонтальной границе прямоугольника
  if(math.isclose(k, 0, rel_tol = 1e-9)):
      if(math.isclose(b, 3, rel_tol = 1e-9) or math.isclose(b, 4, rel_tol = 1e-9)):
        return True
      else:
        return False
      
def is_intersecting(k, b):
  #проверка пересечения прямой с горизонтальными границами прямоугольника
  y1 = k * 1 + b
  y2 = k * 2 + b

  if (math.isclose(y1, 3, rel_tol = 1e-9) and math.isclose(y2, 4, rel_tol = 1e-9)) or \
      (math.isclose(y2, 3, rel_tol = 1e-9) and math.isclose(y1, 4, rel_tol = 1e-9)):
      return True
  elif (math.isclose(k, 0, rel_tol = 1e-9) and 3 <= b <= 4):
    return True
  else:
      return False
  
def count_intersection_points(k, b):
  count = 0 #количество точек пересечения

  #Если k == 0, то линия паралельна горизонтальным граням
  if(k == 0):
    if(b < 4 and b > 3):
      count = 2
    else:
      count = 0
  else:
    #проверка пересечения прямой с вертикальными границами прямоугольника
    x1 = (3 - b) / k
    x2 = (4 - b) / k
    if x1 is not None and 1 < x1 < 2:
        count += 1
    if x2 is not None and 1 < x2 < 2:
        count += 1
    #проверка пересечения прямой с горизонтальными границами прямоугольника
    y1 = k * 1 + b
    y2 = k * 2 + b
    if y1 is not None and 3 <= y1 <= 4:
        count += 1
    if y2 is not None and 3 <= y2 <= 4:
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
if is_lying(k, b):
  plt.title(f"Горизонтальная граница прямоугольника лежит в прямой")
  print("\nГоризонтальная граница прямоугольника лежит в прямой")
else:
  intersection_count = count_intersection_points(k, b)
  if intersection_count > 0:
      plt.title(f"Количество точек пересечения: {intersection_count}")
      print("\nКоличество точек пересечения:", intersection_count)
  else:
      plt.title("Прямая не пересекается с прямоугольником")
      print("\nПрямая не пересекается с прямоугольником")

plt.legend()
plt.grid(True)
plt.show()





