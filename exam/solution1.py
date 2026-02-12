import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, χ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

data = pd.read_excel(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\exam\data.xlsx")

x = data["masa"]

ɑ = 0.05

stat, p_value = stats.shapiro(x)

print("1. Hipotezy:")
print("   H₀: Rozkład zmiennej MASA jest rozkładem normalnym")
print("   H₁: Rozkład zmiennej MASA nie jest rozkładem normalnym\n")

print(f"   Wartość p = {p_value:.6f}\n")

if p_value < ɑ:
	decision = "Należy odrzucić H₀"
else:
	decision = "Brak podstaw do odrzucenia H₀"

print(f"   {decision} przy poziomie istotności ɑ = 0.05")

print("2. Hipotezy:")
print("   H₀: Kobiety z populacji nie są średnio niższe od mężczyzn z populacji (μK ≥ μM)")
print("   H₁: Kobiety z populacji są średnio niższe od mężczyzn z populacji (μK < μM)\n")

x = data[data["płeć"] == "M"]["wzrost"]
y = data[data["płeć"] == "K"]["wzrost"]

nM = len(x)
nK = len(y)

x̄ = np.mean(x)
ȳ = np.mean(y)

sM = np.std(x, ddof=1)
sK = np.std(y, ddof=1)

t = (x̄ - ȳ) / np.sqrt((sM**2 / nM) + (sK**2 / nK))
df = (((sM**2 / nM) + (sK**2 / nK))**2) / (((sM**2 / nM)**2) / (nM-1) + ((sK**2 / nK)**2) / (nK-1))

t_crit = stats.t.ppf(1-ɑ, df)

print("   Obliczenia:")
print(f"   Statystyka t = {t:.4f}")
print(f"   t krytyczne = {t_crit:.4f}\n")

if t > t_crit:
	decision = "Należy odrzucić H₀"
else:
	decision = "Brak podstaw do odrzucenia H₀"

print(f"   {decision} przy poziomie istotności ɑ = 0.05")