#The Poisson distribution is the probability distribution of independent event occurrences in an interval.
#For example, a Poisson distribution can describe the number 
# of emails received in an hour, the number of phone calls received in a day,
# or the number of customers arriving in a store in an hour.

#It has two parameters:
#lam - Expected number of occurrences in a given interval
#size - The shape of the returned array

from numpy import random

x = random.poisson(lam=2, size=10)
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

#The Diferece between Poisson and Normal Distribution is that the 
# Poisson distribution is the probability distribution of independent event 
# occurrences in an interval, while the normal distribution is the 
# probability distribution of a continuous variable and is symmetric 
# around the mean.

#But we can see that as the lam value increases the poisson distribution
# starts to look like a normal distribution

sns.kdeplot(random.poisson(lam=50, size=1000), color='g', label='lam=5')
sns.kdeplot(random.normal(loc=50, scale=7, size=1000), color='b', label='normal')
plt.show()

#The difference between Poisson and Binomial Distribution is that
# The Poisson distribution is the limit of the binomial distribution for large N.
# If the number of trials is indefinitely large or the probability of success is infinitesimally
# small, the binomial distribution converges to the Poisson distribution such that
# the product of mean and variance is equal to the parameter of the Poisson distribution.

sns.kdeplot(random.binomial(n=1000, p=0.01, size=1000), color='r', label='binomial')
sns.kdeplot(random.poisson(lam=10, size=1000), color='g', label='poisson')
plt.show()