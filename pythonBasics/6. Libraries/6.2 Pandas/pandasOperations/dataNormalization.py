import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Data normalization is the process of standardizing the values of independent features of data in a dataset.
Since the range of values of raw data varies widely, in some machine learning algorithms, objective functions will not work properly without normalization.
We have different methods, as escaling, standardization, normalization, etc.
"""

#Real scale

df = pd.read_csv('pythonBasics/CSV/people_data.csv')

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)
ax1.set_title('Original Data together')
ax1.plot(df)
ax2.set_title('Salary')
ax2.plot(df['salary'], linewidth = 0, marker = 'o', color = 'blue', markersize = 6)
ax3.set_title('Cars')
ax3.plot(df['cars'], linewidth = 0, marker = '+', color = 'orange', markersize = 16)
plt.show()

fig2 = plt.figure(figsize=(8, 8))
ax4 = fig2.add_subplot(2, 2, 1)
ax5 = fig2.add_subplot(2, 2, 2)
ax4.set_title('Salary')
ax4.hist(df['salary'], bins = 100, color = 'blue')
ax5.set_title('Cars')
ax5.hist(df['cars'], color = 'orange')
plt.show()

#Scaling (min-max scaling)

"""
The min-max scaling method scales the data to a fixed range, usually 0 to 1.
The formula to scale the data is:
X_scaled = (X - X.min) / (X.max - X.min)
"""

df_min_max = df.copy(deep=True)
for column in df_min_max.columns:
    df_min_max[column] = (df_min_max[column] - df_min_max[column].min()) / (df_min_max[column].max() - df_min_max[column].min())

#Normalizing

"""
Normalization is the process of scaling individual samples to have unit norm.
This process can be useful if you plan to use a quadratic form such as the dot-product or any other kernel to quantify the similarity of any pair of samples.
The formula to normalize the data is:
X_normalized = X / sqrt(X_1^2 + X_2^2 + ... + X_n^2)
"""

df_normalized = df.copy(deep=True)
for column in df_normalized.columns:
    df_normalized[column] = df_normalized[column] / np.sqrt(np.sum(df_normalized[column] ** 2))

#Standardization

"""
Standardization is the process of transforming data into a standard scale.
The formula to standardize the data is:
X_standardized = (X - X.mean) / X.std
"""

df_standardized = df.copy(deep=True)
for column in df_standardized.columns:
    df_standardized[column] = (df_standardized[column] - df_standardized[column].mean()) / df_standardized[column].std()

#Standardization interquartile

"""
Standardization interquartile is the process of transforming data into a standard scale using the interquartile range.
The formula to standardize the data is:
X_standardized = (X - X.median) / IQR
IQR = Q3 - Q1
Q1 = 25th percentile
Q3 = 75th percentile
"""

df_standardized_iqr = df.copy(deep=True)
for column in df_standardized_iqr.columns:
    df_standardized_iqr[column] = (df_standardized_iqr[column] - df_standardized_iqr[column].median()) / (df_standardized_iqr[column].quantile(0.75) - df_standardized_iqr[column].quantile(0.25))

fig3 = plt.figure(figsize=(15, 3))
ax6 = fig3.add_subplot(1, 5, 1)
ax7 = fig3.add_subplot(1, 5, 2)
ax8 = fig3.add_subplot(1, 5, 3)
#ax8.set_ylim(0, 1) 
ax9 = fig3.add_subplot(1, 5, 4)
ax10 = fig3.add_subplot(1, 5, 5)
ax6.set_title('Salary')
ax6.plot(df['salary'], linewidth = 0, marker = 'o', color = 'blue', markersize = 6)
ax7.set_title('Min Max Salary')
ax7.plot(df_min_max['salary'], linewidth = 0, marker = 'o', color = 'blue', markersize = 6)
ax8.set_title('Normalized Salary')
ax8.plot(df_normalized['salary'], linewidth = 0, marker = 'o', color = 'blue', markersize = 6)
ax9.set_title('Standardized Salary')
ax9.plot(df_standardized['salary'], linewidth = 0, marker = 'o', color = 'blue', markersize = 6)
ax10.set_title('Standardized IQR Salary')
ax10.plot(df_standardized_iqr['salary'], linewidth = 0, marker = 'o', color = 'blue', markersize = 6)
plt.show()

fig4 = plt.figure(figsize=(15, 3))
ax11 = fig4.add_subplot(1, 5, 1)
ax12 = fig4.add_subplot(1, 5, 2)
ax13 = fig4.add_subplot(1, 5, 3)
#ax13.set_ylim(0, 1)
ax14 = fig4.add_subplot(1, 5, 4)
ax15 = fig4.add_subplot(1, 5, 5)
ax11.set_title('Cars')
ax11.plot(df['cars'], linewidth = 0, marker = '+', color = 'orange', markersize = 16)
ax12.set_title('Min Max Cars')
ax12.plot(df_min_max['cars'], linewidth = 0, marker = '+', color = 'orange', markersize = 16)
ax13.set_title('Normalized Cars')
ax13.plot(df_normalized['cars'], linewidth = 0, marker = '+', color = 'orange', markersize = 16)
ax14.set_title('Standardized Cars')
ax14.plot(df_standardized['cars'], linewidth = 0, marker = '+', color = 'orange', markersize = 16)
ax15.set_title('Standardized IQR Cars')
ax15.plot(df_standardized_iqr['cars'], linewidth = 0, marker = '+', color = 'orange', markersize = 16)
plt.show()

"""
This way we can see the difference between the original data and the data normalized, scaled, standardized and standardized using the interquartile range.
And now we can compare the data in the same scale.
When we have a dataset with different scales, it is important to normalize the data to avoid bias in the model.
When to use each method?
- Scaling: when you have a dataset with a range of values and you want to scale them to a fixed range. (0 to 1, -1 to 1, etc.)
- Normalization: When the data represents vectors and you want to normalize them to have unit norm.
- Standardization: When the data has a normal distribution and you want to standardize them to have a mean of 0 and a standard deviation of 1.
- Standardization interquartile: When the data has outliers and you want to standardize them using the interquartile range.
"""