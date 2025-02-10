#Exponential distribution is used for describing time till next event e.g. failure/success etc.
# It has two parameters:
# scale - beta = 1/lambda. It is the mean time until the next event.
# size - The shape of the returned array.

from numpy import random

x = random.exponential(scale=2, size=(2, 3))
print(x)

#Real World example
#Assume a company has 1000 customer support agents and the average time 
# between two calls is 4 minutes.

n = 10000
timeBetweenTwoCalls = random.default_rng().exponential(scale=4, size=n)

#What is the probability that a customer will call in the next 4 to 5 minutes?

x = ((timeBetweenTwoCalls < 5).sum() / n)
y = ((timeBetweenTwoCalls < 4).sum() / n)
print(x-y)

#Relation with Poisson Distribution
#Poisson distribution deals with number of occurences of an event in a time period whereas
#exponential distribution deals with the time between these events.

"""
There's more distribution functions available in numpy.random package.
Like pareto, rayleigh, zipf and chi square etc.
You can read more about them here: https://numpy.org/doc/stable/reference/random/generator.html
"""