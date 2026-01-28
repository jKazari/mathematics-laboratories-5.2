from scipy import stats
import numpy as np

# Dane
mu0 = 20
x_bar = 19.95
s = 0.022
n = 30
alpha = 0.05

print("Test hipotezy o średniej średnicy elementów\n")

print("Hipotezy:")
print("   H0: μ = 20 mm")
print("   H1: μ ≠ 20 mm\n")

# Statystyka testowa
SE = s / np.sqrt(n)
t_stat = (x_bar - mu0) / SE

# p-value
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=n-1))

# Wartość krytyczna
t_crit = stats.t.ppf(1 - alpha/2, df=n-1)

print("Dane z próby:")
print(f"   n = {n}")
print(f"   x̄ = {x_bar:.4f} mm")
print(f"   s = {s:.4f} mm\n")

print("Obliczenia:")
print(f"   Błąd standardowy = {SE:.6f}")
print(f"   Statystyka t = {t_stat:.4f}")
print(f"   t krytyczne = ±{t_crit:.4f}")
print(f"   p-value = {p_value:.6e}\n")

# Decyzja
if abs(t_stat) > t_crit:
    decision = "Odrzucamy H0"
else:
    decision = "Brak podstaw do odrzucenia H0"

print("Decyzja:")
print(f"   {decision} przy poziomie istotności α = 0.05")
