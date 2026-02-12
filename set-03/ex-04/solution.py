import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

data = pd.read_excel(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-03\ex-04\data.xlsx")

x = data["Cena"].dropna()

ɑ = 0.05

n = len(x)
x̄ = np.mean(x)
s = np.std(x, ddof=1)

t_crit = stats.t.ppf(1-ɑ/2, df=n-1)
margin = t_crit * s / np.sqrt(n)

print("Estymacja przedziałowa średniej ceny mieszkania w Gdańsku na poziomie ufności 0.95:")
print(f"   μ ∈ ({x̄ - margin:,.2f} PLN, {x̄ + margin:,.2f} PLN)")