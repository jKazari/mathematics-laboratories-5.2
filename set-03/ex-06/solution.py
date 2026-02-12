import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

data = pd.read_excel(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-03\ex-06\data.xlsx")

x = data["Cena za m2"].dropna()
ɑ = 0.05

n = len(x)
x̄ = np.mean(x)
s = np.std(x, ddof=1)
μ0 = 12500

print("Dane z próby:")
print(f"   n = {n}")
print(f"   x̄ = {x̄:.2f}")
print(f"   s = {s:.2f}\n")

t = (x̄ - μ0) / (s / np.sqrt(n))
t_crit = stats.t.ppf(1-ɑ/2, df=n-1)

print("Obliczenia:")
print(f"   Statystyka t = {t:.4f}")
print(f"   t krytyczne = {t_crit:.4f}\n")

if np.abs(t) > t_crit:
	decision = "Odrzucamy H₀"
else:
	decision = "Brak podstaw do odrzucenia H₀"

print(f"{decision} przy poziomie istotności ɑ = 0.05")

# Hipoteza zerowa ma postać: "średnia cena mieszkania w Gdańsku wynosi 
# 12500 zł/m²", zaś alternatywna: "średnia cena mieszkania w Gdańsku nie wynosi 
# 12500 zł/m²". Statystyka testowa t ma wartość około 1.4799, co pozwala
# wyprowadzić wniosek, iż brakuje podstaw do odrzucenia hipotezy zerowej
# przy poziomie istotności ɑ = 0.05, ponieważ |t| ≤ t_crit ≈ 1.9886.