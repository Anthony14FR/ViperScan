# MrA ViperScan

Ce programme permet de rechercher des fichiers dans un répertoire spécifié en utilisant un mot-clé de recherche.

## Fonctionnalités

- Recherche de fichiers par mot-clé dans un répertoire spécifié.
- Affichage des résultats de recherche avec mise en évidence du chemin des fichiers trouvés.
- Affichage du temps d'exécution de la recherche.

## Prérequis

- Python 3.x
- Les modules suivants doivent être installés :
  - os
  - glob
  - time
  - colorama
  - ctypes

## Installation

1. Clonez ce référentiel sur votre machine locale :

   ```shell
   git clone https://github.com/VotreUtilisateur/VotreRepositoire.git
   ```

2. Accédez au répertoire du projet :

   ```shell
   cd VotreRepositoire
   ```

3. Exécutez le programme :

   ```shell
   python viper_scan.py
   ```

## Utilisation

1. Entrez le mot-clé que vous souhaitez rechercher lorsque vous y êtes invité.
2. Entrez le répertoire dans lequel vous souhaitez effectuer la recherche lorsque vous y êtes invité.
3. Attendez que la recherche soit terminée.
4. Les résultats de recherche seront affichés avec les chemins des fichiers trouvés mis en évidence.
5. Le temps d'exécution de la recherche sera également affiché.

## Exemple

```shell
$ python viper_scan.py

Crédits du développeur :
Développé par : MrAnthony#6281
Pour Synaria

Entrez le mot-clé à rechercher : python
Entrez le répertoire de recherche : C:\Projet

Crédits du développeur :
Développé par : MrAnthony#6281
Pour Synaria

Mot recherché : python
Répertoire sélectionné : C:\Projet

Fichier trouvé : C:\Projet\script.py
Fichier trouvé : C:\Projet\module\utils.py

La recherche est terminée.

Temps d'exécution : 2.345 secondes.

Développé par : MrAnthony#6281
Pour Synaria

Appuyez sur Entrée pour quitter...
```

## Crédits

- Développé par : MrAnthony#6281
- Pour Synaria
