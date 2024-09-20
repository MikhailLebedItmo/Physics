import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation

matplotlib.use('TkAgg')

# Входные параметры
R = float(input("Введите радиус колеса: "))
v = float(input("Введите скорость центра масс колеса: "))  # скорость центра масс
T = 20  # продолжительность анимации в секундах
fps = 30  # количество кадров в секунду (Frames Per Second)

# Частота вращения колеса (v = omega * R -> omega = v / R)
omega = v / R

# Время моделирования (генерация последовательности времени)
frames = fps * T  # всего кадров
t = np.linspace(0, T, frames)


# Создание графика
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Одинаковые пропорции осей

# Настройки осей: график подлиннее, чтобы видеть полную траекторию
ax.set_xlim(0, v * T)
ax.set_ylim(0, R * 4)

# Линия для отображения траектории точки
line, = ax.plot([], [], lw=2)

# Колесо (круг)
wheel, = ax.plot([], [], 'b-', lw=2)

# Точка на ободе колеса
point, = ax.plot([], [], 'ro')

# Таймер
timer_text = ax.text(0.1, 0.7, '', transform=ax.transAxes, fontsize=12)


# Инициализация графика
def init():
    line.set_data([], [])
    wheel.set_data([], [])
    point.set_data([], [])
    return line, wheel, point


# Функция обновления положения колеса и точки на нём
def animate(i):
    wheel_center_x = v * t[i] + R
    wheel_center_y = R
    theta = np.linspace(0, 2 * np.pi, 100)
    wheel_x = wheel_center_x + R * np.cos(theta)
    wheel_y = wheel_center_y + R * np.sin(theta)
    x_cycloid = v * t[:i + 1] + R + R * np.sin(np.pi + omega * t[:i + 1])
    y_cycloid = R + R * np.cos(np.pi + omega * t[:i + 1])
    x_point, y_point = x_cycloid[-1], y_cycloid[-1]

    # Обновляем траекторию
    line.set_data(x_cycloid, y_cycloid)
    # Обновляем круг
    wheel.set_data(wheel_x, wheel_y)
    # Обновляем положение точки на ободе
    point.set_data([x_point], [y_point])
    # Обновляем таймер
    timer_text.set_text(f'Time: {t[i]:.1f} s')

    return line, wheel, point, timer_text


# Анимация с настройкой интервала
ani = FuncAnimation(fig, animate, frames=frames, init_func=init, interval=1000 / fps, blit=True)

# Показ анимации
plt.show()



