# 100 Prisoners Problem

## Description

Bienvenue sur l'annexe numérique de notre projet !

Ce répertoire vise à expliquer à [le problème des 100 prisonniers](https://en.wikipedia.org/wiki/100_prisoners_problem).
Dans ce but, nous avons écrit un PDF ainsi que plusieurs petits programmes permettant
de mettre en pratique ce que nous avançons.

## Table of contents
  * [Installation](#installation)
  * [Requirements and dependencies](#requirements-and-dependencies)
  * [How to run](#how-to-run)
  * [Credits](#credits)
  * [Contributing](#contributing)
  * [License](#license)

## Installation 
Procédez au clonage du répertoire sur votre machine personelle.
Si vous avez configurer le `ssh`, alors vous pouvez exécutez la commande suivante afin de cloner le projet.
```
git clone git@github.com:YanisLcn/100-prisoners.git
```

## Requirements and dependencies 
Vous aurez besoin de 
* python3 >= 3.10
* pip

Ainsi que des dépendances suivantes
* networkx
* numpy
* matplotlib

## How to run 

Afficher une permutation aléatoire de 100 éléments sous forme de cycles :
```
python3 gui/GraphRepresentation.py
```

Tester l'énigme des 100 prisonniers et comparer les pourcentages de réussite :
```
python3 tools/100-prisoners.py
```

Afficher les cycles d'une permutation
```
python3 tools/permutation_cycles.py
```

## Credits 

Contributors : 
 * Guetteville Nathan
 * Soan Tony Ly
 * Lacenne Yanis

## Contributing
See [CONTRIBUTING](/CONTRIBUTING.md)

## License
See [LICENSE](/LICENSE)
