class Triangle():
    """
    Класс треугольника
    """
    def __init__(self, a=0,b=0,c=0,h=0):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def area(self) -> float:
        """
        Принимает сторону треугольника a и высоту h, возвращаёт его площадь.

        Code example:

        >>> t = Triangle(a=3,h=2)
        >>> print(t.area())
        3.0

        Параметры:
            a (float) сторона треугольника
            h (float) высота треугольника

        Возвращаемое значение:
            area (float) площадь треугольника
        """
        return self.a * self.h / 2


    def perimeter(self) -> float:
        """
        Принимает стороны треугольника a,b,c, возвращаёт его периметр.

        Code example:

        >>> t = Triangle(a=1,b=2,c=3)
        >>> print(t.perimeter())
        6

        Параметры:
            a (float) 1-ая сторона треугольника
            b (float) 2-ая сторона треугольника
            c (float) 3-ья сторона треугольника

        Возвращаемое значение:
            perimetr (float) периметр треугольника
        """
        return self.a + self.b + self.c