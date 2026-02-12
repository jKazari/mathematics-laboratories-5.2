import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

n = 246
k = 246 - 85
x̄ = 88
s = 25.3

ɑ = 0.05
t_crit = stats.t.ppf(1-ɑ/2, df=n-1)
margin = t_crit * s / np.sqrt(n)

print("1. Estymacja przedziałowa dla wartości oczekiwanej oglądalności w populacji gospodarstw z 95% poziomu ufności:")
print(f"   μ ∈ ({x̄ - margin:.2f}, {x̄ + margin:.2f})")

ɑ = 0.1
t_crit = stats.t.ppf(1-ɑ/2, df=n-1)

print("2. Estymacja przedziałowa dla odchylenia standardowego oglądalności w populacji gospodarstw z 90% poziomu ufności:")
print(f"   σ ∈ ({(s * np.sqrt(2 * n)) / (np.sqrt(2 * n) + t_crit):.2f}, {(s * np.sqrt(2 * n)) / (np.sqrt(2 * n) - t_crit):.2f})")

ɑ = 0.05
p̂ = k / n
t_crit = stats.t.ppf(1-ɑ/2, df=n-1)
margin = t_crit * np.sqrt((p̂ * (1 - p̂)) / (n))

print("3. Estymacja przedziałowa dla udziału gospodarstw oglądających wiadomości w populacji z 95% poziomu ufności:")
print(f"   p ∈ ({p̂ - margin:.2f}, {p̂ + margin:.2f})")