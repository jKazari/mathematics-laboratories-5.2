# import pandas as pd
# import numpy as np
# from scipy import stats

# # Przydatne symbole: ɑ, σ, χ, μ, μ₀, x̄, p̂, α, H₀, H₁, ², ≥, ≤, ≠, ≈, ∪, ∞, ∈

# # Dane
# n = ...
# μ = ...
# σ = ...
# x̄ = ...
# s = ...
# μ0 = ...
# p0 = ...
# ɑ = ...

# # Przykładowe obliczenia
# z_crit = stats.norm.ppf(1-ɑ/2) # dla dwustronnego
# z_crit = stats.norm.ppf(1-ɑ) # dla lewo i prawostronnego

# χ2_crit = stats.chi2.ppf(1-ɑ/2, df=n-1) # dla dwustronnego
# χ2_crit = stats.chi2.ppf(1-ɑ, df=n-1) # dla lewo i prawostronnego

# t_crit = stats.t.ppf(1-ɑ/2, df=n-1) # dla dwustronnego
# t_crit = stats.t.ppf(1-ɑ, df=n-1) # dla lewo i prawostronnego

# t = ...
# z = ...
# χ2 = ...

# p_value = 2 * (1 - stats.t.cdf(abs(t), df=n-1)) # dla dwustronnego (H₀: θ = θ₀)
# p_value = 1 - stats.t.cdf(t, df=n-1) # dla prawostronnego (H₀: θ ≤ θ₀)
# p_value = stats.t.cdf(t, df=n-1) # dla lewostronnego (H₀: θ ≥ θ₀)

# # Formułki
# print("Hipotezy:")
# print("   H₀: ...")
# print("   H₁: ...\n")

# print("Dane z próby:")
# print(f"   n = {n}")
# print(f"   x̄ = {x̄:.2f}")
# print(f"   s = {s:.2f}\n")

# print("Obliczenia:")
# print(f"   Statystyka t = {t:.4f}")
# print(f"   t krytyczne = {t_crit:.4f}")
# print(f"   p-value = {p_value:.6f}\n")

# decision = "Należy odrzucić H₀"
# decision = "Brak podstaw do odrzucenia H₀"

# print("Decyzja:")
# print(f"   {decision} przy poziomie istotności α = 0.05")