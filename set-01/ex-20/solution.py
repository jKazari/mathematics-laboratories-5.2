from scipy import stats
import numpy as np

# Dane
mu0 = 5000
x_bar = 4650
s = 1080
n = 10
alpha = 0.05

print("Test hipotezy o średniej trwałości ekranów LED\n")

print("Hipotezy:")
print("   H0: μ ≥ 5000 h")
print("   H1: μ < 5000 h\n")

# Statystyka testowa
SE = s / np.sqrt(n)
t_stat = (x_bar - mu0) / SE

# p-value (jednostronne, lewostronne)
p_value = stats.t.cdf(t_stat, df=n-1)

# wartość krytyczna
t_crit = stats.t.ppf(alpha, df=n-1)

print("Dane z próby:")
print(f"   n = {n}")
print(f"   x̄ = {x_bar:.2f} h")
print(f"   s = {s:.2f} h\n")

print("Obliczenia:")
print(f"   Błąd standardowy = {SE:.2f}")
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
