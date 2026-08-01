import sys
import subprocess

def install_packages():
    """
    Downloads and installs required packages if not already installed.
    """
    print("Installing packages...")
    packages = ['numpy', 'scipy', 'jupyter', 'statsmodels', 'pandas', 'matplotlib', 'seaborn', 'plotly', 'bokeh']
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + packages)

# Uncomment the line below to automatically install packages when running the script
# install_packages()

import numpy as np
import scipy
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import bokeh

print("--- Package Exploration ---")
print("NumPy version:", np.__version__)
print("SciPy version:", scipy.__version__)
print("Pandas version:", pd.__version__)
print("Statsmodels version:", sm.__version__)
print("Matplotlib version:", plt.matplotlib.__version__)
print("Seaborn version:", sns.__version__)
print("Plotly version:", plotly.__version__)
print("Bokeh version:", bokeh.__version__)
print("Exploration of libraries completed.")
