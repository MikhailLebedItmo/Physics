import numpy as np
import matplotlib.pyplot as plt

DEBUG = False

# Ввод данных от пользователя

if DEBUG:
    mass = 10
    k = 10
    b = 0
else:
    mass = float(input("Введите массу груза (кг): "))
    k = float(input("Введите коэффициент жесткости пружины (Н/м): "))
    b = float(input("Введите коэффициент сопротивления (Н·с/м): "))
g = 9.81  # ускорение свободного падения (м/с^2)

# Параметры моделирования
time_end = 80  # конец моделирования (в секундах)
dt = 0.0005  # шаг по времени

# Инициализация массивов для хранения данных
time = np.arange(0, time_end, dt)
x = np.zeros_like(time)  # положение груза
v = np.zeros_like(time)  # скорость груза

# Начальные условия
x[0] = 0.0  # начальное смещение (м)
v[0] = 0.0  # начальная скорость (м/с)

# Расчет энергии
kinetic_energy = np.zeros_like(time)
spring_potential_energy = np.zeros_like(time)
gravitational_potential_energy = np.zeros_like(time)
total_energy = np.zeros_like(time)

# Численное решение уравнения движения методом Эйлера
for i in range(1, len(time)):
    a = (-k * x[i - 1] - b * v[i - 1] - g * mass) / mass  # ускорение с учетом гравитации
    v[i] = v[i - 1] + a * dt
    x[i] = x[i - 1] + v[i - 1] * dt

    # Расчет энергий
    kinetic_energy[i] = 0.5 * mass * v[i] ** 2
    spring_potential_energy[i] = 0.5 * k * x[i] ** 2
    gravitational_potential_energy[i] = mass * g * x[i]
    total_energy[i] = kinetic_energy[i] + spring_potential_energy[i] + gravitational_potential_energy[i]

# Построение графиков
plt.figure(figsize=(18, 9))

plt.plot(time, kinetic_energy, label="Кинетическая энергия тела", color='blue', linestyle='-')
plt.plot(time, spring_potential_energy, label="Потенциальная энергия пружины", color='black', linestyle='-')
plt.plot(time, gravitational_potential_energy, label="Потенциальная энергия тела", color='red', linestyle='-')
plt.plot(time, total_energy, label="Полная механическая энергия", color='green', linestyle='--')

plt.xlabel("Time (S)")
plt.ylabel("Energy (J)")
plt.legend()
plt.grid(True)

plt.show()
