import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

data = pd.read_excel(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-03\ex-11\data.xlsx")

x = data["Kwota"]

ɑ = 0.05

stat, p_value = stats.shapiro(x)

if p_value > ɑ:
	decision = "Rozkład kwoty zaciągniętych kredytów jest rozkładem normalnym"
else:
	decision = "Rozkład kwoty zaciągniętych kredytów nie jest rozkładem normalnym"

print(f"{decision} przy poziomie istotności ɑ = 0.05.")