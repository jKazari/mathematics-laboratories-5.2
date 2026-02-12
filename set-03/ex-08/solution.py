import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

μ = 17330
σ2 = 25300000
σ = np.sqrt(σ2)

dist = stats.norm(loc=μ, scale=σ)

# P(8000 < X < 12000)
p1 = dist.cdf(12000) - dist.cdf(8000)
print("1. Udział gospodarstw mających dochody większe niż 8000 zł i jednocześnie mniejsze niż 12000 zł:")
print(f"   P(8000 < X < 12000) = {p1:.4f}")
print(f"   Odpowiedź: {p1*100:.2f}%")

print("2. Jakie minimalne dochody będzie otrzymywało 5% gospodarstw o największych dochodach:")
print(f"   Odpowiedź: {dist.ppf(0.95):.2f} PLN")

n = 200
k = 53
x̄ = 16100
s = 6000
ɑ = 0.1

p̂ = k / n

t_crit = stats.t.ppf(1-ɑ/2, df=n-1)

margin = t_crit * np.sqrt((p̂ * (1-p̂)) / n)

print("3. Estymacja przedziałowa udziału gospodarstw bezdzietnych w populacji przy poziomie istotności ɑ = 0.1:")
print(f"   p ∈ ({p̂ - margin:.2f}, {p̂ + margin:.2f})")

ɑ = 0.05

t_crit = stats.t.ppf(1-ɑ/2, df=n-1)

margin = t_crit * s / np.sqrt(n)

print("4. Estymacja przedziałowa wartości średniej dochodów w populacji gospodarstw przy poziomie istotności ɑ = 0.05:")
print(f"   μ ∈ ({x̄ - margin:.2f} PLN, {x̄ + margin:.2f} PLN)")