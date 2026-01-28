import numpy as np
from scipy import stats

# Dane
n = 250
x = 57
p0 = 0.25
alpha = 0.05

p_hat = x / n

print("Test hipotezy o udziale gospodarstw kupujących prasę kobiecą\n")

print("Hipotezy:")
print("   H0: p = 0.25")
print("   H1: p ≠ 0.25\n")

print("Dane z próby:")
print(f"   n = {n}")
print(f"   liczba kupujących = {x}")
print(f"   estymator p̂ = {p_hat:.4f}\n")

# Statystyka Z
SE = np.sqrt(p0 * (1 - p0) / n)
Z = (p_hat - p0) / SE

# p-value
p_value = 2 * (1 - stats.norm.cdf(abs(Z)))

# wartość krytyczna
z_crit = stats.norm.ppf(1 - alpha/2)

print("Obliczenia:")
print(f"   Błąd standardowy = {SE:.5f}")
print(f"   Statystyka Z = {Z:.4f}")
print(f"   z krytyczne = ±{z_crit:.4f}")
print(f"   p-value = {p_value:.6f}\n")

# Decyzja
if abs(Z) > z_crit:
    decision = "Odrzucamy H0"
else:
    decision = "Brak podstaw do odrzucenia H0"

print("Decyzja:")
print(f"   {decision} przy poziomie istotności α = 0.05")
