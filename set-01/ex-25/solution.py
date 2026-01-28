import pandas as pd
import numpy as np
from scipy import stats

# wczytanie danych
data = pd.read_csv(r"C:\Users\zacha\Repositories\mathematics-laboratories-5.2\set-01\ex-25\data.csv")

women = data[data["PŁEĆ"] == "KOBIETA"]["PRACE DOMOWE"].dropna()
men   = data[data["PŁEĆ"] == "MĘŻCZYZNA"]["PRACE DOMOWE"].dropna()

n_w = len(women)
n_m = len(men)

mean_w = women.mean()
mean_m = men.mean()

s_w = women.std(ddof=1)
s_m = men.std(ddof=1)

# test Welcha (jednostronny: kobiety > mężczyźni)
SE = np.sqrt(s_w**2 / n_w + s_m**2 / n_m)
t_stat = (mean_w - mean_m) / SE

df = (s_w**2 / n_w + s_m**2 / n_m)**2 / (
    (s_w**2 / n_w)**2 / (n_w - 1) + (s_m**2 / n_m)**2 / (n_m - 1)
)

p_value = 1 - stats.t.cdf(t_stat, df)

print("Kobiety vs mężczyźni")
print(f"   n_K = {n_w},  x̄_K = {mean_w:.4f},  s_K = {s_w:.4f}")
print(f"   n_M = {n_m},  x̄_M = {mean_m:.4f},  s_M = {s_m:.4f}")
print(f"   t = {t_stat:.4f},  df = {df:.2f},  p-value = {p_value:.6f}")

if p_value < 0.05:
    print("   Odrzucamy H0 (kobiety poświęcają więcej czasu)\n")
else:
    print("   Brak podstaw do odrzucenia H0\n")

east = data[data["REGION"] == "WSCHÓD"]["PRACE DOMOWE"].dropna()
west = data[data["REGION"] == "ZACHÓD"]["PRACE DOMOWE"].dropna()

n_e = len(east)
n_z = len(west)

mean_e = east.mean()
mean_z = west.mean()

s_e = east.std(ddof=1)
s_z = west.std(ddof=1)

# test Welcha (jednostronny: wschód > zachód)
SE = np.sqrt(s_e**2 / n_e + s_z**2 / n_z)
t_stat = (mean_e - mean_z) / SE

df = (s_e**2 / n_e + s_z**2 / n_z)**2 / (
    (s_e**2 / n_e)**2 / (n_e - 1) + (s_z**2 / n_z)**2 / (n_z - 1)
)

p_value = 1 - stats.t.cdf(t_stat, df)

print("Wschód vs zachód")
print(f"   n_W = {n_e},  x̄_W = {mean_e:.4f},  s_W = {s_e:.4f}")
print(f"   n_Z = {n_z},  x̄_Z = {mean_z:.4f},  s_Z = {s_z:.4f}")
print(f"   t = {t_stat:.4f},  df = {df:.2f},  p-value = {p_value:.6f}")

if p_value < 0.05:
    print("   Odrzucamy H0 (wschód poświęca więcej czasu)")
else:
    print("   Brak podstaw do odrzucenia H0")
