# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Set the style for the plots
sns.set_theme(style="whitegrid")

# Load the built-in "tips" dataset
# If you downloaded it from Kaggle, you would use: df = pd.read_csv('tips.csv')
df = sns.load_dataset("tips")

# --- 1. Bar Plot: Average Total Bill by Day ---
# This plot helps us compare a numeric value across different categories.
plt.figure(figsize=(10, 6))
sns.barplot(x='day', y='total_bill', data=df, palette='viridis', hue='day', dodge=False, legend=False)
plt.title('Average Total Bill by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Total Bill ($)')
plt.savefig('avg_bill_by_day.png') # Save the figure
plt.show()

# --- 2. Scatter Plot: Relationship between Total Bill and Tip ---
# This shows the relationship and correlation between two numeric variables.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_bill', y='tip', data=df, hue='time', style='time', s=100)
plt.title('Relationship between Total Bill and Tip Amount')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip Amount ($)')
plt.savefig('bill_vs_tip_scatter.png') # Save the figure
plt.show()

# --- 3. Box Plot: Distribution of Bills by Smoker Status ---
# A box plot is excellent for visualizing the distribution (median, quartiles, outliers) of a numeric variable.
plt.figure(figsize=(10, 6))
sns.boxplot(x='smoker', y='total_bill', data=df, palette='coolwarm', hue='smoker', legend=False)
plt.title('Distribution of Total Bills for Smokers vs. Non-Smokers')
plt.xlabel('Smoker')
plt.ylabel('Total Bill ($)')
plt.savefig('bill_dist_smoker.png') # Save the figure
plt.show()

# --- 4. Violin Plot + Swarm Plot: Tip Distribution by Day ---
# A violin plot shows the probability density of the data at different values.
# Combining it with a swarm plot shows the individual data points.
plt.figure(figsize=(12, 7))
sns.violinplot(x='day', y='tip', data=df, palette='pastel', hue='day', legend=False)
sns.swarmplot(x='day', y='tip', data=df, color='black', alpha=0.5) # Overlay swarm plot
plt.title('Distribution of Tips by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Tip Amount ($)')
plt.savefig('tip_dist_by_day.png') # Save the figure
plt.show()

# --- 5. KDE Plot: Distribution of Total Bills ---
# A Kernel Density Estimate (KDE) plot visualizes the distribution of a single variable.
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='total_bill', fill=True, color='purple', hue='time', multiple="stack")
plt.title('Density Distribution of Total Bills')
plt.xlabel('Total Bill ($)')
plt.ylabel('Density')
plt.savefig('bill_kde.png') # Save the figure
plt.show()