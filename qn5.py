import pandas as pd
import matplotlib.pyplot as plt
import csv
from collections import defaultdict
import os

# --- Helper Function for 5.2 (Using loops and the standard 'csv' library) ---
def compute_sales_metrics(filename):
    """
    Computes total sales and monthly sales aggregates using pure Python loops.
    """
    total_sales = 0
    # Use defaultdict to easily aggregate sales per month
    monthly_totals = defaultdict(int)
    number_of_months = set()

    print("\n" + "="*50)
    print("5.2 COMPUTATION (Using Loops and Functions)")
    print("="*50)

    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                try:
                    month, region, sales_str = row
                    sales = int(sales_str)

                    # a. Total sales across all regions and months
                    total_sales += sales

                    # Aggregate monthly totals
                    monthly_totals[month] += sales

                    # Track the unique months present
                    number_of_months.add(month)

                except ValueError:
                    print(f"Warning: Skipped row due to invalid sales data: {row}")
                except IndexError:
                    print(f"Warning: Skipped row due to incorrect column structure: {row}")

        # b. The average sales per month (Interpreted as average of total monthly sales)
        num_unique_months = len(number_of_months)
        if num_unique_months > 0:
            total_monthly_sales_sum = sum(monthly_totals.values())
            average_sales_per_month = total_monthly_sales_sum / num_unique_months
        else:
            average_sales_per_month = 0
            print("No sales data found to compute average.")

        # Display results for 5.2
        print(f"a. The total sales across all regions and months: ${total_sales:,.2f}")
        print("-" * 50)
        print("Monthly Total Sales:")
        for month, total in monthly_totals.items():
            print(f"  {month}: ${total:,.2f}")
        print("-" * 50)
        print(f"b. The overall average sales per month (Avg of Monthly Totals): ${average_sales_per_month:,.2f}")
        print("="*50)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please ensure it is in the correct directory.")
        return None, None, None

    return monthly_totals, total_sales

# --- Main Analysis Script ---
FILE_PATH = 'sales_data.csv'

# Check if the CSV file exists
if not os.path.exists(FILE_PATH):
    print(f"Error: The required file '{FILE_PATH}' does not exist.")
    print("Please ensure you have generated the 'sales_data.csv' file.")
else:
    # 5.1 Read the CSV file and display its content in a structured format (using pandas)
    try:
        df = pd.read_csv(FILE_PATH)

        print("5.1 CSV File Content (Structured Format):")
        print("="*50)
        # Display the DataFrame content
        print(df.to_string(index=False))
        print("="*50)

    except Exception as e:
        print(f"An error occurred while reading the CSV with pandas: {e}")
        exit()

    # 5.2 Compute using loops and functions
    monthly_totals, total_sales = compute_sales_metrics(FILE_PATH)

    if monthly_totals is not None:
        # --- 5.3 & 5.4 & 5.5: Generate Charts with Proper Labels ---

        # 5.3 Generate a bar chart showing monthly sales distribution (Total Sales Per Month)
        # We can use the data calculated in 5.2 or re-aggregate with pandas
        monthly_df = pd.DataFrame(monthly_totals.items(), columns=['Month', 'Total Sales'])

        plt.figure(figsize=(10, 6))
        plt.bar(
            monthly_df['Month'],
            monthly_df['Total Sales'],
            color=['#4C72B0', '#55A868', '#C44E52', '#8172B2'], # Custom colors
            edgecolor='black'
        )
        # 5.5 Labels and Title
        plt.title('Monthly Sales Distribution', fontsize=16, fontweight='bold')
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Total Sales (USD)', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()


        # 5.4 Create a pie chart representing the proportion of total sales by region
        regional_totals = df.groupby('Region')['Sales'].sum()

        plt.figure(figsize=(8, 8))
        plt.pie(
            regional_totals,
            labels=regional_totals.index,
            autopct='%1.1f%%',  # Show percentage up to one decimal place
            startangle=90,
            wedgeprops={'edgecolor': 'black', 'linewidth': 1.5},
            # Use 'viridis' color map for distinct colors
            colors=plt.cm.viridis(regional_totals.index.map(lambda x: hash(x) % 10 / 10))
        )
        # 5.5 Labels and Title
        plt.title('Proportion of Total Sales by Region', fontsize=16, fontweight='bold')
        plt.axis('equal')  # Ensures the pie chart is circular
        plt.legend(title="Regions", loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))
        plt.tight_layout()
        plt.show()