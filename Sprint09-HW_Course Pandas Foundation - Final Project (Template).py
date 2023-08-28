# -*- coding: utf-8 -*-

# -- Project --

# # Final Project - Analyzing Sales Data
# 
# **Date**: 27 August 2023
# 
# **Author**: Kesinee Chukorn (Gade)
# 
# **Course**: `Pandas Foundation`


# import data
import pandas as pd
df = pd.read_csv("sample-store.csv")

# preview top 5 rows
df.head()

# shape of dataframe
df.shape

# see data frame information using .info()
df.info()

# We can use `pd.to_datetime()` function to convert columns 'Order Date' and 'Ship Date' to datetime.


# example of pd.to_datetime() function
pd.to_datetime(df['Order Date'].head(), format='%m/%d/%Y')

# TODO - convert order date and ship date to datetime in the original dataframe
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# TODO - count nan in postal code column
nan_count = df['Postal Code'].isnull().sum()

print("Nan:", nan_count)

# TODO - filter rows with missing values
df.dropna(axis=0, how='any', inplace=True)

# TODO - Explore this dataset on your owns, ask your own questions
# Display the first few rows
print(df.head())

# Get summary statistics
print(df.describe())

# Check data types and null values
print(df.info())

# ## Data Analysis Part
# 
# Answer 10 below questions to get credit from this course. Write `pandas` code to find answers.


# TODO 01 - how many columns, rows in this dataset
df.shape = num_rows, num_columns 

print("Number of rows:", num_rows)
print("Number of columns:", num_columns)

# TODO 02 - is there any missing values?, if there is, which colunm? how many nan values?

# Check for missing values in each column
missing_values = df.isnull().sum()

# Print columns with missing values and their respective counts
for column, count in missing_values.items():
    if count > 0:
        print(f"Column '{column}' has {count} missing values.")

# TODO 03 - your friend ask for `California` data, filter it and export csv for him

# Filter data for California
california_data = df[df['State'] == 'California']

# Export filtered data to a new CSV file
california_data.to_csv('california_data.csv', index=False)

print("Filtered data for California exported to 'california_data.csv'")

# TODO 04 - your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file
# Convert 'Order Date' column to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Filter data for California and Texas in 2017
filtered_data = df[(df['State'].isin(['California', 'Texas'])) & (df['Order Date'].dt.year == 2017)]

# Export filtered data to a new CSV file
filtered_data.to_csv('filtered_orders_2017_CA_TX.csv', index=False)

print("Filtered data exported to 'filtered_orders_2017_CA_TX.csv'")

# TODO 05 - how much total sales, average sales, and standard deviation of sales your company make in 2017
# Convert 'Order Date' column to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Filter data for the year 2017
data_2017 = df[df['Order Date'].dt.year == 2017]

# Calculate total sales
total_sales = data_2017['Sales'].sum()

# Calculate average sales
avg_sales = data_2017['Sales'].mean()

# Calculate standard deviation of sales
std_dev_sales = data_2017['Sales'].std()

print("Total Sales in 2017:", total_sales)
print("Average Sales in 2017:", avg_sales)
print("Standard Deviation of Sales in 2017:", std_dev_sales)

# TODO 06 - which Segment has the highest profit in 2018
# Filter data for the year 2018
data_2018 = df[df['Order Date'].dt.year == 2018]

# Group data by Segment and calculate total profit
segment_profit = data_2018.groupby('Segment')['Profit'].sum()

# Find the segment with the highest profit
highest_profit_segment = segment_profit.idxmax()
highest_profit_value = segment_profit.max()

print(highest_profit_segment ),
print(highest_profit_value )

# TODO 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019
# Filter data for the specified date range
start_date = pd.Timestamp('2019-04-15')
end_date = pd.Timestamp('2019-12-31')
data_range = df[(df['Order Date'] >= start_date) & (df['Order Date'] <= end_date)]

# Group data by State and calculate total sales
state_sales = data_range.groupby('State')['Sales'].sum()

# Find the top 5 states with the least total sales
top_least_sales_states = state_sales.nsmallest(5)

print("Top 5 States with the Least Total Sales:")
print(top_least_sales_states)

# TODO 08 - what is the proportion of total sales (%) in West + Central in 2019 e.g. 25% 
# Filter data for the year 2019
data_2019 = df[df['Order Date'].dt.year == 2019]

# Filter data for West and Central regions
west_central_data = data_2019[data_2019['Region'].isin(['West', 'Central'])]

# Calculate total sales for West + Central
total_sales_west_central = west_central_data['Sales'].sum()

# Calculate total sales for the entire dataset in 2019
total_sales_2019 = data_2019['Sales'].sum()

# Calculate the proportion of total sales for West + Central
proportion_west_central = (total_sales_west_central / total_sales_2019) * 100

print(f"The proportion of total sales in West + Central in 2019 is: {proportion_west_central:.2f}%")

# TODO 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020
# Filter data for the years 2019 and 2020
data_2019_2020 = df[(df['Order Date'].dt.year >= 2019) & (df['Order Date'].dt.year <= 2020)]

# Group data by Product Name and calculate number of orders and total sales
product_stats = data_2019_2020.groupby('Product Name').agg({'Order ID': 'count', 'Sales': 'sum'})

# Rename columns for clarity
product_stats.rename(columns={'Order ID': 'Number of Orders'}, inplace=True)

# Sort products by both number of orders and total sales
sorted_products = product_stats.sort_values(by=['Number of Orders', 'Sales'], ascending=False)

# Get top 10 popular products
top_10_popular_products = sorted_products.head(10)

print("Top 10 Popular Products in 2019-2020:")
print(top_10_popular_products)

# TODO 10 - plot at least 2 plots, any plot you think interesting :)
top_10_popular_products['Number of Orders'].plot(kind='bar', color='blue')

top_10_popular_products[['Number of Orders', 'Total Sales']]\ 
    .plot(x='Number of Orders', y='Total Sales', kind="scatter", color="orange")

# TODO Bonus - use np.where() to create new column in dataframe to help you answer your own questions
# Create a new column 'year' to extract the year from 'Order Date'
df['year'] = df['Order Date'].dt.year

# Calculate total sales, average sales, and standard deviation of sales for 2017
data_2017 = df[df['year'] == 2017]
total_sales_2017 = data_2017['Sales'].sum()
average_sales_2017 = data_2017['Sales'].mean()
std_dev_sales_2017 = data_2017['Sales'].std()

print("Total Sales in 2017:", total_sales_2017)
print("Average Sales in 2017:", average_sales_2017)
print("Standard Deviation of Sales in 2017:", std_dev_sales_2017)

