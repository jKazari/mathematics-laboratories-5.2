import pandas as pd
import numpy as np
from scipy import stats

# wczytanie danych
data = pd.read_csv(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-01\ex-XX\data.csv")

x = data["price [euro]"].dropna()

n = len(x)
x_bar = x.mean()
s = x.std(ddof=1)
mu0 = 300000

print("Test hipotezy o średniej cenie mieszkania w Sewilli\n")

print("Dane z próby:")
print(f"   n = {n}")
print(f"   x̄ = {x_bar:.2f}")
print(f"   s = {s:.2f}\n")

# statystyka testowa
SE = s / np.sqrt(n)
t_stat = (x_bar - mu0) / SE

# p-value (dwustronne)
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=n-1))

print("Obliczenia:")
print(f"   Błąd standardowy = {SE:.2f}")
print(f"   Statystyka t = {t_stat:.4f}")
print(f"   p-value = {p_value:.6f}\n")

# decyzje dla α = 0.05 i 0.01
for alpha in [0.05, 0.01]:
    t_crit = stats.t.ppf(1 - alpha/2, df=n-1)

    if abs(t_stat) > t_crit:
        decision = "Odrzucamy H0"
    else:
        decision = "Brak podstaw do odrzucenia H0"

    print(f"Poziom istotności α = {alpha}:")
    print(f"   t krytyczne = ±{t_crit:.4f}")
    print(f"   {decision}\n")
