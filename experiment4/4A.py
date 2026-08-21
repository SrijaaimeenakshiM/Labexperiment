import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.datasets import load_diabetes

print("--- Data Visualization: Normal Curves on UCI Diabetes Dataset ---")

# Load UCI dataset
diabetes_uci = load_diabetes(as_frame=True)
df_uci = diabetes_uci.frame

# Select a continuous variable, e.g., 'bmi'
feature = 'bmi'
data = df_uci[feature]

# Fit a normal distribution to the data
mu, std = stats.norm.fit(data)

# Plot the histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=25, density=True, alpha=0.6, color='skyblue', edgecolor='black')

# Plot the Normal curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2, label=f'Normal curve (mu={mu:.2f}, std={std:.2f})')

plt.title(f'Histogram and Normal Curve for {feature.upper()}')
plt.xlabel(feature.upper())
plt.ylabel('Density')
plt.legend()

print(f"Normal curve parameters for '{feature}': mean = {mu:.4f}, std = {std:.4f}")
plt.savefig('s:/A/lab_Experiments/dav/experiment4/4A_plot.png')
print("Plot generated and saved as 4A_plot.png.")
