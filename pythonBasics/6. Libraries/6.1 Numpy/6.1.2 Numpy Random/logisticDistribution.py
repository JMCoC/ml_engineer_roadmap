#The logistic distribution is used in extreme value problems where 
# it can act as a mixture of Gumbel distributions, in epidemiology, and 
# in neural networks. It is related to the logit function in statistics.

#It has three parameters:

#loc - mean, where the peak is. Default 0.
#scale - standard deviation, the flatness of distribution. Default 1.
#size - The shape of the returned array.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

sns.kdeplot(random.logistic(size=1000))
plt.show()

#Difference Between Logistic and Normal Distribution
#Both distributions are near identical, but the logistic distribution has
# more area under the tails. ie. It representage more possibility of
# occurence of an events further away from mean.