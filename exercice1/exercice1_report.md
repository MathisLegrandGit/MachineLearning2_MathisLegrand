*(Scroll down for the French version / Faites défiler pour la version française)*

# Machine Learning Mathis Legrand - Exercise 1 Report

# English Version

# Exercise 1 – Data Distribution and the Law of Large Numbers

## Summary

In this exercise, I explored a 2-dimensional random variable and used simulations to understand how the empirical average converges to the expected value as the number of samples increases. I had some trouble at first figuring out how to define a meaningful distribution and how to visualize the convergence, but after testing different sampling strategies and plotting styles, I managed to make it work.

## Goal

The goal was to create a 2D random variable \( Z = (X, Y) \) with real-valued components, compute its theoretical expected value, then sample from it and show that the empirical average gets closer and closer to the expected value as the number of samples increases. The point was to get a more intuitive understanding of the **law of large numbers** in practice.

## What I Tried

At the start, I tried using very simple uniform distributions for both X and Y, but I found the samples too evenly spread and the expected value not that interesting. Then I switched to a normal distribution for X and a Poisson-like skewed distribution for Y to have more contrast. This made the expected value asymmetric and easier to track visually.

I also struggled a bit to get the convergence plot to actually look like something meaningful — I wasn’t sure how to measure the distance to the expected value at each step. Eventually I used the **Euclidean distance** between the empirical average vector and the true expected value, which worked well and gave me a nice curve that decreases over time.

## Implementation Details

- I defined X as a Gaussian variable with mean 5 and std 2.
- I defined Y as a skewed exponential-like distribution shifted to have a finite mean.
- I sampled 10,000 values of Z = (X, Y), plotted them as a scatterplot.
- Then I computed the empirical average at various sample sizes (e.g. 100, 500, 1000, etc.).
- For each of those, I calculated the Euclidean distance to the expected value.
- Finally, I plotted this distance as a function of the number of samples.

## Visualizations

- `scatter_samples.png`: shows the 2D distribution of the samples (looks mostly round at first glance, but that’s due to the randomness of the first points).
- `convergence_plot.png`: shows how the empirical average vector gets closer to the theoretical mean. The curve goes down overall but has a few noisy bumps at the start.

## Observations

The convergence graph wasn’t perfectly smooth, but it clearly dropped and stabilized, showing that the empirical average does get close to the expected value. I noticed that the shape of the convergence depends a lot on how “noisy” the early samples are — sometimes it starts off close to the mean by chance, sometimes not.

## Conclusion

This was a simple but good exercise to better understand convergence through simulation. At first I thought plotting it would be trivial, but tuning the sampling and choosing the right way to represent convergence made it much clearer. I also realized that randomness can make the early results misleading, which is kind of the point of this whole exercise I think lol.

---

# French Version

# Exercice 1 – Distribution de données et loi des grands nombres

## Résumé

Dans cet exercice, j'ai exploré une variable aléatoire à deux dimensions et utilisé des simulations pour comprendre comment la moyenne empirique converge vers la valeur espérée à mesure que le nombre d'échantillons augmente. J'ai galéré un peu au début pour trouver une distribution intéressante et comprendre comment représenter visuellement la convergence, mais après plusieurs essais avec différents types d’échantillonnage et styles de tracés, j’ai fini par y arriver.

## Objectif

L'objectif était de créer une variable aléatoire \( Z = (X, Y) \) à deux dimensions avec des composantes réelles, de calculer sa valeur espérée, puis de générer des échantillons pour montrer que la moyenne empirique se rapproche progressivement de cette valeur. L’idée était de comprendre de manière plus intuitive la loi des grands nombres.

## Ce que j’ai essayé

Au début, j’ai utilisé une distribution uniforme pour X et Y, mais les points étaient trop bien répartis et la valeur moyenne n’était pas très intéressante. Ensuite, j’ai testé une distribution normale pour X et une distribution asymétrique (comme une exponentielle) pour Y, ce qui donnait une valeur moyenne décalée, donc plus facile à suivre visuellement.

J’ai aussi galéré à rendre le graphe de convergence lisible — je ne savais pas trop comment mesurer la distance à la moyenne théorique à chaque étape. Finalement, j’ai utilisé la **distance euclidienne** entre la moyenne empirique et la valeur espérée, et ça a bien marché. La courbe diminue globalement au fil du temps.

## Détails d’implémentation

- X suit une loi normale de moyenne 5 et d’écart-type 2.
- Y suit une loi exponentielle décalée avec une moyenne finie.
- J’ai généré 10 000 points de Z = (X, Y), et je les ai affichés dans un nuage de points.
- J’ai ensuite calculé la moyenne empirique pour différents nombres d’échantillons (100, 500, 1000, etc.).
- Pour chaque étape, j’ai calculé la distance euclidienne entre cette moyenne et la valeur espérée.
- Enfin, j’ai affiché cette distance en fonction du nombre d’échantillons.

## Visualisations

- `scatter_samples.png` : montre la répartition des échantillons en 2D (ça semble assez circulaire au début, mais c’est à cause du hasard sur les premiers points).
- `convergence_plot.png` : montre la convergence de la moyenne empirique vers la valeur théorique. La courbe descend globalement mais avec quelques bosses au début.

## Observations

Le graphe de convergence n’était pas parfaitement lisse, mais on voit clairement une tendance à la baisse qui se stabilise. J’ai remarqué que la forme de la courbe dépend beaucoup du "bruit" des premiers échantillons — parfois on commence proche de la moyenne par chance, parfois pas du tout.

## Conclusion

C’était un exercice simple mais efficace pour comprendre la convergence via des simulations. Je pensais que le graphe serait trivial à faire au début, mais il a fallu bien ajuster l’échantillonnage et le type de mesure. J’ai aussi compris que le hasard peut être trompeur au début, ce qui est justement le cœur du sujet ici.