import os
import glob
import time
import colorama
import ctypes

# Initialiser Colorama
colorama.init()

# Changer le titre de la fenêtre
ctypes.windll.kernel32.SetConsoleTitleW("MrA ViperScan")

# Définir les couleurs
COLOR_BLUE = colorama.Fore.BLUE
COLOR_GREEN = colorama.Fore.GREEN
COLOR_YELLOW = colorama.Fore.YELLOW
COLOR_RED = colorama.Fore.RED
COLOR_RESET = colorama.Style.RESET_ALL

def rechercher_fichiers_par_mot(mot_cle, chemin_recherche):
    fichiers_trouves = []

    for root, _, _ in os.walk(chemin_recherche):
        for chemin_fichier in glob.glob(os.path.join(root, "*")):
            if mot_cle.lower() in os.path.basename(chemin_fichier).lower():
                fichiers_trouves.append(chemin_fichier)
                print("Fichier trouvé :", COLOR_GREEN + chemin_fichier + COLOR_RESET)

    return fichiers_trouves

def rechercher_fichiers_par_liste_mots(mots_cles, chemin_recherche):
    fichiers_trouves = []

    for root, _, _ in os.walk(chemin_recherche):
        for chemin_fichier in glob.glob(os.path.join(root, "*")):
            nom_fichier = os.path.basename(chemin_fichier).lower()
            if any(mot.lower() in nom_fichier for mot in mots_cles):
                fichiers_trouves.append(chemin_fichier)
                print("Fichier trouvé :", COLOR_GREEN + chemin_fichier + COLOR_RESET)

    return fichiers_trouves

# Afficher les crédits
print(COLOR_BLUE + "Crédits du développeur :" + COLOR_RESET)
print("Développé par : " + COLOR_GREEN + "MrAnthony#6281" + COLOR_RESET)
print("Pour " + COLOR_YELLOW + "Synaria" + COLOR_RESET)

# Obtenir l'option de recherche à partir de l'entrée de l'utilisateur
option_recherche = input("Veuillez choisir une option de recherche : \n1. Rechercher avec un mot\n2. Rechercher avec une liste de mots\n")

# Obtenir le mot-clé ou la liste de mots à partir de l'entrée de l'utilisateur
if option_recherche == "1":
    mot_cle = input("Entrez le mot-clé à rechercher : ")
elif option_recherche == "2":
    mots_cles = input("Entrez une liste de mots séparés par des espaces : ").split()

# Obtenir le répertoire de recherche à partir de l'entrée de l'utilisateur
chemin_recherche = input("Entrez le répertoire de recherche : ")

# Effacer l'écran
os.system('cls' if os.name == 'nt' else 'clear')

# Afficher les crédits
print(COLOR_BLUE + "Crédits du développeur :" + COLOR_RESET)
print("Développé par : " + COLOR_GREEN + "MrAnthony#6281" + COLOR_RESET)
print("Pour " + COLOR_YELLOW + "Synaria" + COLOR_RESET)
print("\nOption de recherche: " + option_recherche)

if option_recherche == "1":
    print("\nMot-clé recherché: " + mot_cle)
elif option_recherche == "2":
    print("\nListe de mots recherchés: ", mots_cles)

print("\nRépertoire sélectionné: " + chemin_recherche)

# Mesurer le temps d'exécution
temps_debut = time.time()

# Appeler la fonction appropriée en fonction de l'option de recherche
if option_recherche == "1":
    resultats_recherche = rechercher_fichiers_par_mot(mot_cle, chemin_recherche)
elif option_recherche == "2":
    resultats_recherche = rechercher_fichiers_par_liste_mots(mots_cles, chemin_recherche)

temps_fin = time.time()
temps_execution = temps_fin - temps_debut

if resultats_recherche:
    print("\nLa recherche est terminée.")
else:
    print("\nLa recherche est terminée. Aucun fichier trouvé.")

print(COLOR_YELLOW + "\nTemps d'exécution :", temps_execution, "secondes." + COLOR_RESET)

# Afficher les crédits
print("Développé par : " + COLOR_GREEN + "MrAnthony#6281" + COLOR_RESET)
print("Pour " + COLOR_YELLOW + "Synaria" + COLOR_RESET)

input("\nAppuyez sur Entrée pour quitter...")

# Réinitialiser Colorama
colorama.deinit()
