from scipy import stats
import numpy as np

mu = 1870
sigma = 625

norm_dist = stats.norm(loc=mu, scale=sigma)

print("Dolna granica wydatków 20% tych osób, które wydają w centrach najwięcej:")
# P(X > x1) = 0.2
x1 = norm_dist.ppf(0.8)
print(f"x1 = {x1:.2f} zł/miesiąc")