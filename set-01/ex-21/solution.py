import pandas as pd
import numpy as np
from scipy import stats

# wczytanie danych
data = pd.read_csv(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-01\ex-21\data.csv")

# kolumna 2 = bezrobotne kobiety, kolumna 3 = bezrobotni mężczyźni
women_unemp = data.iloc[:, 1].dropna()
men_unemp   = data.iloc[:, 2].dropna()

# sumy bezrobotnych
x1 = women_unemp.sum()
x2 = men_unemp.sum()

# liczba obserwacji (zakładamy tyle samo okresów dla obu płci)
n1 = len(women_unemp)
n2 = len(men_unemp)

# estymatory proporcji (tu: średnia liczba bezrobotnych w okresie jako "udział" w skali danych)
p1 = x1 / (x1 + x2)
p2 = x2 / (x1 + x2)

# proporcja łączna
p = (x1 + x2) / (x1 + x2)

print("Test równości poziomu bezrobocia kobiet i mężczyzn\n")

print("Dane zagregowane:")
print(f"   Suma bezrobotnych kobiet = {x1}")
print(f"   Suma bezrobotnych mężczyzn = {x2}")
print(f"   p̂_K = {p1:.4f}")
print(f"   p̂_M = {p2:.4f}\n")

# statystyka Z
SE = np.sqrt(p1*(1-p1)/(x1+x2) + p2*(1-p2)/(x1+x2))
Z = (p1 - p2) / SE

# p-value (dwustronne)
p_value = 2 * (1 - stats.norm.cdf(abs(Z)))

# wartość krytyczna
z_crit = stats.norm.ppf(1 - 0.05/2)

print("Obliczenia:")
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
