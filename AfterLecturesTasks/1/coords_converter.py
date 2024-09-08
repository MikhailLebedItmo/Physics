import math


def cartesian_to_spherical(x, y, z, precision):
    r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    phi = math.atan2(y, x)
    theta = math.acos(z / r) if r != 0 else 0
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
