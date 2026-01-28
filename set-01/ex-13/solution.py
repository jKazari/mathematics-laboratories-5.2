from scipy import stats
import numpy as np

# Dane
mu0 = 110
x_bar = 94
s = 48
n = 100
alpha = 0.05

print("Test hipotezy o średniej cenie abonamentu\n")

print("Hipotezy:")
print("   H0: μ = 110")
print("   H1: μ ≠ 110\n")

# Statystyka testowa
SE = s / np.sqrt(n)
t_stat = (x_bar - mu0) / SE

# p-value
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=n-1))

# wartość krytyczna
t_crit = stats.t.ppf(1 - alpha/2, df=n-1)

print("Dane z próby:")
print(f"   n = {n}")
print(f"   x̄ = {x_bar:.2f}")
print(f"   s = {s:.2f}\n")

print("Obliczenia:")
print(f"   Błąd standardowy = {SE:.4f}")
print(f"   Statystyka t = {t_stat:.4f}")
print(f"   t krytyczne = ±{t_crit:.4f}")
print(f"   p-value = {p_value:.6f}\n")

# Decyzja
if abs(t_stat) > t_crit:
    decision = "Odrzucamy H0"
else:
    decision = "Brak podstaw do odrzucenia H0"

print("Decyzja:")
print(f"   {decision} przy poziomie istotności α = 0.05")
