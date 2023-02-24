import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel file
data = pd.read_excel('sales_data.xlsx')

# Extract columns of interest
monthly_sales = data[['Month', 'Total Sales']]

# Group sales by month
monthly_sales_grouped = monthly_sales.groupby('Month').sum()

# Create line chart of monthly sales
monthly_sales_grouped.plot(kind='line', legend=None)
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

# Calculate average sales per day
total_sales = data['Total Sales'].sum()
num_days = len(data)
avg_sales_per_day = total_sales / num_days

print('Average sales per day:', avg_sales_per_day)

