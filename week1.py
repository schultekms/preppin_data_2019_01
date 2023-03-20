import pandas as pd

# Load the data into a Pandas dataframe
df = pd.read_csv('2019 Week 1.csv')

# Group the car sales per colour columns by dealership and when_sold_date
df_sales_per_colour = df.groupby(['Dealership', 'When_Sold_Year', 'When_Sold_Month'])[['Red_Cars', 'Silver_Cars', 'Black_Cars', 'Blue_Cars']].sum().reset_index()

# Combine the month and year columns into a single date column
df_sales_per_colour['When_Sold_Date'] = pd.to_datetime(df_sales_per_colour['When_Sold_Year'].astype(str) + '-' + df_sales_per_colour['When_Sold_Month'].astype(str), format='%Y-%m')

# Calculate the total car sales per month and dealership
df_monthly_sales = df_sales_per_colour.groupby(['Dealership', 'When_Sold_Date'])[['Red_Cars', 'Silver_Cars', 'Black_Cars', 'Blue_Cars']].sum().reset_index()
df_monthly_sales['Total_Sales'] = df_monthly_sales.sum(axis=1)

# Reorder the columns
df_merged = df_monthly_sales[['Dealership', 'When_Sold_Date', 'Total_Sales', 'Red_Cars', 'Silver_Cars', 'Black_Cars', 'Blue_Cars']]

# Export the data to a CSV file
df_merged.to_csv('solution_week1.csv', index=False)

print(df_merged)
