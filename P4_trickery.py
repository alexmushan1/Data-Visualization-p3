import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# alex's data story for trickery

# Load data
file_path = "indicator_bacteria_tests_datasd.csv"
df = pd.read_csv(file_path)

# Convert date_sampled to datetime
df['date_sampled'] = pd.to_datetime(df['date_sampled'], errors='coerce')

# Data preprocessing
df['month'] = df['date_sampled'].dt.month_name()
df['cl2_total'] = pd.to_numeric(df['cl2_total'], errors='coerce')
df['year'] = df['date_sampled'].dt.year
yearly = df.groupby('year')['cl2_total'].mean().reset_index()
monthly_avg = df.groupby('month', sort=False)['cl2_total'].mean().reset_index()
yearly_filtered = yearly[(yearly['year'] >= 2022) & (yearly['year'] <= 2025)]

# Order months correctly
month_order = ['January','February','March','April','May','June','July',
               'August','September','October','November','December']
monthly_avg['month'] = pd.Categorical(monthly_avg['month'], categories=month_order, ordered=True)
monthly_avg = monthly_avg.sort_values('month')

# Plot
plt.figure(figsize=(10,6))
sns.lineplot(data=yearly_filtered, x='year', y='cl2_total', marker='o')
plt.title("Average Total Chlorine Level by Year", fontsize=14, pad=15)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Average Chlorine Level Total", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()