import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from scipy.spatial.distance import cdist

# Load 4D customer data
data = np.load("data.npy")
print(f"Loaded data: {data.shape[0]} samples, {data.shape[1]} features")

# Elbow method to help pick k
def plot_elbow_method(data, max_k=10, title="Elbow Method", filename="elbow.png"):
    distortions = []
    for k in range(2, max_k+1):
        kmeans = KMeans(n_clusters=k, random_state=0)
        kmeans.fit(data)
        dist = np.mean(np.min(cdist(data, kmeans.cluster_centers_, 'euclidean'), axis=1))
        distortions.append(dist)
    
    plt.figure()
    plt.plot(range(2, max_k+1), distortions, marker='o')
    # I check the elbow manually here
    plt.title(title)
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Distortion")
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

# Silhouette score to check cluster tightness
def silhouette_for_range(data, clustering_cls, name, filename):
    scores = []
    for k in range(2, 10):
        model = clustering_cls(n_clusters=k)
        labels = model.fit_predict(data)
        score = silhouette_score(data, labels)
        scores.append(score)
    plt.figure()
    plt.plot(range(2, 10), scores, marker='x')
    plt.title(f"Silhouette Score - {name}")
    plt.xlabel("k")
    plt.ylabel("Score")
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

# Run clustering and plot with PCA projection
def run_and_plot_clustering(data, model, name, filename):
    model.fit(data)
    if hasattr(model, 'labels_'):
        labels = model.labels_
    else:
        raise ValueError("No labels found after fit")
    
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(data)
    
    plt.figure()
    plt.scatter(reduced[:, 0], reduced[:, 1], c=labels, cmap='tab10', s=15)
    plt.title(name)
    plt.xlabel("PCA Comp 1")
    plt.ylabel("PCA Comp 2")
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

# Run everything

# KMeans raw data
plot_elbow_method(data, title="Elbow - KMeans (Euclidean)", filename="kmeans_elbow.png")
silhouette_for_range(data, KMeans, "KMeans (Euclidean)", filename="kmeans_silhouette.png")

# Pick 3 clusters based on elbow and silhouette
kmeans_final = KMeans(n_clusters=3, random_state=0)
run_and_plot_clustering(data, kmeans_final, "KMeans (Euclidean)", filename="kmeans_result.png")

# Agglomerative with scaled data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

plot_elbow_method(data_scaled, title="Elbow - Agglomerative (Scaled)", filename="agglo_elbow.png")
silhouette_for_range(data_scaled, AgglomerativeClustering, "Agglomerative (Scaled)", filename="agglo_silhouette.png")

# Also 3 clusters here for consistency
agglo_final = AgglomerativeClustering(n_clusters=3)
run_and_plot_clustering(data_scaled, agglo_final, "Agglomerative (Scaled)", filename="agglo_result.png")