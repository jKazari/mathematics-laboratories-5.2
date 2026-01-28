from scipy import stats
import numpy as np

mu = 487
sigma = 98

norm_dist = stats.norm(loc=mu, scale=sigma)

# a. Jaki procent studentów uzyska wyniki powyżej 500?
print("a. Procent studentów z wynikami powyżej 500:")
# P(X > 500) = 1 - P(X <= 500) = 1 - CDF(500)
prob_above_500 = 1 - norm_dist.cdf(500)
percent_above_500 = prob_above_500 * 100
print(f"   P(X > 500) = {prob_above_500:.6f}")
print(f"   Odpowiedź: {percent_above_500:.2f}%\n")

# b. Jaki procent studentów uzyska wynik między 600 a 700?
print("b. Procent studentów z wynikami między 600 a 700:")
# P(600 < X < 700) = CDF(700) - CDF(600)
prob_between_600_700 = norm_dist.cdf(700) - norm_dist.cdf(600)
percent_between_600_700 = prob_between_600_700 * 100
print(f"   P(600 < X < 700) = {prob_between_600_700:.6f}")
print(f"   Odpowiedź: {percent_between_600_700:.2f}%\n")

# c. Graniczna minimalna liczba punktów dla 75% najlepszych
print("c. Minimalna liczba punktów dla 75% najlepszych:")
min_score_top_75 = norm_dist.ppf(0.25)
print(f"   Percentyl 25%: {min_score_top_75:.2f}")
print(f"   Odpowiedź: {min_score_top_75:.2f} punktów\n")

# d. Największy przedział zawierający wyniki 75% studentów
print("d. Największy przedział zawierający 75% studentów:")
lower_bound = norm_dist.ppf(0.125)
upper_bound = norm_dist.ppf(0.875)
interval_width = upper_bound - lower_bound
print(f"   Dolna granica (12.5%): {lower_bound:.2f}")
print(f"   Górna granica (87.5%): {upper_bound:.2f}")
print(f"   Przedział: [{lower_bound:.2f}, {upper_bound:.2f}]")
print(f"   Szerokość przedziału: {interval_width:.2f}\n")