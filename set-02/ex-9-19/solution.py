from scipy import stats
import numpy as np

# Parametry czasu dojazdu
mu_X = 25
sigma_X = 3

# Parametry czasu na lotnisku
mu_Y = 15
sigma_Y = 2

# Parametry sumy
mu_T = mu_X + mu_Y
sigma_T = np.sqrt(sigma_X**2 + sigma_Y**2)

total_time = stats.norm(loc=mu_T, scale=sigma_T)

print("Rozkład całkowitego czasu:")
print(f"   Średnia = {mu_T}")
print(f"   Odchylenie standardowe = {sigma_T:.4f}\n")

# Prawdopodobieństwo spóźnienia (T > 45)
print("Prawdopodobieństwo spóźnienia się Meg:")

prob_late = 1 - total_time.cdf(45)
percent_late = prob_late * 100

print(f"   P(T > 45) = {prob_late:.6f}")
print(f"   Odpowiedź: {percent_late:.2f}%")
