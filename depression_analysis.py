#Dataset using from https://www.kaggle.com/datasets/anthonytherrien/depression-dataset?resource=download

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
file_path = 'depression_data.csv'
depression_data = pd.read_csv(file_path)

# Set plot style
sns.set(style="whitegrid")

# 1. Histogram: Age distribution
plt.figure(figsize=(10, 6))
sns.histplot(depression_data['Age'], kde=True, bins=30, color='blue')
plt.title('Age Distribution', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()

# 2. Box Plot: Income distribution
plt.figure(figsize=(10, 6))
sns.boxplot(x=depression_data['Family History of Depression'], y=depression_data['Income'], palette="Set2")
plt.title('Income Distribution by Family History of Depression', fontsize=16)
plt.xlabel('Family History of Depression', fontsize=12)
plt.ylabel('Income', fontsize=12)
plt.ylim(0, 150000)  # Limit to reduce the impact of outliers
plt.show()

# 3. Scatter Plot: Age vs Income relationship
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Income', hue='Family History of Depression', data=depression_data, palette='Set1', alpha=0.6)
plt.title('Age vs Income Relationship (by Family History of Depression)', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Income', fontsize=12)
plt.ylim(0, 150000)
plt.legend(title='Family History of Depression')
plt.show()
