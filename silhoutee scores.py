from sklearn.metrics import silhouette_samples

# 1. Calculate the silhouette score for each data point
silhouette_scores = silhouette_samples(df_for_clustering.drop(columns=['Cluster_Label']), df_for_clustering['Cluster_Label'])

# 2. Add the silhouette scores as a new column, 'Silhouette_Score', to the df_for_clustering DataFrame
df_for_clustering['Silhouette_Score'] = silhouette_scores

# 3. Calculate the mean of the features for each cluster
cluster_analysis = df_for_clustering.groupby('Cluster_Label').mean()

# 5. Add a 'Cluster_Size' column to the cluster_analysis DataFrame
cluster_sizes = df_for_clustering['Cluster_Label'].value_counts().sort_index()
cluster_analysis['Cluster_Size'] = cluster_sizes

# 4. Store the results in a new DataFrame called cluster_analysis (already done in step 3 and 5)

# 6. Display the cluster_analysis DataFrame
display(cluster_analysis)
