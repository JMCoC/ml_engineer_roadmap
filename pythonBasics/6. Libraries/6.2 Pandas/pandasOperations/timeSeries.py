import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Time Series definition
"""
Time Series is a series of data points indexed in time order.
Analyzing time series data is an important part of data analysis because 
it is used in forecasting, monitoring, and analysis of economic data and
allows us to understand the past behavior of the data and predict the future.
Talking about time series, is has some concepts like:
1. Trend: The increasing or decreasing value in the series.
2. Seasonality: The repeating short-term cycle in the series.
3. Moving Average: The average of the data points in a specific window.
4. Noise: The random variation in the data.
5. Diferencing: The difference between the data points in a specific window.
6. Stationarity: The statistical properties of the data that do not change over time.
7. Order: The number of times the time series is differenced to make it stationary.
8. Autocorrelation: The correlation of the time series with a lagged version of itself.
9. Resampling: The process of converting the time series to a different frequency to reveal the data pattern.
"""

#Types of Time Series
"""
1. Continuous Time Series: The data points are recorded at regular intervals.
It is commonly encountered in: Temperature, Humidity, Stock Prices, sensor data, etc.

2. Discrete Time Series: The data points are recorded at irregular intervals.
It is commonly encountered in: Count data, categorical data, binary data, etc.
"""

#Visualizing Time Series Data
"""
Plotting countinuous time series data is done using the line plot, area plot or smooth plots.
Plotting discrete time series data is done using the bar chart, histogram and stacked bar chart.
"""

df = pd.read_csv('pythonBasics/CSV/stock_data.csv',
                parse_dates=['Date'],
                index_col='Date')

df.drop('Unnamed: 0', axis=1, inplace=True)
df.info()

sns.set(style="whitegrid")  

plt.figure(figsize=(12, 6))  
sns.lineplot(data=df, x='Date', y='High', label='High Price', color='blue')

plt.xlabel('Date')
plt.ylabel('High')
plt.title('Share Highest Price Over Time')

plt.show()

#Resampling Time Series Data
"""
Resampling is the process of converting the time series data to a different frequency.
1. rule: The frequency to convert the data to. (D(Day), ME(Month), YE(Year), H(Hour), etc.)
"""


sampleDf = df.resample('ME').mean(numeric_only=True)

sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
sns.lineplot(data=sampleDf, x=sampleDf.index, y='High', label='High Price Month', color='blue')

plt.xlabel('Date')
plt.ylabel('High')
plt.title('Share Highest Price Over Time')

plt.show()

#Smoothing Time Series Data

#Differencing

# Differencing
df['high_diff'] = df['High'].diff()

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(df['High'], label='Original High', color='blue')
plt.plot(df['high_diff'], label='Differenced High', linestyle='--', color='green')
plt.legend()
plt.title('Original vs Differenced High')
plt.show()

#Moving Average

# Moving Average
window_size = 120
df['high_smoothed'] = df['High'].rolling(window=window_size).mean()

# Plotting
plt.figure(figsize=(12, 6))

plt.plot(df['High'], label='Original High', color='blue')
plt.plot(df['high_smoothed'], label=f'Moving Average (Window={window_size})', linestyle='--', color='orange')

plt.xlabel('Date')
plt.ylabel('High')
plt.title('Original vs Moving Average')
plt.legend()
plt.show()
