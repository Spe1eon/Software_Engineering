def calculating_area(vertices):
    n = len(vertices)
    area = 0
    
    if n < 3:
        raise ValueError("Многоугольник должен иметь не менее трех вершин.")

    # Вычисление площади по формуле Гаусса
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)

    area = abs(area) / 2.0
    return area

vertices = [(0, 0), (3, 0), (3, 4), (0, 4)]
result = calculating_area(vertices)
print(f"Площадь многоугольника: {result}")
