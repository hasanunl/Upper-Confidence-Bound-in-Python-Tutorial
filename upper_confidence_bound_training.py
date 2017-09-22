
#Libraires
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.set_printoptions(threshold=np.inf)

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing UCB (Ni = numbers of selections , Ri = sums of rewards , ar = avarage reward, ucb = upper confidence bound)
import math
N = 10000
d = 10
ads_selected = []
Ni = [0] * d
Ri = [0] * d
total_reward = 0
for n in range(0,N):
    ad = 0
    max_ucb = 0
    for i in range(0, d):
        if(Ni[i] > 0):            
            ar = Ri[i] / Ni[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / Ni[i])
            ucb = ar + delta_i
        else :
            ucb = 1e400
        if(ucb > max_ucb): 
            max_ucb = ucb
            ad = i
    ads_selected.append(ad)
    Ni[ad] = Ni[ad] + 1
    reward = dataset.values[n,ad]
    Ri[ad] = Ri[ad] + reward
    total_reward = total_reward + reward
    
# Visualizing the results
plt.hist(ads_selected)
plt.title('Histogram of ads')
plt.xlabel('Ads')
plt.ylabel('Number of times the ads were selected')
plt.show()    
    
        
        
    
