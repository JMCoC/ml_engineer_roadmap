#Seaborn is a library for making statistical graphics in Python. 
# It is built on top of matplotlib and closely integrated with pandas data structures.

#Distplots stands for distribution plots, it takes as input an array 
# and plots a curve corresponding to the distribution of points in the array.

import matplotlib.pyplot as plt
import seaborn as sns

data = [0, 1, 2, 3, 4, 5] 

sns.histplot(data, kde=True) 
plt.title("Histograma con KDE")
plt.show()

sns.kdeplot(data)
plt.title("Gráfico KDE")
plt.show()