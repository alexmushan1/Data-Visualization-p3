import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reload the dataset
file_path = "Copy of P2_Spaceship Titanic - Sheet1.csv"
df = pd.read_csv(file_path)

# Clean the data
df_clean = df.dropna(subset=['Age', 'CryoSleep'])

# Create 10-year bins from 0 to 90
bins = list(range(0, 91, 10))
labels = [f"{i}-{i+9}" for i in bins[:-1]]
df_clean['AgeGroup'] = pd.cut(df_clean['Age'], bins=bins, labels=labels, right=False)

# Calculate CryoSleep ratio per 10-year group
ratio = df_clean.groupby('AgeGroup')['CryoSleep'].mean().reset_index()
ratio['CryoSleep'] = ratio['CryoSleep'] * 100  # Convert to percentage

# Plot the line chart
plt.figure(figsize=(9, 5))
sns.lineplot(data=ratio, x='AgeGroup', y='CryoSleep', marker='o', linewidth=2.5, color='teal')

# Add labels and formatting
plt.title("CryoSleep Ratio by 10-Year Age Group on the Spaceship Titanic", fontsize=14, pad=15)
plt.xlabel("Age Group (Years)", fontsize=12)
plt.ylabel("Percentage of Passengers in CryoSleep (%)", fontsize=12)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
