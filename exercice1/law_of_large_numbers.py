import numpy as np
import matplotlib.pyplot as plt

# X is height (m), Y is average winter temp (°C)

def sample_Z(n):
    # Draw samples from normal distributions
    X = np.random.normal(3, 1, n)
    Y = np.random.normal(-2, 2, n)
    return np.column_stack((X, Y))

expected_value = np.array([3, -2])  # Theoretical mean

n_points = 1000  # Number of samples
samples = sample_Z(n_points)

plt.figure(figsize=(6, 6))
plt.scatter(samples[:, 0], samples[:, 1], alpha=0.5, s=10)
plt.title("Samples of Z = (X, Y)")
plt.xlabel("X (height in m)")
plt.ylabel("Y (winter temp °C)")
plt.grid(True)
plt.tight_layout()
plt.savefig("scatter_samples.png")
plt.show()

# Calculate empirical means and distance to expected value
ns = np.arange(1, n_points + 1)
emp_means = []
for n in ns:
    emp_means.append(np.mean(samples[:n], axis=0))
emp_means = np.array(emp_means)

dists = np.linalg.norm(emp_means - expected_value, axis=1)

plt.figure(figsize=(8, 4))
plt.plot(ns, dists)
plt.title("Distance between empirical mean and expected value")
plt.xlabel("Number of samples")
plt.ylabel("Euclidean distance")
plt.grid(True)
plt.tight_layout()
plt.savefig("convergence_plot.png")
plt.show()