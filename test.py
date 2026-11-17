# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Generate small sample data
rng = np.random.default_rng(10)
df = pd.DataFrame({
    'city': ['Lagos', 'Abuja', 'Kano', 'Ibadan', 'Port Harcourt'],
    'sales_m': [14.2, 9.8, 6.4, 5.1, 7.3]
}).sort_values(by='sales_m', ascending=False)

# 2. Build a clean bar chart following your Module 4 standards
colors = ['#1f77b4' if i == 0 else '#b0b0b0' for i in range(len(df))]

fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(df['city'], df['sales_m'], color=colors)
ax.set_title(f"Lagos Leads Regional Sales at ₦{df['sales_m'].iloc[0]}M", fontsize=12, fontweight='bold')
ax.set_xlabel('City')
ax.set_ylabel('Sales (₦ Millions)')
ax.grid(True, axis='y', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.tight_layout()

# 3. Save to disk AND trigger display window
fig.savefig('experiment_chart.png', dpi=150)
print("Saved 'experiment_chart.png' to your project folder.")
print("Opening chart window now (close the pop-up window to let the script finish)...")

plt.show()
print("Script finished cleanly!")
