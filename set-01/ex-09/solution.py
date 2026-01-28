from scipy import stats
import numpy as np

# Dane
n = 75
s = 2350
alpha = 0.05

s2 = s**2

print("Estymacja wariancji dochodów klientów banku\n")

print("Dane:")
print(f"   Liczność próby n = {n}")
print(f"   Odchylenie standardowe s = {s:.2f} zł")
print(f"   Wariancja z próby s² = {s2:.2f}\n")

# Kwantyle chi-kwadrat
chi2_lower = stats.chi2.ppf(1 - alpha/2, df=n-1)
chi2_upper = stats.chi2.ppf(alpha/2, df=n-1)

print("Rozkład chi-kwadrat:")
print(f"   χ²_(1-α/2) = χ²_0.975 = {chi2_lower:.4f}")
print(f"   χ²_(α/2)   = χ²_0.025 = {chi2_upper:.4f}\n")

# Granice przedziału
lower = (n - 1) * s2 / chi2_lower
upper = (n - 1) * s2 / chi2_upper

print("95% przedział ufności dla wariancji:")
print(f"   [{lower:,.2f} , {upper:,.2f}] (zł²)")
