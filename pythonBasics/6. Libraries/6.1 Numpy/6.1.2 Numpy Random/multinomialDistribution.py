#Multinomial distribution is a generalization of binomial distribution. 
# It describes outcomes of multi-nomial scenarios unlike binomial where 
# scenarios must be only one of two. e.g. Blood type of a population, 
# dice roll outcome.

# It has three parameters:

# n - number of possible outcomes (e.g. 6 for dice roll).
# pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
# size - The shape of the returned array.

from numpy import random

x = random.multinomial(20, [1/6]*6, size=1) # 20 dice rolls, with 6 possible outcomes
print(x)

x = random.multinomial(100, [1/6]*6, size=10) # 100 dice rolls, with 6 possible outcomes, tested 10 times
print(x)

#loaded dice example

x = random.multinomial(100, [0.1, 0.1, 0.1, 0.1, 0.1, 0.5], size=1)
print(x)

# Visualization of Multinomial Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(random.multinomial(100, [1/6]*6, size=1000), kde=True)

plt.show()