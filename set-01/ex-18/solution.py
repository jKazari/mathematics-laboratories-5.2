from scipy import stats
import numpy as np

# Dane
mu0 = 60
x_bar = 56
s = 16
n = 70
alpha = 0.05

print("Test hipotezy o średnim czasie dostawy\n")

print("Hipotezy:")
print("   H0: μ = 60 min")
print("   H1: μ < 60 min\n")

# Statystyka testowa
SE = s / np.sqrt(n)
t_stat = (x_bar - mu0) / SE

# p-value (jednostronne)
p_value = stats.t.cdf(t_stat, df=n-1)

# wartość krytyczna
t_crit = stats.t.ppf(alpha, df=n-1)

print("Dane z próby:")
print(f"   n = {n}")
print(f"   x̄ = {x_bar:.2f} min")
print(f"   s = {s:.2f} min\n")

print("Obliczenia:")
print(f"   Błąd standardowy = {SE:.4f}")
print(f"   Statystyka t = {t_stat:.4f}")
print(f"   t krytyczne = {t_crit:.4f}")
print(f"   p-value = {p_value:.6f}\n")

# Decyzja
if t_stat < t_crit:
    decision = "Odrzucamy H0"
else:
    decision = "Brak podstaw do odrzucenia H0"

print("Decyzja:")
print(f"   {decision} przy poziomie istotności α = 0.05")
