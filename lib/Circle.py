import math

from numpy.f2py.auxfuncs import throw_error


class Circle():
    """
    Класс окружности
    """
    def __init__(self, radius: int):
        if radius > 0:
            self.radius = radius
        else: raise ValueError
    def area(self) -> float:
        """
        Принимает радиус r окружности, возвращаёт её площадь.

        Code Example:

        >>> c = Circle(16)
        >>> print(c.area())
        804.247719318987

        Параметры:
            r (float) радиус окружности

        Возвращаемое значение:
            area (float) площадь окружности
        """
        return math.pi * self.radius * self.radius

    def perimeter(self) -> float:
        """
        Принимает радиус r окружности, возвращаёт её периметр.

        Code example:

        >>> c = Circle(16)
        >>> print(c.perimeter())
        100.53096491487338

        Параметры:
            r (float) радиус окружности

        Возвращаемое значение:
            perimeter (float) периметр окружности
        """
        return 2 * math.pi * self.radius