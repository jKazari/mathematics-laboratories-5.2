import numpy as np
from scipy import stats

# Dane
n1 = 195
x1 = 4670
s1_sq = 3.61e6

n2 = 125
x2 = 5535
s2_sq = 4.22e6

alpha = 0.05

print("Test równości średnich dochodów w dwóch miastach\n")

print("Hipotezy:")
print("   H0: μ1 = μ2")
print("   H1: μ1 ≠ μ2\n")

print("Dane:")
print(f"   Miasto A: n1 = {n1}, x̄1 = {x1}, s1² = {s1_sq:.0f}")
print(f"   Miasto B: n2 = {n2}, x̄2 = {x2}, s2² = {s2_sq:.0f}\n")

# Błąd standardowy różnicy
SE = np.sqrt(s1_sq/n1 + s2_sq/n2)

# Statystyka t
t_stat = (x1 - x2) / SE

# Stopnie swobody (Welch)
df = (s1_sq/n1 + s2_sq/n2)**2 / (
    (s1_sq/n1)**2/(n1-1) + (s2_sq/n2)**2/(n2-1)
)

# p-value (dwustronne)
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))

# wartość krytyczna
t_crit = stats.t.ppf(1 - alpha/2, df)

print("Obliczenia:")
print(f"   Błąd standardowy różnicy = {SE:.2f}")
print(f"   Statystyka t = {t_stat:.4f}")
print(f"   Stopnie swobody ≈ {df:.2f}")
print(f"   t krytyczne = ±{t_crit:.4f}")
print(f"   p-value = {p_value:.6f}\n")

# Decyzja
if abs(t_stat) > t_crit:
    decision = "Odrzucamy H0"
else:
    decision = "Brak podstaw do odrzucenia H0"

print("Decyzja:")
print(f"   {decision} przy α = 0.05")
