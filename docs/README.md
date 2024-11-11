# Математические формулы

Проект реализует набор классов для вычисления площади и периметра геометрических фигур: круга, прямоугольника, квадрата и треугольника. Каждый класс содержит методы для расчета площади и периметра на основе стандартных математических формул. Проект спроектирован с упором на простоту и эффективность, предлагая чистый объектно-ориентированный код для базовых геометрических расчетов.

## Классы и методы

### Класс: `Circle` (Круг)

- **Формула для площади:**  
  $( S = \pi R^2 )$
  
- **Формула для периметра:**  
  $( P = 2\pi R )$

#### Методы:

- `area()`:  
  Вычисляет и возвращает площадь круга.
  
  Пример:
  ```python
  c = Circle(5)
  print(c.area())  # Вывод: 78.53981633974483
  ```

- `perimeter()`:  
  Вычисляет и возвращает периметр (окружность) круга.
  
  Пример:
  ```python
  c = Circle(5)
  print(c.perimeter())  # Вывод: 31.41592653589793
  ```

---

### Класс: `Rectangle` (Прямоугольник)

- **Формула для площади:**  
  $( S = a \times b )$
  
- **Формула для периметра:**  
  $( P = 2a + 2b )$

#### Методы:

- `area()`:  
  Вычисляет и возвращает площадь прямоугольника.
  
  Пример:
  ```python
  r = Rectangle(4, 6)
  print(r.area())  # Вывод: 24
  ```

- `perimeter()`:  
  Вычисляет и возвращает периметр прямоугольника.
  
  Пример:
  ```python
  r = Rectangle(4, 6)
  print(r.perimeter())  # Вывод: 20
  ```

---

### Класс: `Square` (Квадрат)

- **Формула для площади:**  
  $( S = a^2 )$
  
- **Формула для периметра:**  
  $( P = 4a )$

#### Методы:

- `area()`:  
  Вычисляет и возвращает площадь квадрата.
  
  Пример:
  ```python
  s = Square(5)
  print(s.area())  # Вывод: 25
  ```

- `perimeter()`:  
  Вычисляет и возвращает периметр квадрата.
  
  Пример:
  ```python
  s = Square(5)
  print(s.perimeter())  # Вывод: 20
  ```

---

### Класс: `Triangle` (Треугольник)

- **Формула для площади:**  
  $( S = \frac{1}{2} \times a \times h )$

- **Формула для периметра:**  
  $( P = a + b + c )$

#### Методы:

- `area()`:  
  Вычисляет и возвращает площадь треугольника (основание (a), высота (h)).
  
  Пример:
  ```python
  t = Triangle(4, 5, 3, 6)
  print(t.area())  # Вывод
  ```
- `perimeter()`:  
  Вычисляет и возвращает периметр треугольника.
  
  Пример:
  ```python
  t = Triangle(4, 5, 3, 6)
  print(t.perimetr())  # Вывод

  ```

## Тестирование

### Тест-кейсы

1. **Корректные данные**
    - Проверка работы методов при корректных входных значениях.

2. **Некорректные данные**
    - Отрицательные значения.
    - Некорректные типы данных (например, строки вместо чисел).

### Ожидаемые результаты

- **Для корректных данных:** методы должны возвращать точные значения площади и периметра.
- **Для некорректных данных:** методы должны возвращать ошибку (например, выброс исключения `ValueError` для отрицательных чисел) или давать корректное обработанное значение, если такие значения предусмотрены.

### Отчёт

| Тест-кейс | Описание теста                                               | Ожидаемый результат         | Фактический результат | Дата       | Вердикт |
|-----------|--------------------------------------------------------------|-----------------------------|-----------------------|------------|---------|
| TC1       | Circle.area() с радиусом 5                                   | Площадь ≈ 78.54             | 78.53981633974483     | 11.11.2024 | Ок      |
| TC2       | Circle.area() с отрицательным радиусом -3                    | Выброс `ValueError`         | `ValueError`          | 11.11.2024 | Ок      |
| TC3       | Rectangle.perimeter() с длиной 2_000_000 и шириной 2_000_000 | Периметр = 8_000_000        | 8_000_000             | 11.11.2024 | Ок      |
| TC4       | Rectangle.perimeter() с некорректным параметром "a"          | Выброс `ValueError`         | `ValueError`          | 11.11.2024 | Ок      |
| TC5       | Square.area() с длиной стороны 1_000_000                     | Площадь = 1_000_000_000_000 | 1_000_000_000_000     | 11.11.2024 | Ок      |
| TC6       | Triangle.area() с отрицательной стороной -5                  | Выброс `ValueError`         | `ValueError`          | 11.11.2024 | Ок      |


## История коммитов

- commit 8db7c68cadd5fccfc309c8bdba1c776995d35826 (HEAD -> labwork3_471843, origin/labwork3_471843)
Author: ngleym <ngleym@ya.ru>
Date:   Mon Nov 11 05:37:03 2024 +0300
 
     **updated README.md**
 
- commit b44cbb67bbc98a3638b5a7416800e463a275e975
Author: ngleym <ngleym@ya.ru>
Date:   Mon Nov 11 05:35:10 2024 +0300

    **added unittests**

- commit 0ea791157e59c1af4a45c56a4da7db6306abd402
Author: ngleym <ngleym@ya.ru>
Date:   Mon Nov 11 05:34:59 2024 +0300

    **main packages update**

- commit dafeeca13f06315247999947d4731a7282e95d8f
Author: ngleym <ngleym@ya.ru>
Date:   Mon Nov 11 05:33:39 2024 +0300

    **add __init__.py**

- commit 1de1c8b170b68d8ca6eb0cc6892b40aa407ae580
Author: ngleym <ngleym@ya.ru>
Date:   Mon Nov 11 05:33:21 2024 +0300

    **renamed main class packages**

- commit 29b74a3c167d52429b72b6846f77b21c351a61be
Author: ngleym <ngleym@ya.ru>
Date:   Mon Nov 11 05:32:44 2024 +0300

    **moved main class packages to separate lib folder**

- commit 6887d0f34a9b7dd426d99c6371a335db9a7365cf (origin/main, origin/HEAD, main)
Author: ngleym <ngleym@ya.ru>
Date:   Wed Oct 2 08:45:51 2024 +0300

    **modified file rectangle.py**

- commit db489e59fa67a1e1d544b275e93cab42d214736c
Author: ngleym <ngleym@ya.ru>
Date:   Wed Oct 2 08:44:35 2024 +0300

    **added new file triangle.py**

- commit 1fef517f6c31f2b3aaab9f806b94c7f262973717
Author: ngleym <ngleym@ya.ru>
Date:   Wed Oct 2 08:43:43 2024 +0300

    **added new file rectangle.py**

- commit e047342a80235e63ef3e3ee53fa389d2ebb6923b
Author: Nikita <108391756+notakeith@users.noreply.github.com>
Date:   Fri Oct 18 08:41:19 2024 +0300

    **Update README.md**

- commit 25d93106412cb6994ee4d8163696b0e1a2ef4842
Author: ngleym <ngleym@ya.ru>
Date:   Fri Oct 18 05:55:36 2024 +0300

    **documentation added**

- commit 4e6b714f4a0947f36e7a4df849ad744c8d13b823
Author: ngleym <ngleym@ya.ru>
Date:   Fri Sep 20 09:23:59 2024 +0300
 
     **added new folder geometric_lib**