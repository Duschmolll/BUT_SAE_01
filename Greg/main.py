from mm import *

pygame.init()
screen: pygame = pygame.display.set_mode((1000, 750))
screen.fill(Blanc)


def randomSecret() -> list:
    secretCode = []
    for i in range(5):
        secretCode.append(TabCouleur[random.randint(0, 7)])
    return secretCode


secretCode = randomSecret()
game_is_running = True

afficherPlateau(screen)
afficherChoixCouleur(screen)
afficherSecret(screen, secretCode)


def checkanswerPlayer():
    propPlayer = construireProposition(screen, userTry)

    wellPlaced = 0
    wrongPlaced = 0

    for i in range(5):
        if secretCode[i] == propPlayer[i]:
            wellPlaced += 1
        else:
            for k in range(i, 5):
                if secretCode[i] == propPlayer[k]:
                    wrongPlaced += 1

    resultat = (wellPlaced, wrongPlaced)
    afficherResultat(screen, resultat, userTry)
    return wellPlaced


secretBroken = False
gameEnded = False
userTry = 2

while not secretBroken and not gameEnded:
    if userTry == 17:
        gameEnded == True
    elif checkanswerPlayer() == 5:
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
