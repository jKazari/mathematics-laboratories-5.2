import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

data = pd.read_excel(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-03\ex-05\data.xlsx")

x = data["Cena za m2"].dropna()
ɑ = 0.05

stat, p_value = stats.shapiro(x)

print("H₀: Rozkład cen mieszkań w Gdańsku jest rozkładem normalnym")
print("H₁: Rozkład cen mieszkań w Gdańsku nie jest rozkładem normalnym\n")

if p_value > ɑ:
	decision = "Odrzucamy hipotezę zerową"
else:
	decision = "Brak podstaw do odrzucenia hipotezy zerowej"

print(f"Wartość p = {p_value:.6f}\n")

print("Decyzja:")
print(f"   {decision} przy poziomie istotności α = 0.05")

# Hipoteza zerowa ma postać: "rozkład cen mieszkań w Gdańsku jest rozkładem 
# normalnym", zaś alternatywna: "rozkład cen mieszkań w Gdańsku nie jest 
# rozkładem normalnym". Statystyka testowa testu p value ma wartość około
# 0.000053, co pozwala wyprowadzić wniosek, iż należy uznać hipotezę zerową
# ponieważ p < ɑ.