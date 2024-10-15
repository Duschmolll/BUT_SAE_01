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


# afficher Fin de partie:


def afficherFin(f: pygame.Surface, text: str, fontSize: int) -> None:
    text01 = text
    myfont = pygame.font.SysFont("monospace", fontSize)
    label1 = myfont.render(text01, 1, mm.Noir)

    f.blit(label1, (150, 700))
    pygame.display.update()


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
    running = True
    doItOnce = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("c'est fini!!!")
                running = False
                pygame.quit()

        if not secretBroken and not gameEnded and running:
            propJoueur = mm.construireProposition(screen, userTry)
            check = checkanswerPlayer(propJoueur, secretCode)
            mm.afficherResultat(screen, check, userTry)
            if userTry == 16:
                gameEnded = True
            elif check[0] == 5:
                secretBroken = True
            else:
                userTry += 1

        # Savoir quoi afficher lors de la sortie de la boucle précédente. Perdu ou Gagner.
        if secretBroken == True and not doItOnce:
            text = (
                "Bravo ! Vous avez trouvé la combinaison en "
                + str(userTry - 1)
                + " coups !"
            )
            afficherFin(screen, text, 18)
            doItOnce = True

        elif gameEnded == True and not doItOnce:
            text = "Perdu, vous avez dépassé vos 15 coups."
            afficherFin(screen, text, 18)
            doItOnce = True


if __name__ == "__main__":
    main()
