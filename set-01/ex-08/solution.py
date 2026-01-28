import pandas as pd
import numpy as np
from scipy import stats

# wczytanie danych
data = pd.read_csv(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-01\ex-08\data.csv")

# ceny sprzedaży
x = data["price"].dropna()

n = len(x)
s2 = x.var(ddof=1)

print("Estymacja wariancji cen sprzedaży samochodów\n")

print("Dane z próby:")
print(f"   Liczność próby n = {n}")
print(f"   Wariancja z próby s² = {s2:.6e}\n")

def conf_interval(confidence):
    alpha = 1 - confidence
    chi2_lo = stats.chi2.ppf(1 - alpha/2, df=n-1)
    chi2_hi = stats.chi2.ppf(alpha/2, df=n-1)
    lower = (n - 1) * s2 / chi2_lo
    upper = (n - 1) * s2 / chi2_hi
    return chi2_lo, chi2_hi, lower, upper

for conf in [0.90, 0.95, 0.99]:
    chi2_lo, chi2_hi, lower, upper = conf_interval(conf)

    print(f"{int(conf*100)}% przedział ufności:")
    print(f"   χ²_(1-α/2) = {chi2_lo:.4f}")
    print(f"   χ²_(α/2)   = {chi2_hi:.4f}")
    print(f"   Przedział: [{lower:.6e} , {upper:.6e}]\n")
