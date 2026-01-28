from scipy import stats
import numpy as np

mu = 549
sigma = 68

norm_dist = stats.norm(loc=mu, scale=sigma)

# Prawdopodobieństwo, że drukarka będzie działać bez awarii przynajmniej 500 godzin.
print("Prawdopodobieństwo, że drukarka będzie działać bez awarii przynajmniej 500 godzin:")
# P(X > 500) = 1 - P(X <= 500) = 1 - CDF(500)
prob_above_500 = 1 - norm_dist.cdf(500)
print(f"P(X > 500) = {prob_above_500:.6f}")