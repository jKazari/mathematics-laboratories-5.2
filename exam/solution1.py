import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, χ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

data = pd.read_excel(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\exam\data.xlsx")

x = data["masa"]

ɑ = 0.05

stat, p_value = stats.shapiro(x)

print("Hipotezy:")
print("   H₀: Rozkład zmiennej MASA jest rozkładem normalnym")
print("   H₁: Rozkład zmiennej MASA nie jest rozkładem normalnym\n")

print(f"Wartość p = {p_value:.6f}\n")

if p_value < ɑ:
	decision = "Należy odrzucić H₀"
else:
	decision = "Brak podstaw do odrzucenia H₀"

print(f"{decision} przy poziomie istotności ɑ = 0.05.")

x = data[data["płeć"] == "M"]["wzrost"]
y = data[data["płeć"] == "K"]["wzrost"]

n = len(x)
m = len(y)

xrow = np.mean(x)
yrow = np.mean(y)

sM = np.std(x, ddof=1)
sK = np.std(y, ddof=1)

print(xrow, yrow)