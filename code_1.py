import numpy as np
import matplotlib.pyplot as plt
import statistics
import pandas as pd
import scipy.stats as stats

#Dataset
age=[2,3,4,6,7,8,9,1,12,13,14,15,16,17,5,10,30,20,39,40,19,18,27]

#to find the mean
mean= statistics.mean(age)
print("The mean is:", mean)

#to find the median
median=statistics.median(age)
print("The median is:", median)

#to find the mode
mode=statistics.mode(age)
print("The mode is:", mode)

#to find the Zscore
zscore=stats.zscore(age)
print("The Z-score are:", zscore)

#to find the standard daviation
data=np.array(age)
sd=np.std(data)
print(sd)
#to show the histogram
plt.hist(age, bins='auto')
plt.show()
