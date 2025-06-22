import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches

# Load dataset
df = pd.read_csv("music-dataset/train.csv")

# Map genre numbers to names
genre_map = {
    0: "Pop",
    1: "Hip-Hop",
    2: "Jazz",
    3: "Rock",
    4: "Electronic",
    5: "Folk",
    6: "Classical",
    7: "R&B",
    8: "Reggae",
    9: "Blues"
}

# Remove columns we don't need
df_numeric = df.drop(columns=["Artist Name", "Track Name"])

# Fill missing data with median
df_filled = df_numeric.fillna(df_numeric.median())

# Separate features and target
X = df_filled.drop(columns=["Class"])
y = df_filled["Class"]

# Scale features to normalize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA in 2D and 3D
pca_2d = PCA(n_components=2).fit_transform(X_scaled)
pca_3d = PCA(n_components=3).fit_transform(X_scaled)

# t-SNE in 2D and 3D
tsne_2d = TSNE(n_components=2, random_state=42).fit_transform(X_scaled)
tsne_3d = TSNE(n_components=3, random_state=42).fit_transform(X_scaled)

# Plotting helper functions
def plot_2d(X, labels, title, filename):
    plt.figure(figsize=(8, 7))
    scatter = plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='tab10', s=30, alpha=0.8)
    plt.title(title)
    plt.xlabel("Main variance direction")
    plt.ylabel("Second variance direction")
    plt.grid(True)

    unique_labels = sorted(set(labels))
    handles = [mpatches.Patch(color=plt.cm.tab10(i/10), label=genre_map.get(label, f"Class {label}")) for i, label in enumerate(unique_labels)]
    plt.legend(handles=handles, title="Genre", bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

def plot_3d(X, labels, title, filename):
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels, cmap='tab10', s=30, alpha=0.8)
    ax.set_title(title)
    ax.set_xlabel("Main variance direction")
    ax.set_ylabel("Second variance direction")
    ax.set_zlabel("Third variance direction")

    unique_labels = sorted(set(labels))
    handles = [mpatches.Patch(color=plt.cm.tab10(i/10), label=genre_map.get(label, f"Class {label}")) for i, label in enumerate(unique_labels)]
    plt.legend(handles=handles, title="Genre", bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

# Plot all
plot_2d(pca_2d, y, "PCA (2D) - Genre Projection", "pca_2d.png")
plot_3d(pca_3d, y, "PCA (3D) - Genre Projection", "pca_3d.png")

plot_2d(tsne_2d, y, "t-SNE (2D) - Genre Projection", "tsne_2d.png")
plot_3d(tsne_3d, y, "t-SNE (3D) - Genre Projection", "tsne_3d.png")