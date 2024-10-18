class Square():
    """
    Класс квадрата
    """
    def __init__(self, a):
        self.a = a
    def area(self) -> float:
        """
        Принимает сторону квадрата a, возвращаёт его площадь.

        Code example:

        >>> s = Square(3)
        >>> print(s.area())
        9

        Параметры:
            a (float) сторона квадрата

        Возвращаемое значение:
            area (float) площадь квадрата
        """
        return self.a * self.a


    def perimeter(self) -> float:
        """
        Принимает сторону квадрата a, возвращаёт его площадь.

        Code example:

        >>> s = Square(3)
        >>> print(s.perimeter())
        12

        Параметры:
            a (float) сторона квадрата

        Возвращаемое значение:
            perimeter (float) периметр квадрата
        """
        return 4 * self.a