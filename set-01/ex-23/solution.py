import pandas as pd
import numpy as np
from scipy import stats

# wczytanie danych
data = pd.read_csv(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-01\ex-23\data.csv")

# kolumna 4 = Gdańsk, kolumna 9 = Poznań
g = data.iloc[:, 3].dropna()
p = data.iloc[:, 8].dropna()

n_g = len(g)
n_p = len(p)

xg = g.mean()
xp = p.mean()

sg = g.std(ddof=1)
sp = p.std(ddof=1)

print("Test równości średniej sprzedaży benzyny Euro 95 (Gdańsk vs Poznań)\n")

print("Dane z próby:")
print(f"   Gdańsk:  n = {n_g}, x̄ = {xg:.4f}, s = {sg:.4f}")
print(f"   Poznań:  n = {n_p}, x̄ = {xp:.4f}, s = {sp:.4f}\n")

# test Welcha
SE = np.sqrt(sg**2 / n_g + sp**2 / n_p)
t_stat = (xg - xp) / SE

df = (sg**2 / n_g + sp**2 / n_p)**2 / (
    (sg**2 / n_g)**2 / (n_g - 1) + (sp**2 / n_p)**2 / (n_p - 1)
)

p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
t_crit = stats.t.ppf(1 - 0.05/2, df)

print("Obliczenia:")
print(f"   Statystyka t = {t_stat:.4f}")
print(f"   Stopnie swobody ≈ {df:.2f}")
print(f"   t krytyczne = ±{t_crit:.4f}")
print(f"   p-value = {p_value:.6f}\n")

if abs(t_stat) > t_crit:
    decision = "Odrzucamy H0"
else:
    decision = "Brak podstaw do odrzucenia H0"

print("Decyzja:")
print(f"   {decision} przy α = 0.05")
