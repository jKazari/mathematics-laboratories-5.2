import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, μ, μ₀, x̄, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞

μ = 86
σ = np.sqrt(894)

dist = stats.norm(loc=μ, scale=σ)

# P(X > 160) = 1 - P(X <= 160)
p1 = 1 - dist.cdf(160)

print("1. Procent ogółu uczniów jaki można uznać za szczególnie uzdolniony matematycznie:")
print(f"   P(X > 160) = {p1:.6f}")
print(f"   Odpowiedź: {p1*100:.2f}%\n")

# P(X < 35)
p2 = dist.cdf(35)

print("2. Procent ogółu uczniów jaki należy skierować do klasy o specjalnym profilu kształcenia:")
print(f"   P(X < 35) = {p2:.6f}")
print(f"   Odpowiedź: {p2*100:.2f}%\n")
