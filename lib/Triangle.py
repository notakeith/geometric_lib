class Triangle():
    """
    Класс треугольника
    """
    def __init__(self, a:int=0,b:int=0,c:int=0,h:int=0):
        if a > 0 and b > 0 and c > 0 and h > 0:
            self.a = a
            self.b = b
            self.c = c
            self.h = h
        else: raise ValueError

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