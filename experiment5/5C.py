import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

print("--- Model Building and Validation: Time Series Analysis ---")

# We will generate a dummy time series dataset for this, 
# as typical diabetes datasets are cross-sectional, not temporal.
print("Generating temporal dummy dataset (Monthly Sales over 3 years)...")
date_rng = pd.date_range(start='1/1/2020', end='12/01/2022', freq='MS')

np.random.seed(42)
trend = np.linspace(10, 50, len(date_rng))
seasonality = 10 * np.sin(np.linspace(0, 3.14 * 6, len(date_rng)))
noise = np.random.normal(0, 2, len(date_rng))
sales = trend + seasonality + noise

ts_df = pd.DataFrame({'Date': date_rng, 'Sales': sales})
ts_df.set_index('Date', inplace=True)

print("\n1. First 5 rows of Time Series Data:")
print(ts_df.head())

# Perform Seasonal Decomposition
print("\n2. Performing Seasonal Decomposition (Trend, Seasonal, Residual)...")
decomposition = seasonal_decompose(ts_df['Sales'], model='additive', period=12)

# Plotting the decomposition
plt.figure(figsize=(10, 8))

plt.subplot(411)
plt.plot(ts_df['Sales'], label='Original Time Series')
plt.legend(loc='upper left')
plt.title('Time Series Decomposition')

plt.subplot(412)
plt.plot(decomposition.trend, label='Trend Component', color='orange')
plt.legend(loc='upper left')

plt.subplot(413)
plt.plot(decomposition.seasonal, label='Seasonal Component', color='green')
plt.legend(loc='upper left')

plt.subplot(414)
plt.plot(decomposition.resid, label='Residuals (Noise)', color='red')
plt.legend(loc='upper left')

plt.tight_layout()

print("\nAnalysis complete. Data decomposed into Trend, Seasonality, and Residuals.")
plt.savefig('s:/A/lab_Experiments/dav/experiment5/5C_plot.png')
print("Decomposition plot saved as 5C_plot.png.")

# Basic Moving Average (Rolling window)
ts_df['SMA_3_Months'] = ts_df['Sales'].rolling(window=3).mean()
print("\n3. Last 5 rows with 3-Month Simple Moving Average (SMA):")
print(ts_df.tail())
