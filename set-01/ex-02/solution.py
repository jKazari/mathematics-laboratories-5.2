import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_csv(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-01\ex-02\data.csv")

prices = data.iloc[:, 12].dropna()   # 13. kolumna (indeks 12)

n = len(prices)
mean = prices.mean()
std = prices.std(ddof=1)   # odchylenie standardowe z próby

print("Dane z próby:")
print(f"   Liczność próby n = {n}")
print(f"   Średnia z próby x̄ = {mean:.2f}")
print(f"   Odchylenie standardowe s = {std:.2f}\n")

def confidence_interval(confidence):
    alpha = 1 - confidence
    t_crit = stats.t.ppf(1 - alpha/2, df=n-1)   # kwantyl t-Studenta
    SE = std / np.sqrt(n)                      # błąd standardowy
    margin = t_crit * SE
    lower = mean - margin
    upper = mean + margin
    return t_crit, SE, margin, lower, upper

for conf in [0.90, 0.95, 0.99]:
    t_crit, SE, margin, lower, upper = confidence_interval(conf)

    print(f"{int(conf*100)}% przedział ufności:")
    print(f"   t_(α/2) = {t_crit:.4f}")
    print(f"   Błąd standardowy SE = {SE:.4f}")
    print(f"   Margines błędu = {margin:.4f}")
    print(f"   Przedział: [{lower:.2f} , {upper:.2f}]\n")
