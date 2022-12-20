# Projet RCR 2022 : Argumentation Framework



## Sommaire
1. [Introduction et informations](README.md#introduction-et-informations)
2. [Fonctionnalités](README.md#fonctionnalités)
3. [Compilation, exécution et arguments possibles](README.md#compilation-execution-et-arguments-possibles)

-------------------------------------------------------



## Introduction et informations
**Informations généraux**
- Le sujet du projet : [projet.pdf](https://github.com/eio-ta/argumentation_framework/blob/main/sujet_projet.pdf)
- Le lien du GitHub : [lien](https://github.com/eio-ta/argumentation_framework)

**Identifiants et membres du groupe**
1. TANG Elody, 21953199, Master VMI



## Fonctionnalités

On appelle "Argumentation Framework" (AF) un graphe <A,R> avec les arguments A et les attaques R. Le programme ci-présent donne les différentes extensions et sémantiques.

Cette version accepte les options qui doivent être précédées d'un tiret et doit être suivies par un argument.

**Fonctionnalités principales :**

1.
2.
3.
4.
5.

**Fonctionnalités secondaires :**

1.
2.
3.
4.
5.



## Compilation execution et arguments possibles


**EXECUTION**

Il existe une méthode pour exécuter le programme :

```python3 ./program.py [OPT1] [ARG1] [OPT2] [ARG2]```

lancera le programme avec les arguments utilisés.


**EXEMPLE**

- Pour afficher le graphe complet du fichier "test.txt" :

```python3 program.py -p SE-CO -f test.txt```

- Pour voir si l'argument "a" est acceptée crédulement pour le graphe stable du fichier "test.txt" :

```python3 program.py -p DC-CO -f test.txt -a a```


**INTRODUCTION AUX OPTIONS POSSIBLES**

- **a** :  Cible un argument précis [un argument obligatoire]
- **f** :  Cible un fichier précis décrivant un AR. [un argument obligatoire]
- **h** :  Affiche ce message d'aide. [sans argument]
- **p** :  Précise le code de l'action que veut l'utilisateur. [un argument obligatoire]

Les options "p" et "f" sont obligatoires.


**LISTE DES CODES POSSIBLES**

- **PR-AF** :   Affiche le graphe.
- **SE-GR** :   Donne la sémantique fondée.
- **SE-CO** :   Donne la sémantique complète.
- **SE-PR** :   Donne la sémantique préférée.
- **SE-ST** :   Donne la sémantique stable.
- **SE-ALL** :  Donne toutes les sémantiques.
- **DC-CO** :   (Sans argument) Donne tous les arguments crédulement acceptés
                (Avec un argument) Vérifie si l'argument est crédulement accepté. [Pour la sémantique complète].
- **DS-CO** :   (Sans argument) Donne tous les arguments sceptiquement accepté.
                (Avec un argument) Vérifie si l'argument est sceptiquement accepté. [Pour la sémantique complète].
- **DC-ST** :   (Sans argument) Donne tous les arguments crédulement acceptés.
                (Avec un argument) Vérifie si l'argument est crédulement accepté. [Pour la sémantique stable].
- **DS-ST** :   (Sans argument) Donne tous les arguments sceptiquement acceptés.
                (Avec un argument) Vérifie si l'argument est sceptiquement accepté. [Pour la sémantique stable].