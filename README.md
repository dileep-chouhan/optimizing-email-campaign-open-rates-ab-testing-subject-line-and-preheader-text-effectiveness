# Optimizing Email Campaign Open Rates: A/B Testing Subject Line and Preheader Text Effectiveness

## Overview

This project analyzes the results of an A/B test conducted on email subject lines and preheader text to determine the most effective combination for maximizing open rates and, consequently, conversion rates.  The analysis utilizes data from the A/B test to identify statistically significant differences between various subject line and preheader text pairings. The results provide actionable insights for future email marketing campaigns.

## Technologies Used

* Python 3
* Pandas
* Matplotlib
* Seaborn

## How to Run

1. **Install Dependencies:**  Navigate to the project directory in your terminal and install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Analysis:** Execute the main script using:

   ```bash
   python main.py
   ```

## Example Output

The script will print a summary of the A/B test results to the console, including key statistics such as open rates for each variation and p-values from statistical tests used to determine significance.  Additionally, the script will generate the following visualization:

* **`open_rate_comparison.png`**: A bar chart visualizing the open rates for each subject line and preheader text combination, allowing for easy comparison of performance.

This output provides a clear understanding of which subject line and preheader text combination yielded the highest open rates and whether the difference is statistically significant.  This information can be used to inform future email marketing strategies.