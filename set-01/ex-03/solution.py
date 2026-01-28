from scipy import stats
import numpy as np

# Dane z zadania
n = 30
x_bar = 6575
s = 2400
alpha = 0.10   # 90% poziom ufności

print("Estymacja średnich dochodów gospodarstw domowych\n")

# Wartość krytyczna t-Studenta
t_crit = stats.t.ppf(1 - alpha/2, df=n-1)

# Błąd standardowy
SE = s / np.sqrt(n)

# Margines błędu
margin = t_crit * SE

# Granice przedziału ufności
lower = x_bar - margin
upper = x_bar + margin

print("Dane:")
print(f"   Liczność próby n = {n}")
print(f"   Średnia z próby x̄ = {x_bar:.2f} zł")
print(f"   Odchylenie standardowe s = {s:.2f} zł\n")

print("Parametry rozkładu t-Studenta:")
print(f"   Stopnie swobody = {n-1}")
print(f"   t_(α/2) = {t_crit:.4f}\n")

print("Obliczenia:")
print(f"   Błąd standardowy SE = s / √n = {SE:.2f}")
print(f"   Margines błędu = t * SE = {margin:.2f}\n")

print("90% przedział ufności dla średniej dochodów:")
print(f"   [{lower:.2f} zł , {upper:.2f} zł]")
