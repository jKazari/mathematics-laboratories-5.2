import numpy as np
from scipy import stats

# Dane
nA = 21
xA = 3.2
sA = 1.7

nB = 34
xB = 3.6
sB = 1.2

alpha = 0.05

print("Test porównania średnich czasów obsługi – bank A vs bank B\n")

print("Hipotezy:")
print("   H0: μA ≥ μB")
print("   H1: μA < μB\n")

print("Dane:")
print(f"   Bank A: n={nA}, x̄={xA}, s={sA}")
print(f"   Bank B: n={nB}, x̄={xB}, s={sB}\n")

# Wariancje
sA2 = sA**2
sB2 = sB**2

# Błąd standardowy różnicy
SE = np.sqrt(sA2/nA + sB2/nB)

# Statystyka t
t_stat = (xA - xB) / SE

# Stopnie swobody (Welch)
df = (sA2/nA + sB2/nB)**2 / (
    (sA2/nA)**2/(nA-1) + (sB2/nB)**2/(nB-1)
)

# p-value (lewostronne)
p_value = stats.t.cdf(t_stat, df)

# wartość krytyczna
t_crit = stats.t.ppf(alpha, df)

print("Obliczenia:")
print(f"   Błąd standardowy różnicy = {SE:.4f}")
print(f"   Statystyka t = {t_stat:.4f}")
print(f"   Stopnie swobody ≈ {df:.2f}")
print(f"   t krytyczne = {t_crit:.4f}")
print(f"   p-value = {p_value:.6f}\n")

# Decyzja
if t_stat < t_crit:
    decision = "Odrzucamy H0"
else:
    decision = "Brak podstaw do odrzucenia H0"

print("Decyzja:")
print(f"   {decision} przy α = 0.05")
