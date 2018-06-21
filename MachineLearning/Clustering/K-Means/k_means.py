import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split 
from sklearn.cluster import KMeans

# SETUP DATASET FROM .csv
dataset = pd.read_csv('Mall_Customers.csv')
x = dataset.iloc[:, [3,4]].values

# FIND THE OPTIMAL NUMBER OF CLUSTERS
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)    
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()
# RESULT = 5 CLUSTERS

# FIT K-MEANS TO DATASET
kmeans = KMeans(n_clusters = 5, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
ykmeans = kmeans.fit_predict(x)

# PLOT CLUSTERS

plt.scatter(x[ykmeans == 0, 0], x[ykmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(x[ykmeans == 1, 0], x[ykmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(x[ykmeans == 2, 0], x[ykmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(x[ykmeans == 3, 0], x[ykmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(x[ykmeans == 4, 0], x[ykmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of Clients')
plt.xlabel('Annual Income ($)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

