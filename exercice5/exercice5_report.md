*(Scroll down for the French version / Faites défiler pour la version française)*

# English Version

# Exercise 5 – Dimensionality Reduction on Music Genre Dataset

## Summary

I am currently working on a music app for my end of year project, so I decided to go with a music genre dataset, I applied dimensionality reduction techniques on the dataset to try and visualize how songs are grouped based on their audio features. I used both PCA and t-SNE in 2D and 3D to check if songs naturally form clusters, and if genres show up visually in the projected space. I found that some separation between genres is visible, especially with t-SNE, and that proper preprocessing was necessary to make the projections meaningful.

## Dataset Description

The dataset is called **Music Genre Classification**, and I downloaded it from [Kaggle](https://www.kaggle.com/datasets/purumalgi/music-genre-classification). It contains a list of songs with features like:

- danceability
- energy
- loudness
- speechiness
- acousticness
- instrumentalness
- valence
- tempo
- and a few others

There’s also a column called `Class` which holds the genre of each song as a number (0 to 9). These numbers represent actual music genres, and I used them only for coloring points in the scatter plots, not for training anything.

## Goal

The goal was to apply **dimensionality reduction** to the dataset in order to visualize song similarities in 2D and 3D. I wanted to see if genres naturally separate based on the audio features alone.

## Initial Exploration

I started by loading the CSV and checking basic stats with `df.describe()` and `.isnull().sum()`. That’s when I saw that some columns had missing data:

- `Popularity`: 428 missing
- `key`: 2014 missing
- `instrumentalness`: 4377 missing

I didn’t want to drop rows because it would’ve meant losing a big chunk of the data. So I decided to **fill missing values with the median** for each column. This was the simplest option and works pretty well for numerical features when you don’t want outliers (like the mean) to affect the result.

## Preprocessing

I dropped irrelevant columns like `Artist Name` and `Track Name`, since they weren’t useful for analysis. Then I scaled the data using **StandardScaler** because PCA and t-SNE are sensitive to feature scale — for example, `tempo` and `valence` are on totally different scales originally.

## Dimensionality Reduction

I applied:

- **PCA** (Principal Component Analysis) to reduce to 2D and 3D
- **t-SNE** (t-distributed Stochastic Neighbor Embedding) in 2D and 3D

I used the real genre labels (`Class`) just to color the points for visualization. The actual unsupervised methods didn’t use the labels at all.

## Visualizations

I generated four plots:

- `pca_2d.png`: PCA projection in 2D
- `pca_3d.png`: PCA projection in 3D
- `tsne_2d.png`: t-SNE projection in 2D
- `tsne_3d.png`: t-SNE projection in 3D

I also improved the labels on the axes to make them more understandable (instead of just "Component 1", I wrote what it actually represents). I added legends using real genre names so that the graphs are easier to read.

## Results & Interpretation

PCA gave us a general sense of spread and variance, but the genre separation wasn’t super clear. On the other hand, t-SNE showed **more defined clusters**, especially in 2D. In 3D, it was also better than PCA but took longer to compute.

The separation wasn’t perfect (which makes sense, since music genres overlap in style), but I did see that some genres were grouped closer together — for example, Pop and R&B had overlapping regions, while Classical or Jazz tended to form their own areas.

## Conclusion

By reducing the dimensionality of the music dataset, I was able to visualize how songs group based on audio features alone. t-SNE in particular helped me find some natural clustering that aligns loosely with genres. Preprocessing — especially filling in missing values and scaling — was key to getting useful results.

---

# Version Française

# Exercice 5 – Réduction de dimension sur un jeu de données de genres musicaux

## Résumé

Je travaille actuellement sur une application musicale pour mon projet de fin d'année, j’ai donc choisi un jeu de données de classification de genres musicaux. J’ai appliqué des techniques de réduction de dimension pour essayer de visualiser comment les chansons se regroupent en fonction de leurs caractéristiques audio. J’ai utilisé PCA et t-SNE en 2D et 3D pour vérifier si les chansons forment naturellement des clusters et si les genres apparaissent visuellement dans l’espace projeté. J’ai constaté qu’une certaine séparation entre les genres est visible, surtout avec t-SNE, et qu’un prétraitement correct était nécessaire pour rendre les projections significatives.

## Description du jeu de données

Le jeu s’appelle **Music Genre Classification**, et je l’ai téléchargé sur [Kaggle](https://www.kaggle.com/datasets/purumalgi/music-genre-classification). Il contient une liste de chansons avec des caractéristiques comme :

- danceability
- energy
- loudness
- speechiness
- acousticness
- instrumentalness
- valence
- tempo
- et quelques autres

Il y a aussi une colonne `Class` qui contient le genre de chaque chanson sous forme de nombre (de 0 à 9). Ces nombres représentent les genres musicaux réels, et je les ai utilisés uniquement pour colorer les points dans les graphiques, pas pour entraîner quoi que ce soit.

## Objectif

L’objectif était d’appliquer une **réduction de dimension** au jeu de données pour visualiser la similarité des chansons en 2D et 3D. Je voulais voir si les genres se séparent naturellement selon les caractéristiques audio seules.

## Exploration initiale

J’ai commencé par charger le CSV et vérifier les statistiques de base avec `df.describe()` et `.isnull().sum()`. C’est là que j’ai vu que certaines colonnes avaient des données manquantes :

- `Popularity` : 428 manquants
- `key` : 2014 manquants
- `instrumentalness` : 4377 manquants

Je ne voulais pas supprimer de lignes car cela aurait fait perdre une grande partie des données. J’ai donc décidé de **remplacer les valeurs manquantes par la médiane** de chaque colonne. C’était la solution la plus simple et qui fonctionne bien pour les données numériques quand on veut éviter que les valeurs extrêmes faussent le résultat.

## Prétraitement

J’ai supprimé les colonnes inutiles comme `Artist Name` et `Track Name` qui n’étaient pas utiles pour l’analyse. Puis j’ai mis à l’échelle les données avec **StandardScaler** parce que PCA et t-SNE sont sensibles à l’échelle des caractéristiques — par exemple, `tempo` et `valence` ont des échelles très différentes à l’origine.

## Réduction de dimension

J’ai appliqué :

- **PCA** (analyse en composantes principales) pour réduire en 2D et 3D
- **t-SNE** (t-distributed Stochastic Neighbor Embedding) en 2D et 3D

J’ai utilisé les vraies étiquettes de genre (`Class`) uniquement pour colorer les points lors de la visualisation. Les méthodes non supervisées ne les ont pas utilisées.

## Visualisations

J’ai généré quatre graphiques :

- `pca_2d.png` : projection PCA en 2D
- `pca_3d.png` : projection PCA en 3D
- `tsne_2d.png` : projection t-SNE en 2D
- `tsne_3d.png` : projection t-SNE en 3D

J’ai aussi amélioré les labels des axes pour les rendre plus compréhensibles (au lieu de "Composante 1", j’ai écrit ce que ça représente vraiment). J’ai ajouté des légendes avec les vrais noms de genres pour faciliter la lecture.

## Résultats et interprétation

PCA a donné une idée générale de la dispersion et de la variance, mais la séparation des genres n’était pas très claire. En revanche, t-SNE a montré des clusters **plus définis**, surtout en 2D. En 3D, c’était aussi mieux que PCA, mais plus long à calculer.

La séparation n’était pas parfaite (ce qui est normal, les genres musicaux se recoupent souvent), mais j’ai vu que certains genres étaient plus proches — par exemple, Pop et R&B se chevauchent, tandis que Classique ou Jazz forment leurs propres zones.

## Conclusion

En réduisant la dimension du jeu de données musical, j’ai pu visualiser comment les chansons se regroupent selon leurs caractéristiques audio. t-SNE en particulier m’a aidé à trouver des clusters naturels qui correspondent vaguement aux genres. Le prétraitement — surtout le remplissage des valeurs manquantes et la mise à l’échelle — était essentiel pour obtenir des résultats utiles.