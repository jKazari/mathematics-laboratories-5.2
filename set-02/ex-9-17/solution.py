from scipy import stats
import numpy as np

mu = 55.7
sigma = 11.5

norm_dist = stats.norm(loc=mu, scale=sigma)

# a) Prawdopodobieństwo złapania nielegalnego żółwia
print("a. Prawdopodobieństwo złapania nielegalnego żółwia:")

# P(40 < X < 60)
prob_legal = norm_dist.cdf(60) - norm_dist.cdf(40)

# P(nielegalny) = 1 - P(legalny)
prob_illegal = 1 - prob_legal
percent_illegal = prob_illegal * 100

print(f"   P(40 < X < 60) = {prob_legal:.6f}")
print(f"   P(nielegalny) = {prob_illegal:.6f}")
print(f"   Odpowiedź: {percent_illegal:.2f}%\n")

# b) Limit L dla którego tylko 10% jest większe
print("b. Maksymalny limit L taki, że tylko 10% żółwi go przekracza:")

# P(X <= L) = 0.90
L = norm_dist.ppf(0.90)

print(f"   Percentyl 90%: {L:.2f}")
print(f"   Odpowiedź: L = {L:.2f} cm")