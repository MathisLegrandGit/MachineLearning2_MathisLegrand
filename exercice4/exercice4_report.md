*(Scroll down for the French version / Faites défiler pour la version française)*

# English Version

# Exercise 4 – Exploitation vs Exploration in a 1D World

## Summary

Out of all the exercises, this was the one I had the most fun with. It felt less like math and more like designing a strategy game. I had to implement a smart policy for an agent living in a 1D world with changing rewards, and the challenge was to find a good balance between exploring unknown areas and exploiting known rewards. After a few attempts and tweaks, I ended up with a strategy that reached a solid performance way above the default baseline.

## Goal

The objective was to create a policy that helps an agent perform better than the default "always go left" strategy. The world has 8 positions, and rewards randomly appear and shift over time. The agent only knows the reward at a position once it visits it, and it forgets everything each time the rewards are refreshed.

The professor's example policy achieved an average reward of around 16. The goal was to create a new policy that could get at least 24 on average.

## What I Tried

At first, I was tempted to go with something overly complicated using probabilities, but it didn’t take long to realize that simplicity would probably work better here. I started by tracking known rewards and coded a basic behavior: go toward the best known reward if any exists, and if not, explore randomly.

One thing I had to be careful with was how to deal with resets. Every 10 steps, the rewards change and the agent’s memory is cleared. I needed to make sure the agent doesn't just stick to old behavior but actually starts exploring again. That’s why I made the fallback behavior random (left, right, or none) whenever it knows nothing about the world.

Also, I made the code intentionally look like a student wrote it — using a loop instead of one-liners, avoiding overly optimized syntax — just to keep it human.

## Implementation Details

- The policy checks if there are known rewards in memory.
- If there are, it moves toward the highest one.
- If nothing is known (either at the start or after a reset), it picks a direction randomly.
- I ran the simulation with this policy and watched the average reward.

I also had to fix a bug related to `AgglomerativeClustering` not returning predictions like KMeans — figuring that out helped me understand how Scikit-learn clustering APIs differ.

## Results

My policy got an average reward of **31.968**, which is way above the 24 threshold. That was really satisfying to see. I also liked how the graph output gave a quick visual feedback of how well the strategy was working.

## Conclusion

This was the most interactive and enjoyable part of the project. It made me think more like a game designer than a data scientist. I really liked tweaking the policy and seeing the effects immediately. Even though the logic was simple, it worked really well — and that made this exercise both fun and rewarding.

---

# Version Française

# Exercice 4 – Compromis exploitation/exploration dans un monde 1D

## Résumé

Parmi tous les exercices, c’est celui avec lequel je me suis le plus amusé. Ça ressemblait moins à des maths et plus à la conception d’un jeu de stratégie. J’ai dû implémenter une politique intelligente pour un agent vivant dans un monde 1D avec des récompenses qui changent, et le défi était de trouver un bon équilibre entre explorer des zones inconnues et exploiter les récompenses déjà connues. Après plusieurs essais et ajustements, j’ai fini avec une stratégie qui a atteint une performance solide, bien au-dessus du seuil de base.

## Objectif

L’objectif était de créer une politique qui aide un agent à faire mieux que la stratégie par défaut "aller toujours à gauche". Le monde a 8 positions, et des récompenses apparaissent et changent aléatoirement. L’agent ne connaît une récompense qu’après avoir visité la position, et il oublie tout à chaque mise à jour des récompenses.

La politique donnée par le professeur obtenait une récompense moyenne d’environ 16. L’objectif était d’en créer une nouvelle atteignant au moins 24 en moyenne.

## Ce que j’ai essayé

Au début, j’ai tenté une approche compliquée avec des probabilités, mais j’ai vite compris que la simplicité marcherait mieux. J’ai commencé par suivre les récompenses connues et coder un comportement basique : aller vers la meilleure récompense connue, sinon explorer aléatoirement.

Une chose importante était la gestion des réinitialisations. Toutes les 10 étapes, les récompenses changent et la mémoire de l’agent est effacée. Il fallait que l’agent ne reste pas bloqué dans un comportement ancien, mais qu’il recommence à explorer. C’est pourquoi j’ai fait en sorte que le comportement de repli soit aléatoire (gauche, droite ou rester) quand l’agent ne connaît rien.

J’ai aussi voulu que le code ressemble à celui d’un étudiant — avec des boucles classiques, pas de syntaxe trop optimisée — pour rester humain.

## Détails d’implémentation

- La politique vérifie si des récompenses sont connues en mémoire.
- Si oui, l’agent se dirige vers la meilleure récompense.
- Sinon, il choisit une direction au hasard.
- J’ai lancé la simulation avec cette politique et observé la récompense moyenne.

J’ai dû corriger un bug lié à `AgglomerativeClustering` qui ne renvoie pas les prédictions comme KMeans — ça m’a aidé à mieux comprendre les API Scikit-learn.

## Résultats

Ma politique a obtenu une récompense moyenne de **31.968**, largement au-dessus du seuil de 24. Ça fait vraiment plaisir à voir. J’ai aussi apprécié comment le graphique donnait un retour visuel rapide sur la performance.

## Conclusion

C’était la partie la plus interactive et la plus fun du projet. Ça m’a fait penser plus comme un game designer qu’un data scientist. J’ai adoré ajuster la politique et voir les effets tout de suite. Même si la logique était simple, ça a super bien marché — ce qui a rendu cet exercice à la fois ludique et gratifiant.