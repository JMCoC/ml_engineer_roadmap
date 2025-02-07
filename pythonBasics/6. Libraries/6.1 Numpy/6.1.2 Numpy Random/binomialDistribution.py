#The binomal distribution is a probability distribution that describes the
# number of successes in a fixed number of Bernoulli trials, where the
# probability of success remains constant throughout the trials.

# We use the numpy.random.binomial() method to get a Binomial Data Distribution.

# It has three parameters:

# n - number of trials. (int or array_like of ints) (n >= 0)
# p - probability of success. (float or array_like of floats) (0 <= p <= 1)
# size - The shape of the returned array. (int or tuple of ints, optional)

# Returns: ndarray or scalar

from numpy import random

# result of flipping a coin 10 times, tested 10 times.
x = random.binomial(n=10, p=0.5, size=10)
print(x)

# Visualization of Binomial Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(random.binomial(n=10, p=0.5, size=1000), kde=True)

plt.show()

#Diferences between the binomial and normal distributions:
# The binomial distribution is a discrete probability distribution, with
# values that can only be integers, while the normal distribution is a
# continuous probability distribution, with values that can be any real
# number.

sns.kdeplot(random.binomial(n=100, p=0.5, size=1000), label='Binomial')
sns.kdeplot(random.normal(loc=50, scale=5, size=1000), label='Normal')

plt.show()