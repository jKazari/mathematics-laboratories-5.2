import pandas as pd
import numpy as np
from scipy import stats

# Dane
μ = 10530
σ2 = 16000000
σ = np.sqrt(σ2)

dist = stats.norm(loc=μ, scale=σ)

# P(X > 12000) = 1 - P(X <= 12000)
print("1. Udział osób mających dochody większe niż 12 000 PLN")
print(f"   P(X > 12000) = {1 - dist.cdf(12000):.4f}")
print(f"   Odpowiedź: {1 - dist.cdf(12000):.2f}%")

# Dane
n = 200
k = 65
x̄ = 9200
s = 4400

ɑ = 0.05
p̂ = k/n
t_crit = stats.t.ppf(1-ɑ/2, df=n-1)
margin = t_crit * np.sqrt((p̂ * (1-p̂)) / n)

print("2. Estymacja przedziałowa udziału osób bezdzietnych w populacji:")
print(f"   p ∈ ({p̂ - margin:.2f}, {p̂ + margin:.2f}) z ufnością 0.95")

margin = t_crit * s / np.sqrt(n)

print("3. Estymacja przedziałowa wartości średniej dochodów w populacji:")
print(f"   μ ∈ ({x̄ - margin:.2f}, {x̄ + margin:.2f}) z ufnością 0.95")

μ0 = 10000
t = (x̄ - μ0) / (s / np.sqrt(n))
t_crit = stats.t.ppf(1-ɑ, df=n-1)

print("4. Hipotezy:")
print("   H₀: średnie dochody w populacji są większe lub równe od 10 000 PLN")
print("   H₁: średnie dochody w populacji są mniejsze od 10 000 PLN\n")

print("   Obliczenia:")
print(f"   Statystyka t = {t:.4f}")
print(f"   t krytyczne = {t_crit:.4f}\n")

if t < t_crit:
	decision = "Odrzucamy H₀"
else:
	decision = "Brak podstaw do odrzucenia H₀"

print(f"   {decision} przy poziomie istotności ɑ = 0.05")