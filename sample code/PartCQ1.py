import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the dataset
df = pd.read_csv("dataset_clustering.csv")

# Extract features
X = df.drop("label", axis=1)

# Experiment with different values of k
best_k = 2  # Initialize with a default value
max_silhouette_score = -1

for k in range(2, 11):  # Try k values from 2 to 10
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X)
    silhouette_avg = silhouette_score(X, labels)

    if silhouette_avg > max_silhouette_score:
        max_silhouette_score = silhouette_avg
        best_k = k
        best_model = kmeans

# Print the best number of clusters
print("Best Number of Clusters (k):", best_k)

# Store the best model in the variable named best_model
best_model = KMeans(n_clusters=best_k, random_state=42)
best_model.fit(X)
