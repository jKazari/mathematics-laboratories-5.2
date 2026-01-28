from scipy import stats
import numpy as np

mu = 1870
sigma = 625

dist = stats.norm(loc=mu, scale=sigma)

# a) P(X < 1400)
print("a. Udział klientów wydających mniej niż 1400 zł:")

p_a = dist.cdf(1400)
print(f"   P(X < 1400) = {p_a:.6f}")
print(f"   Odpowiedź: {p_a*100:.2f}%\n")

# b) P(X > 2000)
print("b. Udział klientów wydających więcej niż 2000 zł:")

p_b = 1 - dist.cdf(2000)
print(f"   P(X > 2000) = {p_b:.6f}")
print(f"   Odpowiedź: {p_b*100:.2f}%\n")

# c) P(500 < X < 1000)
print("c. Udział klientów wydających między 500 a 1000 zł:")

p_c = dist.cdf(1000) - dist.cdf(500)
print(f"   P(500 < X < 1000) = {p_c:.6f}")
print(f"   Odpowiedź: {p_c*100:.2f}%\n")

# d) Dolna granica dla top 20%
print("d. Dolna granica wydatków dla 20% najwięcej wydających:")

# P(X >= L) = 0.20  ->  P(X <= L) = 0.80
L = dist.ppf(0.80)

print(f"   Percentyl 80%: {L:.2f}")
print(f"   Odpowiedź: L = {L:.2f} zł")