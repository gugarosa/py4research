import py4research.math.clustering as c
import py4research.math.random as r

# Variables definitions
n_samples = 10
n_variables = 4
n_dimensions = 1
n_clusters = 4

# Creates the features to be clustered
features = r.generate_gaussian_random_number(size=(n_samples, n_variables, n_dimensions))

# Performs K-Means clustering
cluster_idx = c.kmeans(features, n_clusters=n_clusters)

print('Sample: cluster_index')
for i, idx in enumerate(cluster_idx):
    print(f'{i}: {idx}')
