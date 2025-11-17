import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("parking_citations_2025_part2_datasd.csv")

plt.scatter(df.index, df['vio_fine'])
plt.xlabel('Index')
plt.ylabel('vio_fine')
plt.title('Scatter Plot of vio_fine by Index')
plt.show()


