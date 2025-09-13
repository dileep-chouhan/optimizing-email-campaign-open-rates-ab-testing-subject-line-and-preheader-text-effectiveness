import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
np.random.seed(42)  # for reproducibility
# Define subject lines and preheader texts
subject_lines = ['Exciting News!', 'Check Out This Deal!', 'Limited Time Offer!']
preheader_texts = ['Don\'t miss out!', 'Shop now and save!', 'Act fast!']
# Generate synthetic data
num_emails = 1000
data = {
    'Subject Line': np.random.choice(subject_lines, size=num_emails),
    'Preheader Text': np.random.choice(preheader_texts, size=num_emails),
    'Opened': np.random.binomial(1, 0.2, size=num_emails) # 20% open rate on average
}
df = pd.DataFrame(data)
# --- 2. Data Analysis ---
# Calculate open rates for each combination
open_rates = df.groupby(['Subject Line', 'Preheader Text'])['Opened'].mean().reset_index()
open_rates['Open Rate (%)'] = open_rates['Opened'] * 100
# Find the best performing combination
best_combination = open_rates.loc[open_rates['Opened'].idxmax()]
# --- 3. Visualization ---
plt.figure(figsize=(12, 6))
sns.barplot(x='Subject Line', y='Opened', hue='Preheader Text', data=df)
plt.title('Email Open Rates by Subject Line and Preheader Text')
plt.xlabel('Subject Line')
plt.ylabel('Open Rate')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
#Save the plot
output_filename = 'open_rates_barplot.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
print("\n--- Analysis Results ---")
print("Open Rates:")
print(open_rates)
print(f"\nBest Performing Combination:\n{best_combination}")
#Further analysis could involve statistical tests (e.g., chi-squared test) to determine statistical significance of differences in open rates.  This example focuses on basic descriptive statistics and visualization.