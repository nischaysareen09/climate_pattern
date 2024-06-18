import pandas as pd
import matplotlib.pyplot as plt

# Load the data
daily_data = pd.read_csv('C:/Users/nisch/Documents/task2/daily_data.csv')
monthly_data = pd.read_csv('C:/Users/nisch/Documents/task2/monthly_data.csv')
three_hour_data = pd.read_csv('C:/Users/nisch/Documents/task2/three_hour_data.csv')

# Convert DATE columns to datetime format
daily_data['DATE'] = pd.to_datetime(daily_data['DATE'])
monthly_data['DATE'] = pd.to_datetime(monthly_data['DATE'])
three_hour_data['DATE'] = pd.to_datetime(three_hour_data['DATE'])

# Handle missing values only for numeric columns
numeric_columns_daily = daily_data.select_dtypes(include=['number']).columns
numeric_columns_monthly = monthly_data.select_dtypes(include=['number']).columns
numeric_columns_three_hour = three_hour_data.select_dtypes(include=['number']).columns

daily_data[numeric_columns_daily] = daily_data[numeric_columns_daily].apply(pd.to_numeric, errors='coerce')
monthly_data[numeric_columns_monthly] = monthly_data[numeric_columns_monthly].apply(pd.to_numeric, errors='coerce')
three_hour_data[numeric_columns_three_hour] = three_hour_data[numeric_columns_three_hour].apply(pd.to_numeric, errors='coerce')

daily_data[numeric_columns_daily] = daily_data[numeric_columns_daily].fillna(daily_data[numeric_columns_daily].mean())
monthly_data[numeric_columns_monthly] = monthly_data[numeric_columns_monthly].fillna(monthly_data[numeric_columns_monthly].mean())
three_hour_data[numeric_columns_three_hour] = three_hour_data[numeric_columns_three_hour].fillna(three_hour_data[numeric_columns_three_hour].mean())

# Descriptive statistics
print(daily_data.describe())
print(monthly_data.describe())
print(three_hour_data.describe())

# Example: Plotting temperature trends
plt.figure(figsize=(12, 6))
plt.plot(daily_data['DATE'], daily_data['DailyAverageDryBulbTemperature'], label='Daily Avg Temp')
plt.plot(monthly_data['DATE'], monthly_data['MonthlyMeanTemperature'], label='Monthly Avg Temp', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Trends Over Time')
plt.legend()
plt.show()