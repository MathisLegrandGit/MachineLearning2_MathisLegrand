import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from mpl_toolkits.mplot3d import Axes3D

# Load data and labels
data = np.load("data.npy")
labels = np.load("labels.npy")

print(f"Loaded {data.shape[0]} samples with {data.shape[1]} features.")

# Dimensionality reduction with PCA and t-SNE

# PCA (linear)
pca_2d = PCA(n_components=2).fit_transform(data)
pca_3d = PCA(n_components=3).fit_transform(data)

# t-SNE (non-linear)
tsne_2d = TSNE(n_components=2, perplexity=30, random_state=0).fit_transform(data)
tsne_3d = TSNE(n_components=3, perplexity=30, random_state=0).fit_transform(data)

# Plotting functions

def plot_2d(X, labels, title, filename):
    plt.figure(figsize=(6, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='coolwarm', s=15)
    plt.title(title)
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

def plot_3d(X, labels, title, filename):
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels, cmap='coolwarm', s=15)
    ax.set_title(title)
    ax.set_xlabel("Comp 1")
    ax.set_ylabel("Comp 2")
    ax.set_zlabel("Comp 3")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

# Plot all

plot_2d(pca_2d, labels, "PCA (2D)", "pca_2d.png")
plot_3d(pca_3d, labels, "PCA (3D)", "pca_3d.png")

plot_2d(tsne_2d, labels, "t-SNE (2D)", "tsne_2d.png")
plot_3d(tsne_3d, labels, "t-SNE (3D)", "tsne_3d.png")