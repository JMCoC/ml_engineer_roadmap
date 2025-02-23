import pandas as pd
import matplotlib.pyplot as plt

"""
.corr() is used to find the pairwise correlation of all columns in the dataframe.
Any NaN values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.
1. method : {'pearson', 'kendall', 'spearman'}
    1.1 pearson : standard correlation coefficient
    1.2 kendall : Kendall Tau correlation coefficient
    1.3 spearman : Spearman rank correlation
2. min_periods : int, optional
    Minimum number of observations required per pair of columns to have a valid result. Currently only available for pearson and spearman correlation
3. numeric_only : bool, optional
    If True, only include numeric columns when calculating correlation.
"""

# Pearson Correlation
"""
This is the default method of correlation. It is used to find the linear relationship between two variables.
The value of Pearson correlation coefficient can be between -1 to 1.
1. 1: perfect positive linear relationship
2. 0: no linear relationship
3. -1: perfect negative linear relationship

Formula:
r = Σ((x - x̄)(y - ȳ)) / √(Σ(x - x̄)² * Σ(y - ȳ)²)
where,
r = Pearson correlation coefficient
x = values of x-variable
y = values of y-variable
x̄ = mean of x
ȳ = mean of y

When should you use Pearson correlation?
1. When the relationship between variables is linear
2. When variables are approximately normally distributed
3. When there are no significant outliers
"""

df = pd.read_csv('pythonBasics/CSV/pearson.csv')
print(df.corr(method='pearson'))

plt.scatter(df['age'], df['income'])
plt.xlabel('age')
plt.ylabel('income')
plt.title('Scatter plot of age and income')
plt.show()

# Spearman Correlation
"""
This method is used to find the monotonic relationship between two variables.
It is used when the relationship between variables is non-linear.
What monotonic means is that the variables tend to change together, but not necessarily at a constant rate.
The value of Spearman correlation coefficient can be between -1 to 1.
1. 1: perfect positive monotonic relationship
2. 0: no monotonic relationship
3. -1: perfect negative monotonic relationship

Formula:
ρ = 1 - ((6 * Σ(d²)) / (n * (n² - 1)))
where,
ρ = Spearman correlation coefficient
d = difference between the ranks of paired observations
n = number of observations

When should you use Spearman correlation?
1. When the relationship between variables is not necessarily linear or non-linear
2. When variables are not normally distributed
3. When there are outliers
"""

df = pd.read_csv('pythonBasics/CSV/spearman.csv')
print(df.corr(method='spearman'))
print(df.corr(method='pearson'))

plt.scatter(df['x'], df['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter plot of x and y')
plt.show()

# Kendall Correlation
"""
This method is used to find the ordinal relationship between two variables.
It is used when the relationship between variables is non-linear.
The value of Kendall correlation coefficient can be between -1 to 1.
1. 1: perfect positive ordinal relationship
2. 0: no ordinal relationship
3. -1: perfect negative ordinal relationship

Formula:
τ = (P - Q) / 1/2(n(n - 1))
or 
τ = (P - Q) / √((P + Q + T)(P + Q + U)) when ties are present
where,
τ = Kendall correlation coefficient
P = number of concordant pairs
Q = number of discordant pairs
n = total number of pairs

T = number of ties in x-variable
U = number of ties in y-variable

When should you use Kendall correlation?
1. When the relationship between variables is not necessarily linear or non-linear
2. When variables are not normally distributed
3. When there are outliers and ties
"""

df = pd.read_csv('pythonBasics/CSV/kendall.csv')
print(df.corr(method='kendall'))
print(df.corr(method='pearson'))
print(df.corr(method='spearman'))

plt.scatter(df['how_good'], df['yes_or_no'])
plt.xlabel('how_good')
plt.ylabel('yes_or_no')
plt.title('Scatter plot of how_good and yes_or_no')
plt.show()