# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori # FILE IN FOLDER

# Data Preprocessing (list of 7500 products bought in a weeek)
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

# Making a list of all the products (columns) in each transaction (lines)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training Apriori on the dataset
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, max_length = 3)
# min_support = products that are bought ate least 3 times a day = 3 * 7 (days) = 21 times in dataset / 7500 = 0.0028
# min_confidence = % of cases the rule is correct = 20%
# min_lift = overral relevancy of rules = 3

# Visualising the results
results = list(rules)

# These 3 lines turn the rules into strings and add them to a list
results_list = []
for i in range(0, len(results)):
    results_list.append('RULE:\t' + str(results[i][0]) + '\nSUPPORT:\t' + str(results[i][1]))
    