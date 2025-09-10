from sklearn.cluster import KMeans

# Determine an appropriate number of clusters (chosen as 3)
n_clusters = 3
total_samples = len(df_for_clustering)
small_cluster_threshold = total_samples / n_clusters # A simple heuristic for a small dataset

# Instantiate a KMeans object
kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)

# Fit the KMeans model to the df_for_clustering DataFrame
kmeans.fit(df_for_clustering)

# Get the cluster labels
labels = kmeans.labels_

# Add the cluster labels to the df_for_clustering DataFrame
df_for_clustering['Cluster_Label'] = labels

# Print the number of samples in each cluster
print("Number of samples in each cluster:")
display(df_for_clustering['Cluster_Label'].value_counts().sort_index())
