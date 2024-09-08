# Программа для перевода координат

## Пример работы программы
```
Введите координату по x: 5
Введите координату по y: 3
Введите координату по z: 3
Введите нужную точность: 2
Сферические координаты: r = 6.56, θ = 62.77°, φ = 30.96°
Цилиндрические координаты: ρ = 5.83, φ = 30.96°, z = 3.0
```

## Описание

Данная программа выполняет перевод координат из декартовой системы в сферическую и цилиндрическую системы координат с заданной точностью. Пользователь вводит координаты $x$, $y$, $z$, а также точность (количество знаков после запятой), и программа выводит эквивалентные координаты в двух других системах.

### Сферическая система координат

Сферическая система координат представляет точку в пространстве с помощью трёх параметров:

- $r$ — радиальное расстояние (расстояние от начала координат до точки),
- $\theta$ — зенитный угол (угол между вектором $\vec{P}$ и осью $Oz$),
- $\phi$ — азимутный угол (угол между проекцией вектора $\vec{P}$ на плоскость $Oxy$ и осью $Ox$).

Формулы для преобразования декартовых координат $(x, y, z)$ в сферические координаты $(r, \theta, \phi)$:

- $r = \sqrt{x^2 + y^2 + z^2}$
- $\theta =  \arccos(\frac{z}{r})$, если $r \neq 0$ 
- $\phi = \arctan(\frac{y}{x})$

### Цилиндрическая система координат

Цилиндрическая система координат использует три переменные:

- $\rho$ — радиальная координата (расстояние от оси $Oz$),
- $\phi$ — азимутный угол (угол между проекцией вектора $\vec{P}$ на плоскость $Oxy$ и осью $Ox$),
- $z$ — вертикальная координата (высота точки над плоскостью $xy$).

Формулы для преобразования декартовых координат $(x, y, z)$ в цилиндрические координаты $(\rho, \phi, z)$:

- $\rho = \sqrt{x^2 + y^2}$
- $\phi = \arctan(\frac{y}{x})$
- $z = z$

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
