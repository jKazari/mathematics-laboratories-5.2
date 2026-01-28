import pandas as pd
import numpy as np
from scipy import stats

# wczytanie danych
data = pd.read_csv(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-01\ex-16\data.csv")

# powierzchnia mieszkań w m^2
area = data["metraż"].dropna()

# liczność próby
n = len(area)

# liczba mieszkań w przedziale 60–90 m^2
x = ((area >= 60) & (area <= 90)).sum()

# estymator punktowy udziału
p_hat = x / n
p0 = 0.30
alpha = 0.05

print("Test hipotezy o udziale mieszkań 60–90 m² w Sewilli\n")

print("Dane z próby:")
print(f"   n = {n}")
print(f"   liczba w przedziale 60–90 m² = {x}")
print(f"   p̂ = {p_hat:.4f}\n")

# statystyka testowa Z
SE = np.sqrt(p0 * (1 - p0) / n)
Z = (p_hat - p0) / SE

# p-value (dwustronne)
p_value = 2 * (1 - stats.norm.cdf(abs(Z)))

# wartość krytyczna
z_crit = stats.norm.ppf(1 - alpha/2)

print("Obliczenia:")
print(f"   Błąd standardowy = {SE:.6f}")
print(f"   Statystyka Z = {Z:.4f}")
print(f"   z krytyczne = ±{z_crit:.4f}")
print(f"   p-value = {p_value:.6f}\n")

# decyzja
if abs(Z) > z_crit:
    decision = "Odrzucamy H0"
else:
    decision = "Brak podstaw do odrzucenia H0"

print("Decyzja:")
print(f"   {decision} przy α = 0.05")
