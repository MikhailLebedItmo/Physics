
# Программа для перевода координат

## Описание

Данная программа выполняет перевод координат из декартовой системы в сферическую и цилиндрическую системы координат с заданной точностью. Пользователь вводит координаты \( x \), \( y \), \( z \), а также точность (количество знаков после запятой), и программа выводит эквивалентные координаты в двух других системах.

### Сферическая система координат

Сферическая система координат представляет точку в пространстве с помощью трёх параметров:

- \( r \) — радиус-вектор (расстояние от начала координат до точки),
- \( 	heta \) — азимутальный угол (угол между проекцией вектора на плоскость \( xy \) и осью \( x \)),
- \( \phi \) — полярный угол (угол между вектором и осью \( z \)).

Формулы для преобразования декартовых координат \( (x, y, z) \) в сферические координаты \( (r, 	heta, \phi) \):

- \( r = \sqrt{x^2 + y^2 + z^2} \)
- \( 	heta = rctan{\left(rac{y}{x}ight)} \)
- \( \phi = rccos{\left(rac{z}{r}ight)} \) (если \( r 
eq 0 \))

### Цилиндрическая система координат

Цилиндрическая система координат использует три переменные:

- \( ho \) — радиальная координата (расстояние от оси \( z \)),
- \( \phi \) — азимутальный угол (угол между проекцией вектора на плоскость \( xy \) и осью \( x \)),
- \( z \) — вертикальная координата (высота точки над плоскостью \( xy \)).

Формулы для преобразования декартовых координат \( (x, y, z) \) в цилиндрические координаты \( (ho, \phi, z) \):

- \( ho = \sqrt{x^2 + y^2} \)
- \( \phi = rctan{\left(rac{y}{x}ight)} \)
- \( z = z \)

## Код программы

```python
import math

def cartesian_to_spherical(x, y, z, precision):
    r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    theta = math.atan2(y, x)
    phi = math.acos(z / r) if r != 0 else 0
    if precision == 0:
        return int(round(r, 0)), int(round(math.degrees(theta), 0)), int(round(math.degrees(phi), 0))

    return round(r, precision), round(math.degrees(theta), precision), round(math.degrees(phi), precision)

def cartesian_to_cylindrical(x, y, z, precision):
    rho = math.sqrt(x ** 2 + y ** 2)
    phi = math.atan2(y, x)
    if precision == 0:
        return int(round(rho, 0)), int(round(math.degrees(phi), 0)), int(round(z, 0))

    return round(rho, precision), round(math.degrees(phi), precision), round(z, precision)

def main():
    while True:
        x = float(input("Введите координату по x: "))
        y = float(input("Введите координату по y: "))
        z = float(input("Введите координату по z: "))
        precision = int(input("Введите нужную точность: "))

        print("Сферические координаты: r = {}, θ = {}°, φ = {}°".format(*cartesian_to_spherical(x, y, z, precision)))
        print("Цилиндрические координаты: ρ = {}, φ = {}°, z = {}".format(*cartesian_to_cylindrical(x, y, z, precision)))

main()
```
