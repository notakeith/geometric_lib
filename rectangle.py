class Rectangle():
    """
    Класс прямоугольника
    """
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def area(self) -> float:
        """
        Принимает стороны прямоугольника a и b, возвращаёт его площадь.

        Code example:

        >>> r = Rectangle(3,4)
        >>> print(r.area())
        12

        Параметры:
            a (float) первая сторона прямоугольника
            b (float) первая сторона прямоугольника

        Возвращаемое значение:
            area (float) площадь прямоугольника
        """
        return self.a * self.b

    def perimeter(self) -> float:
        """
        Принимает стороны прямоугольника a и b, возвращаёт его периметр.

        Code example:

        >>> r = Rectangle(3,4)
        >>> print(r.perimeter())
        14

        Параметры:
            a (float) первая сторона прямоугольника
            b (float) первая сторона прямоугольника

        Возвращаемое значение:
            perimeter (float) периметр прямоугольника
        """
        return 2*(self.a + self.b)
