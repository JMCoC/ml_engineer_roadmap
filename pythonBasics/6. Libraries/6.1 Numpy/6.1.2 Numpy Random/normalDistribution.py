#The Normal distribution is a probability distribution that is symmetric 
# about the mean, showing that data near the mean are more frequent 
# in occurrence than data far from the mean. In graph form, 
# normal distribution will appear as a bell curve.

# We use the numpy.random.normal() method to get a Normal Data Distribution.

# It has three parameters:

# loc - (Mean) where the peak of the bell exists. (float or array_like of floats)
# scale - (Standard Deviation) how flat the graph distribution should be. (float or array_like of floats)
# size - The shape of the returned array. (int or tuple of ints, optional)

#Returns: ndarray or scalar

from numpy import random

x = random.normal(size=(2, 3))
print(x)

x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

# Visualization of Normal Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(random.normal(size=1000), kde=True)

plt.show()