import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, μ, μ₀, x̄, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞

n = 34
x̄ = 3.3
s = 1.4
μ0 = 2.6
ɑ = 0.05

print("Hipotezy:")
print("   H₀: μ = 2.6 dni")
print("   H₁: μ ≠ 2.6 dni\n")

t = (x̄ - μ0) / (s / np.sqrt(n))

t_crit = stats.t.ppf(1-ɑ/2, df=n-1)

p_value = 1 - stats.t.cdf(t, df=n-1)

print("Dane z próby:")
print(f"   n = {n}")
print(f"   x̄ = {x̄:.2f}")
print(f"   s = {s:.2f}\n")

print("Obliczenia:")
print(f"   Statystyka t = {t:.4f}")
print(f"   t krytyczne = {t_crit:.4f}")
print(f"   p-value = {p_value:.6f}\n")

# Decyzja
if t < -t_crit or t > t_crit:
    decision = "Odrzucamy H₀"
else:
    decision = "Brak podstaw do odrzucenia H₀"

print("Decyzja:")
print(f"   {decision} przy poziomie istotności α = 0.05")

# Hipoteza zerowa zakłada, że przeciętny czas dostarczenia przesyłki wynosi 
# 2.6 dnia, a hipoteza alternatywna zakłąda, że przeciętny czas dostarczenia
# przesyłki nie wynosi 2.6 dnia (wynosi więcej). Na poziomie istotności 0.05
# stwierdzamy, że należy odrzucić hipotezę zerową, ponieważ otrzymana 
# statystyka t znajduje się w przedziale (-∞, t_crit) ∪ (t_crit, ∞).