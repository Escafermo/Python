# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implement Thompson Sampling
N = 10000 # Total number of rounds
d = 10 # Total number of ads (arms)
numbers_of_rewards_1 = [0] * d # Vector of size d containing only 0s
numbers_of_rewards_0 = [0] * d # Vector of size d containing only 0s
ads_selected = []
total_reward = 0

for n in range (0, N):
    max_random = 0
    ad = 0
    for i in range (0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i]+1, numbers_of_rewards_0[i]+1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    real_reward = dataset.values[n, ad] # Using the dataset we get the reward that would happen during a campaign
    if real_reward == 1:
        numbers_of_rewards_1[ad] += 1
    else:
        numbers_of_rewards_0[ad] += 1
    
    total_reward += real_reward
    
    
# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()



