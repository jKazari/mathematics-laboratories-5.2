import pandas as pd
import numpy as np
from scipy import stats

# wczytanie danych
data = pd.read_excel(r"C:\Users\Kazari\Desktop\data.xlsx")

# powierzchnia mieszkań (ft^2)
area = data["TOT_LIVING_AREA (stopy kw)"].dropna()

n = len(area)

# liczba mieszkań w przedziale 1500–2200
x = ((area >= 1500) & (area <= 2200)).sum()

# estymator punktowy
p_hat = x / n

print("Estymacja udziału mieszkań 1500–2200 ft²\n")

print("Dane z próby:")
print(f"   Liczność próby n = {n}")
print(f"   Liczba mieszkań w przedziale = {x}")
print(f"   Estymator punktowy p̂ = {p_hat:.4f}\n")

# funkcja do przedziału ufności dla proporcji
def conf_interval(confidence):
    alpha = 1 - confidence
    z = stats.norm.ppf(1 - alpha/2)
    SE = np.sqrt(p_hat * (1 - p_hat) / n)
    margin = z * SE
    lower = p_hat - margin
    upper = p_hat + margin
    return z, SE, margin, lower, upper

# 90%, 95%, 99%
for conf in [0.90, 0.95, 0.99]:
    z, SE, margin, lower, upper = conf_interval(conf)

    print(f"{int(conf*100)}% przedział ufności:")
    print(f"   z_(α/2) = {z:.4f}")
    print(f"   Błąd standardowy SE = {SE:.5f}")
    print(f"   Margines błędu = {margin:.5f}")
    print(f"   Przedział: [{lower:.4f} , {upper:.4f}]\n")
