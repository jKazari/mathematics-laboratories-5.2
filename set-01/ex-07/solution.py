import numpy as np
from scipy import stats

# Dane
n = 255
x = 149   # liczba oglądających
alpha = 0.05

p_hat = x / n

print("Estymacja udziału gospodarstw oglądających wiadomości\n")

print("Dane:")
print(f"   Liczność próby n = {n}")
print(f"   Liczba oglądających = {x}")
print(f"   Estymator punktowy p̂ = {p_hat:.4f}\n")

# wartość krytyczna z
z = stats.norm.ppf(1 - alpha/2)

# błąd standardowy
SE = np.sqrt(p_hat * (1 - p_hat) / n)

# margines błędu
margin = z * SE

lower = p_hat - margin
upper = p_hat + margin

print("Parametry:")
print(f"   z_(α/2) = {z:.4f}")
print(f"   Błąd standardowy SE = {SE:.5f}")
print(f"   Margines błędu = {margin:.5f}\n")

print("95% przedział ufności dla udziału oglądających:")
print(f"   [{lower:.4f} , {upper:.4f}]")
print(f"   czyli [{lower*100:.2f}% , {upper*100:.2f}%]")
