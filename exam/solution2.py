import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, χ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

μ = 10530
σ2 = 16000000
σ = np.sqrt(σ2)

dist = stats.norm(loc=μ, scale=σ)

# P(X > 12000) = 1 - P(X <= 12000)
print("1. Udział osób mających dochody większe niż 12000 zł")
print(f"   {1 - dist.cdf(12000):.4f}")
print(f"   Odpowiedź: {1 - dist.cdf(12000):.2f}%")

n = 200
k = 65
x̄ = 9200
s = 4400

ɑ = 0.05

p̂ = k/n
t_crit = stats.t.ppf(1-ɑ/2, df=n-1)

margin = t_crit * np.sqrt((p̂ * (1-p̂)) / n)

print("2. Estymacja przedziałowa udziału osób bezdzietnych w populacji:")
print(f"   ({p̂ - margin:.2f}, {p̂ + margin:.2f})")

margin = t_crit * s / np.sqrt(n)

print("3. Estymacja przedziałowa wartości średniej dochodów w populacji")
print(f"μ in ({x̄ - margin:.2f}, {x̄ + margin:.2f})")

μ0 = 10000
t = (x̄ - μ0) / (s / np.sqrt(n))
t_crit = stats.t.ppf(1-ɑ, df=n-1)

print("4. Hipotezy")
print("   H0: średnie dochody w populacji są większe lub równe od 10000")
print("   H1: średnie dochody w populacji są mniejsze od 10000")

print(t)
print(t_crit)

if t < t_crit:
	decision = "Odrzucamy H0"
else:
	decision = "Brak podstaw do odrzucenia H0"

print(f"{decision} przy poziomie istotności alpha = 0.05")