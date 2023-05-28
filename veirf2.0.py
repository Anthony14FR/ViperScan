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

def rechercher_fichiers(mot_cle, chemin_recherche):
    fichiers_trouves = []
    for root, _, _ in os.walk(chemin_recherche):
        for chemin_fichier in glob.glob(os.path.join(root, "*")):
            if mot_cle.lower() in os.path.basename(chemin_fichier).lower():
                fichiers_trouves.append(chemin_fichier)
                print("Fichier trouvé :", COLOR_GREEN + chemin_fichier + COLOR_RESET)
    return fichiers_trouves

# Afficher les crédits
print(COLOR_BLUE + "Crédits du développeur :" + COLOR_RESET)
print("Développé par : " + COLOR_GREEN + "MrAnthony#6281" + COLOR_RESET)
print("Pour " + COLOR_YELLOW + "Synaria" + COLOR_RESET)

# Obtenir le mot-clé à partir de l'entrée de l'utilisateur
mot_cle = input("Entrez le mot-clé à rechercher : ")

# Obtenir le répertoire de recherche à partir de l'entrée de l'utilisateur
chemin_recherche = input("Entrez le répertoire de recherche : ")

# Effacer l'écran
os.system('cls' if os.name == 'nt' else 'clear')

# Afficher les crédits
print(COLOR_BLUE + "Crédits du développeur :" + COLOR_RESET)
print("Développé par : " + COLOR_GREEN + "MrAnthony#6281" + COLOR_RESET)
print("Pour " + COLOR_YELLOW + "Synaria" + COLOR_RESET)
print("\n Mot recherché: " + mot_cle)
print("\n Répertoire selectionné: " + chemin_recherche )

# Mesurer le temps d'exécution
temps_debut = time.time()

# Appeler la fonction rechercher_fichiers
resultats_recherche = rechercher_fichiers(mot_cle, chemin_recherche)

temps_fin = time.time()
temps_execution = temps_fin - temps_debut

if resultats_recherche:
    print("\nLa recherche est terminée")
else:
    print("\nLa recherche est terminée. Aucun fichier trouvé.")

print(COLOR_YELLOW + "\nTemps d'exécution :", temps_execution, "secondes." + COLOR_RESET)

# Afficher les crédits

print("Développé par : " + COLOR_GREEN + "MrAnthony#6281" + COLOR_RESET)
print("Pour " + COLOR_YELLOW + "Synaria" + COLOR_RESET)

input("\nAppuyez sur Entrée pour quitter...")
input("\n" + COLOR_RED + "Appuyez sur Entrée pour confirmer..."+ COLOR_RESET)

# Réinitialiser Colorama
colorama.deinit()