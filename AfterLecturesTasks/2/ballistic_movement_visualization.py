import numpy as np
import matplotlib.pyplot as plt
import argparse

g = 9.81


def parse_arguments():
    parser = argparse.ArgumentParser(description='Симуляция движения тела, брошенного под углом.')
    parser.add_argument('height', type=float, help='Высота, с которой брошено тело (м)')
    parser.add_argument('speed', type=float, help='Начальная скорость (м/с)')
    parser.add_argument('angle', type=float, help='Угол броска (в градусах)')

    return parser.parse_args()

def get_user_input():
    height = float(input("Введите высоту, с которой брошено тело (м): "))
    speed = float(input("Введите начальную скорость (м/с): "))
    angle = float(input("Введите угол броска (в градусах): "))
    return height, speed, angle


def calculate_trajectory(h, v0, angle):
    angle = np.radians(angle)

    vx_start = v0 * np.cos(angle)
    vy_start = v0 * np.sin(angle)

    t_flight = (vy_start + np.sqrt(vy_start**2 + 2 * g * h)) / g
    t = np.linspace(0, t_flight, num=500)

    x = vx_start * t
    y = h + vy_start * t - 0.5 * g * t**2

    vx = vx_start * np.ones_like(t)
    vy = vy_start - g * t

    v = np.sqrt(vx**2 + vy**2)

    return t, x, y, v, vx, vy

def plot_graphs(t, x, y, v, vx, vy):
    plt.figure(figsize=(15, 10))

    # График x(t) и y(t)
    plt.subplot(2, 2, 1)
    plt.plot(t, x, label="Горизонтальная координата (x)", color='b')
    plt.plot(t, y, label="Вертикальная координата (y)", color='r')
    plt.title("Зависимость координат от времени")
    plt.xlabel("Время (с)")
    plt.ylabel("Координаты (м)")
    plt.legend()
    plt.grid(True)

    # График траектории (x, y)
    plt.subplot(2, 2, 2)
    plt.plot(x, y, label="Траектория", color='g', linestyle='--')
    plt.title("Траектория движения тела")
    plt.xlabel("Горизонтальная координата (м)")
    plt.ylabel("Вертикальная координата (м)")
    plt.grid(True)

    # График v(t)
    plt.subplot(2, 2, 3)
    plt.plot(t, v, label="Скорость (м/с)", color='purple')
    plt.title("Зависимость скорости от времени")
    plt.xlabel("Время (с)")
    plt.ylabel("Скорость (м/с)")
    plt.grid(True)

    # График vx(t) и vy(t)
    plt.subplot(2, 2, 4)
    plt.plot(t, vx, label="Горизонтальная скорость (vx)", color='orange')
    plt.plot(t, vy, label="Вертикальная скорость (vy)", color='cyan')
    plt.title("Зависимость скоростей от времени")
    plt.xlabel("Время (с)")
    plt.ylabel("Скорости (м/с)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()



def main():
    height, speed, angle = get_user_input()
    t, x, y, v, vx, vy = calculate_trajectory(height, speed, angle)
    plot_graphs(t, x, y, v, vx, vy)

main()
