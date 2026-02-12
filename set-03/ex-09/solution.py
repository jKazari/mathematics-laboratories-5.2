import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

data = pd.read_excel(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-03\ex-09\data.xlsx")

x = data["TRANSPORT"]

ɑ = 0.05

n = len(x)
x̄ = np.mean(x)
s = np.std(x, ddof=1)

t_crit = stats.t.ppf(1-ɑ/2, df=n-1)

l_margin = (s * np.sqrt(2*n)) / (np.sqrt(2*n) + t_crit)
r_margin = (s * np.sqrt(2*n)) / (np.sqrt(2*n) - t_crit)

print("1. Przedział ufności dla odchylenia standardowego zmiennej TRANSPORT na poziomie 0.95 ma postać:")
print(f"   σ ∈ ({l_margin:.2f}, {r_margin:.2f})\n")

# Przedział ufności dla odchylenia standardowego zmiennej TRANSPORT na poziomie 
# ufności 0.95 ma postać (35.82, 62.89) i na jego podstawie powiemy, że z 
# poziomem ufności 0.95 szacujemy, że rzeczywiste odchylenie standardowe
# zmiennej TRANSPORT w populacji mieści się w przedziale (35.82, 62.89).

stat, p_value = stats.shapiro(x)

print("2. Test normalności rozkładu Shapiro-Wilka dla zmiennej TRANSPORT:")
print("   H₀: Rozkład zmiennej losowej TRANSPORT jest rozkładem normalnym")
print("   H₁: Rozkład zmiennej losowej TRANSPORT jest rozkładem normalnym\n")
print(f"   p = {p_value:.6f}\n")

if p_value > ɑ:
	decision = "Należy odrzucić H₀"
else:
	decision = "Brak podstaw do odrzucenia H₀"

print(f"   {decision} przy poziomie istotności ɑ = 0.05.")

# Na poziomie istotności 0.05 powiemy, że rozkład tej zmiennej jest rozkładem 
# normalnym, ponieważ statystyka p <= ɑ.