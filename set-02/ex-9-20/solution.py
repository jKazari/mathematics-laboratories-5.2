from scipy import stats
import numpy as np

# Parametry Alison
mu_A = 37
sigma_A = 1

# Parametry Julie
mu_J = 33
sigma_J = 2

# Parametry różnicy D = A - J
mu_D = mu_A - mu_J
sigma_D = np.sqrt(sigma_A**2 + sigma_J**2)

diff = stats.norm(loc=mu_D, scale=sigma_D)

print("Rozkład różnicy D = A - J:")
print(f"   Średnia = {mu_D}")
print(f"   Odchylenie standardowe = {sigma_D:.4f}\n")

# P(A < J) = P(D < 0)
print("Prawdopodobieństwo, że Alison wygra:")

prob_win = diff.cdf(0)
percent_win = prob_win * 100

print(f"   P(A < J) = P(D < 0) = {prob_win:.6f}")
print(f"   Odpowiedź: {percent_win:.2f}%")
