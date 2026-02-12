import pandas as pd
import numpy as np
from scipy import stats

# Przydatne symbole: ɑ, σ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

data = pd.read_excel(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-03\ex-07\data.xlsx")

x = data["price"]

n = len(x)
x̄ = np.mean(x)
s = np.std(x, ddof=1)
ɑ = 0.05

t_crit = stats.t.ppf(1-ɑ/2, df=n-1)

l_margin = (s * np.sqrt(2*n)) / (np.sqrt(2*n) + t_crit)
r_margin = (s * np.sqrt(2*n)) / (np.sqrt(2*n) - t_crit)

print("Estymacja przedziałowa odchylenia standardowego ceny sprzedaży samochodów marki Volkswagen na poziomie ufności 0.95:")
print(f"   σ ∈ ({l_margin:,.2f}, {r_margin:,.2f})")