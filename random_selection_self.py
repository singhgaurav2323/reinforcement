# random selection ads basic

import random
import pandas as pd
import matplotlib.pyplot as plt
#reading the file
dataset=pd.read_csv('Ads_CTR_Optimisation.csv')

#random function loop
N=1000
d=10
ads_selected=[]
total_score=0
for i in range(0,N):
    ads=random.randrange(d)
    ads_selected.append(ads)
    score=dataset.values[i,ads]
    total_score=total_score+score

#plotting histogram
plt.hist(ads_selected)
plt.title('ads selection chart')
plt.xlabel('ad number')
plt.ylabel('number of people clicked')
plt.xlim(0,10)
plt.show()