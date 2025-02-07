#The uniform distribution is a probability distribution 
# where each value within a certain range is equally likely to occur.

#It has three parameters:
#low - the lowest value in the distribution (default 0)
#high - the highest value in the distribution (default 1)
#size - the shape of the returned array

import numpy as np
from numpy import random

x = random.uniform(size=(2, 3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.kdeplot(random.uniform(size=1000), color='r', label='uniform')
plt.show()