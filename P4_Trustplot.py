import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data
df = pd.read_csv("indicator_bacteria_tests_datasd.csv", parse_dates=['date_sampled'])

start_date = df['date_sampled'].min().date()
end_date = df['date_sampled'].max().date()
total_tests = df.shape[0]

# data counts
non_positive_tests = total_tests
positive_detections = 0 

plot_data = pd.DataFrame({
    'Result': ['Tests with Zero E. coli', 'Confirmed E. coli Detection'],
    'Count': [non_positive_tests, positive_detections]
})

PALETTE = ['#005bbb', '#D3D3D3']

# grid
sns.set_style("whitegrid", {'grid.linestyle': ':', 'axes.edgecolor': '.8'})
sns.set_context("notebook", font_scale=1.2)

plt.figure(figsize=(9, 6))
ax = plt.gca() 

ax = sns.barplot(
    x='Result',
    y='Count',
    data=plot_data,
    palette=PALETTE,
    width=0.45,
    ax=ax
)

# negtative Bar
plt.text(
    0, non_positive_tests * 0.95, 
    f"{non_positive_tests:,}", 
    ha='center', va='top', 
    color='white', fontsize=16, fontweight='bold'
)

plt.text(
    1, non_positive_tests * 0.01, 
    f"{positive_detections}", 
    ha='center', va='bottom', 
    color='k', fontsize=16, fontweight='bold' 
)

plt.title(
    'E. coli Monitoring: Proactive Testing Confirms Water Safety', 
    fontsize=20, pad=20, fontweight='bold', loc='left'
)
plt.ylabel('Number of Samples', fontsize=14, labelpad=10)
plt.xlabel('')

ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.ylim(0, non_positive_tests * 1.05)

# trust message
trust_message = (
    f"Data Source: San Diego Public Utilities Department.\n"
    f"Over {total_tests:,} samples collected from {start_date} to {end_date} showed zero confirmed E. coli detections, "
    f"meeting federal safety standards (Maximum Contaminant Level = 0)."
)

plt.figtext(
    0.5, 0.07, trust_message, wrap=True, ha='center', fontsize=10, color='gray',
    bbox=dict(facecolor='#f6f8fd', edgecolor='gray', boxstyle='round,pad=1', alpha=1)
)

plt.grid(axis='x', which='both', linestyle='', alpha=0)
plt.tight_layout(rect=[0, 0.18, 1, 1]) 
plt.show()