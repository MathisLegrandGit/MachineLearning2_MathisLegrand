*(Scroll down for the French version / Faites défiler pour la version française)*

# Exercise 3 – Company Clustering Customers

## Summary

In this exercise, I explored customer data using unsupervised clustering techniques. The dataset was 4-dimensional and the goal was to find patterns in the customer base that could help group similar clients. I used two different clustering methods (KMeans and Agglomerative Clustering), and I applied two heuristics to determine how many clusters to use: the elbow method and silhouette score. At first, it was a bit confusing to make sense of the results, especially because there’s no label to check “correctness,” but the visualizations helped me compare which combinations gave more meaningful groupings.

## Goal

The objective was to cluster the customers based on their features and try to identify natural groupings. Since there are no labels in this dataset, I had to rely on visual plots and internal metrics (like silhouette score and distortion) to judge how well the clustering worked. I also had to try two different distance metrics and compare how each method performed.

## What I Tried

I started with **KMeans** using the raw data and the elbow method to figure out the number of clusters. That part went pretty smoothly, and the elbow was clearly visible around 3 or 4 clusters. Then I used the silhouette score, which confirmed that 3 was a solid choice.

Next, I worked on **Agglomerative Clustering**, but this time I scaled the data using StandardScaler. I picked this approach because distance-based methods like Agglomerative are really sensitive to feature scale. I used the same two heuristics as before to find the right number of clusters. The silhouette score gave the best results here too, and the visual plot actually looked more “organic” than KMeans.

One thing I got stuck on for a while was that Agglomerative Clustering doesn’t return labels the same way KMeans does, so I had to extract them manually. Once I figured that out, the rest of the script worked fine.

## Implementation Details

- I used **KMeans** on the raw data with Euclidean distance.
- I used **Agglomerative Clustering** on scaled data.
- For both, I ran:
  - The **elbow method** (using distortion/inertia)
  - The **silhouette score** (which turned out more useful)
- I plotted the resulting clusters using PCA for 2D projection just to make the clusters visual.

The plots generated were:

- `kmeans_elbow.png`
- `kmeans_silhouette.png`
- `kmeans_result.png`
- `agglo_elbow.png`
- `agglo_silhouette.png`
- `agglo_result.png`

## Observations

- KMeans gave reasonably tight clusters but looked very geometric.
- Agglomerative Clustering showed more natural shapes, probably because of the way it builds clusters bottom-up.
- The silhouette scores helped me decide when 3 clusters was a good cutoff.
- The visual differences between scaled and non-scaled data were pretty noticeable.

## Conclusion

Clustering helped reveal some potential structure in the customer data, even without labels. The silhouette score turned out to be the most helpful metric for this task. I found that Agglomerative Clustering with scaled data gave slightly better results than KMeans in this case, both in terms of visuals and internal evaluation scores.

---

# Version Française

# Exercice 3 – Regroupement des clients d’une entreprise

## Résumé

Dans cet exercice, j’ai exploré les données clients en utilisant des techniques de clustering non supervisé. Le jeu de données contenait 4 dimensions et l’objectif était de trouver des regroupements naturels parmi les clients. J’ai utilisé deux méthodes différentes (KMeans et clustering agglomératif), ainsi que deux heuristiques pour choisir le nombre de clusters : la méthode du coude et le score de silhouette. Au début, c’était un peu compliqué de comprendre les résultats, surtout sans étiquettes pour vérifier, mais les visualisations m’ont aidé à comparer quelles combinaisons donnaient des groupes plus cohérents.

## Objectif

L’objectif était de regrouper les clients selon leurs caractéristiques pour essayer d’identifier des groupes naturels. Comme il n’y avait pas d’étiquettes, j’ai dû m’appuyer sur des métriques internes (score de silhouette, distorsion) pour juger la qualité du clustering. J’ai aussi testé deux métriques de distance différentes pour comparer les méthodes.

## Ce que j’ai essayé

J’ai commencé par utiliser KMeans sur les données brutes, avec la méthode du coude pour estimer le nombre de clusters. Le coude était visible autour de 3 ou 4 clusters. Le score de silhouette a confirmé que 3 clusters était un bon choix.

Ensuite, j’ai testé le clustering agglomératif sur des données mises à l’échelle avec StandardScaler, parce que les méthodes basées sur la distance sont sensibles à l’échelle des données. J’ai utilisé les mêmes heuristiques pour choisir le nombre de clusters. Le score de silhouette donnait de bons résultats et les clusters semblaient plus “organiques” que ceux de KMeans.

J’ai eu un peu de mal à récupérer les labels pour le clustering agglomératif, qui ne renvoie pas les prédictions comme KMeans, mais une fois compris, tout a bien fonctionné.

## Détails d’implémentation

- J’ai utilisé KMeans sur les données brutes avec la distance euclidienne.
- J’ai utilisé le clustering agglomératif sur les données mises à l’échelle.
- Pour les deux méthodes, j’ai appliqué :
  - La méthode du coude (distorsion/inertie)
  - Le score de silhouette
- J’ai utilisé PCA pour projeter les clusters en 2D et faciliter la visualisation.

Les graphes générés étaient :

- `kmeans_elbow.png`
- `kmeans_silhouette.png`
- `kmeans_result.png`
- `agglo_elbow.png`
- `agglo_silhouette.png`
- `agglo_result.png`

## Observations

- KMeans produisait des clusters assez serrés mais très géométriques.
- Le clustering agglomératif donnait des formes plus naturelles, probablement grâce à son approche hiérarchique.
- Le score de silhouette m’a aidé à décider que 3 clusters était un bon nombre.
- La mise à l’échelle avait un impact visible sur la qualité des clusters.

## Conclusion

Le clustering a permis de révéler une structure possible dans les données clients, même sans étiquettes. Le score de silhouette était la métrique la plus utile. Le clustering agglomératif sur données mises à l’échelle a donné de meilleurs résultats que KMeans, aussi bien visuellement qu’au niveau des métriques internes.