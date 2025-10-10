import numpy as np 
import matplotlib.pyplot as plt 
l = 1.000
n = np.array([20, 20, 20, 20, 20, 20, 20, 20, 20])#число колебаний
a = np.array([190.0, 220.0, 140.0, 280.0, 90.0, 200.0, 250.0, 130.0, 160.0]) # [мм]
x_c = np.array([48.1, 48.0, 48.55, 47.5, 49.0, 48.18, 47.6, 48.9, 48.5])
a = a / 1e3 # перевод в [м]
N = len(a) # число точек
t = np.array([32.11, 31.24, 34.80, 30.30, 40.94, 31.59, 30.92, 35.52, 34.48]) #время
T = np.array(t) / n #период
sigma_t=0.13
sigma_a=0.5e-3
sigma_T = sigma_t / t * T

sorted_indices = np.argsort(a)
a_sorted = a[sorted_indices]
T_sorted = T[sorted_indices]
sigma_T_sorted = sigma_T[sorted_indices]


plt.figure(figsize=(8,6), dpi=100)
plt.ylabel("$T$, с")
plt.xlabel("$a$, м")
plt.xlim([0, 0.5])  
plt.title('Рис.1. График зависимости периода $T$ от положения призмы $a$')
plt.grid(True, linestyle="--")


plt.errorbar(a_sorted, T_sorted, xerr=sigma_a, yerr=sigma_T_sorted, 
             fmt=".k", capsize=3, label="Экспериментальные точки")


plt.plot(a_sorted, T_sorted, "--r", linewidth=1, label="Кусочно линейная интерполяция")


min_index = np.argmin(T_sorted)
min_a = a_sorted[min_index]
min_T = T_sorted[min_index]

plt.plot(min_a, min_T, 'bo', markersize=8, label=f"Минимум (a={min_a:.3f} м)")
plt.axvline(x=min_a, color='blue', linestyle=':', alpha=0.5)
plt.axhline(y=min_T, color='blue', linestyle=':', alpha=0.5)

plt.legend()
plt.tight_layout()
plt.show()
