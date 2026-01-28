import pandas as pd
import numpy as np
from scipy import stats

# wczytanie danych
data = pd.read_csv(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-01\ex-10\data.csv")

# wartości faktur
x = data["WARTOSC_FV"].dropna()

n = len(x)
s = x.std(ddof=1)
s2 = s**2

print("Estymacja odchylenia standardowego wartości faktury\n")

print("Dane z próby:")
print(f"   Liczność próby n = {n}")
print(f"   Odchylenie standardowe z próby s = {s:.4f}\n")

def conf_interval(confidence):
    alpha = 1 - confidence
    chi2_lo = stats.chi2.ppf(1 - alpha/2, df=n-1)
    chi2_hi = stats.chi2.ppf(alpha/2, df=n-1)

    var_lower = (n - 1) * s2 / chi2_lo
    var_upper = (n - 1) * s2 / chi2_hi

    # przedział dla odchylenia standardowego
    lower = np.sqrt(var_lower)
    upper = np.sqrt(var_upper)

    return chi2_lo, chi2_hi, lower, upper

for conf in [0.90, 0.95, 0.99]:
    chi2_lo, chi2_hi, lower, upper = conf_interval(conf)

    print(f"{int(conf*100)}% przedział ufności:")
    print(f"   χ²_(1-α/2) = {chi2_lo:.4f}")
    print(f"   χ²_(α/2)   = {chi2_hi:.4f}")
    print(f"   Przedział dla σ: [{lower:.4f} , {upper:.4f}]\n")
