from scipy import stats
import numpy as np

# Dane
mu0 = 10
x_bar = 11.6
s = 3.7
n = 18
alpha = 0.01

print("Test hipotezy o średnim poborze mocy żarówek LED\n")

print("Hipotezy:")
print("   H0: μ ≤ 10 W")
print("   H1: μ > 10 W\n")

# Statystyka testowa
SE = s / np.sqrt(n)
t_stat = (x_bar - mu0) / SE

# p-value (jednostronne)
p_value = 1 - stats.t.cdf(t_stat, df=n-1)

# wartość krytyczna
t_crit = stats.t.ppf(1 - alpha, df=n-1)

print("Dane z próby:")
print(f"   n = {n}")
print(f"   x̄ = {x_bar:.2f} W")
print(f"   s = {s:.2f} W\n")

print("Obliczenia:")
print(f"   Błąd standardowy = {SE:.4f}")
print(f"   Statystyka t = {t_stat:.4f}")
print(f"   t krytyczne = {t_crit:.4f}")
print(f"   p-value = {p_value:.6f}\n")

# Decyzja
if t_stat > t_crit:
    decision = "Odrzucamy H0"
else:
    decision = "Brak podstaw do odrzucenia H0"

print("Decyzja:")
print(f"   {decision} przy poziomie istotności α = 0.01")
