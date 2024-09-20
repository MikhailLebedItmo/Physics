
# Отчёт по симуляции баллистического движения

Ссылка на исполняемый файл с программой: [ballistic_movement_visualization.exe](https://drive.google.com/drive/folders/1D21uuw61HFgApwHCO2jaRYHK5oxqH52_?usp=sharing) 

## Описание программы

Данная программа моделирует движение тела, брошенного под углом к горизонту, с учётом силы тяжести. Для симуляции траектории движения и скоростей на различных участках времени используется численный метод.

### Основные шаги программы

1. **Деление временного промежутка**: Время полёта разбивается на множество малых промежутков.
2. **Постоянная скорость в каждом промежутке**: В каждом из этих малых промежутков скорость считается постоянной.
3. **Изменение скорости**: В конце каждого промежутка скорости пересчитываются в соответствии с ускорением (гравитацией).

### Результаты

На выходе программа строит несколько графиков, которые отображают:
- Зависимость горизонтальной и вертикальной координаты от времени.
- Траекторию движения.
- Зависимость общей скорости от времени.
- Зависимость горизонтальной и вертикальной скоростей от времени.

## Заключение

Программа является примером численного моделирования баллистического движения, где на каждом малом участке времени параметры (скорость, координаты) обновляются с учётом ускорения свободного падения.