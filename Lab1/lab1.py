from math import isclose
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def func (a, x, b):
    return a*x + b

def main ():
    x1 = 1
    x2 = 4
    y1 = func(1, x1, 0)
    y2 = func(1, x2, 0)

    x_min = 1
    x_max = 3
    y_min = 2
    y_max = 4

    line = (x1, y1, x2, y2)
    rectangle = (x_min, y_min, x_max, y_max)
    print("line:", line, "rectangle:", rectangle) 
    # if x1 < x_min and x2 < x_min:
    #     return False
    # if x1 > x_max and x2 > x_max:
    #     return False
    # if y1 < y_min and y2 < y_max:
    #     return False
    # if y1 > y_min and y2 > y_max:
    #     return False
    
    # if x1 >= x_min and x2 <= x_max and y1 >= y_min and y2 <= y_max:
    #     return True

if __name__ == '__main__':
    main()

    
    #y = list(map(f, x))


     #for i in range(len(x)):
    #    y = func(a, x[i], b)
    #    list.append(y)
    #    print("x =", x[i], "y =", y)
    #    i += 1


    #fig, ax = plt.subplots()
    #ax.plot([0, 10],[0, 10])
    #ax.add_patch (Rectangle((1, 2), 2, 2))
    #plt.show()