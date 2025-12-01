import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
file_path = "indicator_bacteria_tests_datasd.csv"
df = pd.read_csv(file_path)

# Convert date_sampled to datetime
df['date_sampled'] = pd.to_datetime(df['date_sampled'], errors='coerce')

# Extract month and year, convert cl2_total to numeric
df['month'] = df['date_sampled'].dt.month_name()
df['cl2_total'] = pd.to_numeric(df['cl2_total'], errors='coerce')
df['year'] = df['date_sampled'].dt.year
yearly = df.groupby('year')['cl2_total'].mean().reset_index()
monthly_avg = df.groupby('month', sort=False)['cl2_total'].mean().reset_index()

# Ensure months are in calendar order
month_order = ['January','February','March','April','May','June','July',
               'August','September','October','November','December']
monthly_avg['month'] = pd.Categorical(monthly_avg['month'], categories=month_order, ordered=True)
monthly_avg = monthly_avg.sort_values('month')

# Plot
plt.figure(figsize=(10,6))
sns.lineplot(data=yearly, x='year', y='cl2_total', marker='o')
'''
sns.lineplot(data=monthly_avg, x='month', y='cl2_total', marker='o', color='#1f77b4')
plt.title("Average Total Chlorine (Cl₂ Total) by Month", fontsize=14, pad=15)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Cl₂ Total", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
'''
plt.show()