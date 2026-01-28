from scipy import stats
import numpy as np

mu = 15.6
sigma = 4.1

norm_dist = stats.norm(loc=mu, scale=sigma)

# Prawdopodobieństwo, że drukarka będzie działać bez awarii przynajmniej 500 godzin.
print("Prawdopodobieństwo, że drukarka będzie działać bez awarii przynajmniej 500 godzin:")
# P(X > x1) = 0.95
x1 = norm_dist.ppf(0.05)
print(f"x1 = {x1:.2f} kW")