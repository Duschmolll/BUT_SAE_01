import mm
import random
import pygame

# Global Var:
secretCode = []


# On utlise un randInt(0,7) 5 fois pour choisir aléatoirement 5 couleurs de la liste TabCouleur.
def randomSecret() -> list:

    for i in range(5):
        secretCode.append(mm.TabCouleur[random.randint(0, 7)])
    return secretCode


# Fonction pour vérifier la proposition du joueurs face au code secret.
def checkanswerPlayer(propPlayer: tuple, secret: list):

    wellPlaced = 0
    wrongPlaced = 0
    alreadyCheckSecret = []
    alreadyCheckPlayer = []

    # Boucle pour regarder si des couleurs de la prop du Joueurs sont présent et bien placé
    for i in range(5):
        if secret[i] == propPlayer[i]:
            wellPlaced += 1
            alreadyCheckSecret.append(i)
            alreadyCheckPlayer.append(i)

    # Boucle pour regarder si des couleurs de la prop du Joueurs sont présent mais mal placé en faisant attention au doublon.
    for i in range(5):
        for k in range(0, 5):
            if (
                secret[i] == propPlayer[k]
                and i not in alreadyCheckSecret
                and k not in alreadyCheckPlayer
            ):
                wrongPlaced += 1
                alreadyCheckSecret.append(i)
                alreadyCheckPlayer.append(k)

    return (wellPlaced, wrongPlaced)


# Fonction principale du programme.
def main():
    # Mise en route de pygame.
    pygame.init()
    screen: pygame = pygame.display.set_mode((1000, 750))
    screen.fill(mm.Blanc)

    # secretCode = randomSecret()
    secretCode = [mm.Noir, mm.Blanc, mm.Vert, mm.Vert, mm.Rouge]

    # Mise en place du GUI en utilisant les fonction de mm.py
    mm.afficherPlateau(screen)
    mm.afficherChoixCouleur(screen)
    mm.afficherSecret(screen, secretCode)

    # Variable
    secretBroken = False
    gameEnded = False
    userTry = 2

    # Boucle pour continuer à demander une proposition si ne joueurs est à moins de 15 essaie et que le code n'as pas été trouvé.
    while not secretBroken and not gameEnded:
        check = checkanswerPlayer(mm.construireProposition(screen, userTry), secretCode)
        mm.afficherResultat(screen, check, userTry)
        if userTry == 17:
            gameEnded == True
        elif check[0] == 5:
            secretBroken = True
        else:
            userTry += 1
            print(userTry)

    # Savoir quoi afficher lors de la sortie de la boucle précédente. Perdu ou Gagner.
    if secretBroken == True:
        print("GG, vous avez trouvé la combinaison en ", userTry - 1, " coups !")
        # afficherSecret(screen, secretCode)
    elif gameEnded == True:
        print("Perdu, vous dépassé vos 15 coups")
        # afficherSecret(screen, secretCode)

    # Laisser tourner Pygame tant que le joueurs n'as pas décidé de quitter le jeu.
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("c'est fini!!!")
                pygame.quit()
                running = False


if __name__ == "__main__":
    main()
