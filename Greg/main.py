import mm
import random
import pygame

# Global Var:
secretCode = []


def randomSecret() -> list:

    for i in range(5):
        secretCode.append(mm.TabCouleur[random.randint(0, 7)])
    return secretCode


def checkanswerPlayer(propPlayer: tuple, secret: list):

    wellPlaced = 0
    wrongPlaced = 0
    alreadyCheckSecret = []
    alreadyCheckPlayer = []

    for i in range(5):
        if secret[i] == propPlayer[i]:
            wellPlaced += 1
            alreadyCheckSecret.append(i)
            alreadyCheckPlayer.append(i)

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


def main():

    pygame.init()
    screen: pygame = pygame.display.set_mode((1000, 750))
    screen.fill(mm.Blanc)

    # secretCode = randomSecret()
    secretCode = [mm.Noir, mm.Blanc, mm.Vert, mm.Vert, mm.Rouge]

    mm.afficherPlateau(screen)
    mm.afficherChoixCouleur(screen)
    mm.afficherSecret(screen, secretCode)

    secretBroken = False
    gameEnded = False
    userTry = 2

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

    if secretBroken == True:
        print("GG, vous avez trouvé la combinaison en ", userTry - 1, " coups !")
        # afficherSecret(screen, secretCode)
    elif gameEnded == True:
        print("Perdu, vous dépassé vos 15 coups")
        # afficherSecret(screen, secretCode)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("c'est fini!!!")
                pygame.quit()
                running = False


if __name__ == "__main__":
    main()
