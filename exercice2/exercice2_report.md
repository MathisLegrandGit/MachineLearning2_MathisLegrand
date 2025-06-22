*(Scroll down for the French version / Faites défiler pour la version française)*

# English Version

# Exercise 2 – Meteorological Data: Dimensionality Reduction and Visualization

## Summary

In this exercise, I worked with a dataset containing meteorological sensor readings and tried to visualize it in lower dimensions to see if there was any structure that could help predict whether a tempest would occur. I used PCA and t-SNE to reduce the 6-dimensional data to 2D and 3D, then visualized the results with color-coded labels. It took some trial and error to get the plots to show something meaningful, especially with t-SNE, which is slower but ended up giving the clearest visual separation.

## Goal

The goal was to reduce the dimensionality of 800 meteorological samples (each with 6 features) to 2 and 3 dimensions, and then check whether the two classes (tempest or not) separate visually in the reduced space. If one method makes the classes clearly separable, then it might be possible to apply a supervised model to the reduced data.

## What I Tried

At first I tried PCA because it's quick and easy to understand. The PCA 2D plot didn’t separate the two classes well, so I tried 3D next, which gave a bit more structure but still had lots of overlap. I figured this might be because PCA is a linear method, and the actual separation between tempest and non-tempest data might be more complex.

Then I tried t-SNE, which took much longer to compute (especially in 3D), but gave much more interesting results. In 2D, I could already see some distinct clusters forming. In 3D, the structure was even clearer — not perfect separation, but definitely better than PCA.

## Implementation Details

- I loaded the data and labels from `.npy` files.
- I applied PCA to reduce to 2D and 3D.
- I also applied t-SNE to reduce to 2D and 3D.
- I plotted each projection using scatter plots, coloring the points by their label (1 for tempest, 0 for no tempest).
- The resulting PNGs were saved as:
  - `pca_2d.png`
  - `pca_3d.png`
  - `tsne_2d.png`
  - `tsne_3d.png`

## Observations

- PCA plots (especially in 2D) showed a large amount of class overlap.
- PCA in 3D was slightly better but still not very clear.
- t-SNE plots were much more effective at visually separating the tempest and non-tempest classes.
- The 3D t-SNE looked kind of “snaky” and irregular, but still revealed structure that wasn’t obvious before.

## Conclusion

Dimensionality reduction helped make some of the structure in the data visible. PCA was fast but not expressive enough for this task. t-SNE gave better visual separation between classes and could help in building a model that only uses 2 or 3 features. Running t-SNE was slower and more sensitive to parameters while still not being that noticeable thanks to my decent laptop performance, but the results were worth it in the end.

---

# Version Française

# Exercice 2 – Données Météorologiques : Réduction de Dimension et Visualisation

## Résumé

Dans cet exercice, j'ai travaillé avec un jeu de données contenant des relevés de capteurs météorologiques et j'ai essayé de le visualiser dans des dimensions réduites pour voir s'il existait une structure pouvant aider à prédire l'apparition d'une tempête. J'ai utilisé PCA et t-SNE pour réduire les données de 6 dimensions à 2 et 3 dimensions, puis j'ai visualisé les résultats avec des étiquettes colorées. Il m'a fallu plusieurs essais pour obtenir des graphes significatifs, surtout avec t-SNE, qui est plus lent, mais qui a fini par donner la meilleure séparation visuelle.

## Objectif

L’objectif était de réduire la dimension de 800 échantillons météorologiques (chacun ayant 6 caractéristiques) à 2 et 3 dimensions, puis de voir si les deux classes (tempête ou pas) se séparaient visuellement. Si une méthode rend les classes bien séparées, il serait alors possible d’entraîner un modèle supervisé sur les données projetées.

## Ce que j’ai essayé

J'ai commencé par utiliser PCA car c’est rapide et facile à comprendre. Le graphe en 2D n’a pas montré de bonne séparation entre les classes, donc j’ai tenté la 3D, qui donnait un peu plus de structure mais avec beaucoup de chevauchement. J’ai supposé que c’était parce que PCA est une méthode linéaire, et que la vraie séparation entre les données était plus complexe.

Ensuite, j’ai utilisé t-SNE, qui a mis beaucoup plus de temps à s’exécuter (surtout en 3D), mais qui a donné des résultats bien plus intéressants. En 2D, on pouvait déjà voir des groupes distincts se former. En 3D, la structure était encore plus claire — pas une séparation parfaite, mais clairement meilleure que PCA.

## Détails d’implémentation

- J’ai chargé les données et les labels depuis les fichiers `.npy`.
- J’ai appliqué PCA pour obtenir des projections en 2D et 3D.
- J’ai aussi utilisé t-SNE pour des projections en 2D et 3D.
- J’ai généré des graphes de dispersion en colorant les points selon leur label (1 pour tempête, 0 sinon).
- Les images générées étaient :
  - `pca_2d.png`
  - `pca_3d.png`
  - `tsne_2d.png`
  - `tsne_3d.png`

## Observations

- Les graphes PCA (surtout en 2D) montraient un gros chevauchement entre les classes.
- La 3D donnait un peu plus de séparation mais pas de manière très nette.
- Les graphes t-SNE ont montré une bien meilleure séparation visuelle entre les deux classes.
- Le t-SNE 3D avait une forme un peu irrégulière, mais révélait une structure qu’on ne voyait pas avant.

## Conclusion

La réduction de dimension a permis de rendre visibles certaines structures dans les données. PCA était rapide mais pas assez expressif pour ce cas. t-SNE a permis une meilleure séparation visuelle des classes et pourrait aider à entraîner un modèle supervisé avec seulement 2 ou 3 caractéristiques. Même si t-SNE est plus lent et sensible aux paramètres, le résultat en valait la peine — surtout avec un ordinateur qui tient bien la charge.