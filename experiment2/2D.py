import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("--- Descriptive Analytics using Iris Dataset ---")

# Load iris dataset using seaborn
try:
    iris = sns.load_dataset('iris')
    
    # 1. Basic info
    print("\n1. Dataset Info:")
    print(iris.info())

    # 2. Descriptive statistics
    print("\n2. Descriptive Statistics:")
    print(iris.describe())

    # 3. Value counts of species
    print("\n3. Species counts:")
    print(iris['species'].value_counts())

    # 4. Group by species and calculate mean
    print("\n4. Mean values grouped by species:")
    print(iris.groupby('species').mean())

    # 5. Visualizing descriptive stats (optional)
    print("\nGenerating Pairplot... (Window may pop up)")
    # sns.pairplot(iris, hue='species')
    # plt.title("Pairplot of Iris Dataset")
    # plt.show()
    print("Uncomment the plotting code in the script to view the pairplot visually.")

except Exception as e:
    print("Error loading dataset:", e)
