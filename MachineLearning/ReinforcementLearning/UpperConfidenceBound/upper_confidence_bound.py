# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implement UCB
N = 10000 # Total number of rounds
d = 10 # Total number of ads (arms)
numbers_of_selections = [0] * d # Vector of size d containing only 0s
sums_of_rewards = [0] * d # Vector of size d containing only 0s
ads_selected = []
total_reward = 0

for n in range (0, N):
    max_upper_bound = 0
    ad = 0
    for i in range (0, d):
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else: # during the first 10 rounds, we select each one of the 10 ads
            upper_bound = 1e400 # 10 to the power of 400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    real_reward = dataset.values[n, ad] # Using the dataset we get the reward that would happen during a campaign
    numbers_of_selections[ad] += 1
    sums_of_rewards[ad] += real_reward
    total_reward += real_reward

# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()



