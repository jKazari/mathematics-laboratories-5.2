import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

μ0 = 20000

n = 15
x̄ = 18650
s = 685
ɑ = 0.05

print("H₀: Przeciętna trwałość lamp LED wynosi 20 000 godzin.")
print("H₁: Przeciętna trwałość lamp LED nie wynosi 20 000 godzin.\n")

t = (x̄ - μ0) / (s / np.sqrt(n))

t_crit = stats.t.ppf(1-ɑ/2, df=n-1)

if np.abs(t) > t_crit:
	decision = "Należy odrzucić H₀"
else:
	decision = "Nie ma podstaw do odrzucenia H₀"

print(f"{decision} przy poziomie istotności ɑ = 0.05.")