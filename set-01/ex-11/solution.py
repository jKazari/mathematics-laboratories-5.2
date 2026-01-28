import pandas as pd
import numpy as np
from scipy import stats

# wczytanie danych
data = pd.read_excel(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-01\ex-XX\data.xlsx")

# ceny noclegów
x = data["price"].dropna()

n = len(x)
s = x.std(ddof=1)
s2 = s**2

alpha = 0.02   # 98% poziom ufności

print("Estymacja odchylenia standardowego ceny noclegu w Berlinie\n")

print("Dane z próby:")
print(f"   Liczność próby n = {n}")
print(f"   Odchylenie standardowe z próby s = {s:.4f}\n")

# kwantyle chi-kwadrat
chi2_lo = stats.chi2.ppf(1 - alpha/2, df=n-1)
chi2_hi = stats.chi2.ppf(alpha/2, df=n-1)

# przedział dla wariancji
var_lower = (n - 1) * s2 / chi2_lo
var_upper = (n - 1) * s2 / chi2_hi

# przedział dla odchylenia standardowego
sigma_lower = np.sqrt(var_lower)
sigma_upper = np.sqrt(var_upper)

print("Obliczenia:")
print(f"   χ²_(1-α/2) = {chi2_lo:.4f}")
print(f"   χ²_(α/2)   = {chi2_hi:.4f}\n")

print("98% przedział ufności dla σ:")
print(f"   [{sigma_lower:.4f} , {sigma_upper:.4f}]")
