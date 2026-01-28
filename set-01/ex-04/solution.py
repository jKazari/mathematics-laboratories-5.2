import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_csv(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-01\ex-04\data.csv")

# Kolumna "Kwota" = wielkość kredytu
x = data["Kwota"].dropna()

n = len(x)
mu_hat = x.mean()
s = x.std(ddof=1)

print("Dane z próby:")
print(f"   Liczność próby n = {n}")
print(f"   Średnia z próby x̄ = {mu_hat:.4f}")
print(f"   Odchylenie standardowe s = {s:.4f}\n")

def confidence_interval(confidence):
    alpha = 1 - confidence
    z = stats.norm.ppf(1 - alpha/2)
    SE = s / np.sqrt(n)
    margin = z * SE
    lower = mu_hat - margin
    upper = mu_hat + margin
    return z, SE, margin, lower, upper

for conf in [0.90, 0.95, 0.99]:
    z, SE, margin, lower, upper = confidence_interval(conf)

    print(f"{int(conf*100)}% przedział ufności:")
    print(f"   z_(α/2) = {z:.4f}")
    print(f"   Błąd standardowy SE = {SE:.4f}")
    print(f"   Margines błędu = {margin:.4f}")
    print(f"   Przedział: [{lower:.2f} , {upper:.2f}]\n")
