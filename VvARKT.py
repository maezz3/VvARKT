import numpy as np
import matplotlib.pyplot as plt
heights = np.linspace(0, 25000, 1000)  # Создаем массив высот

gravi_parameter_kerbin = 3531600000000
gravi_parameter_Mun = 65138398000

r1_kerbin = 737161
r2_kerbin = 4567334

a = (r1_kerbin + r2_kerbin) / 2
r_mun = 333478

g0 = 9.80665
V_e = 2570
p0 = 101325
P_e = p0 * 1.5
C_p = 1004.685
T0 = 288.16
M = 0.0289697
R0 = 8.31446
A_e = 0.9
m = 236.6


# Находим удельный импульс двигателя относительно высоты
def specific_impulse_engine(height):
    return (V_e / g0) + (((P_e - p0) * (1 - g0 * height / (C_p * T0))**((C_p * M) / R0) * A_e) / (m * g0))


def delta_necessary_momentum():
    return ((gravi_parameter_kerbin / r1_kerbin)**0.5) * (((r2_kerbin / a)**0.5) - 1)


def momentum_in_mun_pericenter():
    return (gravi_parameter_Mun / r_mun)**0.5


def mun_zero_eccentricity_momentum():
    return delta_necessary_momentum() - momentum_in_mun_pericenter()


print(f"Необходимый удельный импульс, который необходимо совершить на орбите Кербина\
для получения переходной орбиты: {delta_necessary_momentum()} м/с\nНеобходимый удельный\
 импульс, который необходимо совершить в перицентре Муны: {mun_zero_eccentricity_momentum()} м/с")

# Передача функции и массива,а также оси по которой нужно резать массив
values = np.apply_along_axis(specific_impulse_engine, 0, heights)
fig, axis = plt.subplots()  # Сетка и оси по умолчанию
graph = axis.plot(heights, values)  # Передача значений по которым строится график
axis.set_xlabel('Высота, м')
axis.set_ylabel('Удельный импульс двигателя, с')

plt.show()


