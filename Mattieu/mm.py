import pygame
import random
import math




# definition de variables globales
Noir = (0, 0, 0)
Blanc = (255, 255, 255)
Gris = (128, 128, 128)
Bleu = (0, 0, 255)
Rouge = (255, 0, 0)
Vert = (0, 255, 0)
Orange = (225, 127, 0)
Rose = (255, 0, 127)

Marron = (160, 60, 0)


TabCouleur = [Noir, Blanc, Gris, Bleu, Rouge, Vert, Orange, Rose]


def afficherSecret(laFenetre: pygame.Surface, leSecret: list) -> None:
    for i in range(len(leSecret)):
        pygame.draw.circle(laFenetre, leSecret[i], [320 + 40 * i, 20], 15)
        pygame.draw.circle(laFenetre, Noir, [320 + 40 * i, 20], 15, 1)
    pygame.display.update()


def afficherCombinaison(
    laFenetre: pygame.Surface, laCombinaison: list, numLigne: int
) -> None:

    for i in range(5):
        pygame.draw.circle(
            laFenetre, Marron, [320 + 40 * i, 40 + 40 * (numLigne - 1)], 15
        )

    for i in range(len(laCombinaison)):
        pygame.draw.circle(
            laFenetre, laCombinaison[i], [320 + 40 * i, 40 + 40 * (numLigne - 1)], 15
        )
        pygame.draw.circle(
            laFenetre, Noir, [320 + 40 * i, 40 + 40 * (numLigne - 1)], 15, 1
        )

    pygame.display.update()


def afficherPlateau(f: pygame.Surface) -> None:
    pygame.draw.rect(f, Marron, [300, 0, 200, 40])
    for i in range(5):
        pygame.draw.rect(f, Noir, [300 + 40 * i, 0, 40, 40], 1)
    pygame.draw.rect(f, Marron, [300, 60, 200, 40 * 15])
    pygame.draw.rect(f, Marron, [520, 60, 40, 40 * 15])

    for l in range(15):
        for i in range(5):
            pygame.draw.rect(f, Noir, [300 + 40 * i, 60 + 40 * l, 40, 40], 1)
        pygame.draw.rect(f, Noir, [520, 60 + 40 * l, 40, 40], 1)

    text1 = "nb noir = nb mal placé"
    text2 = "nb blanc = nb bien placé"
    text3 = "choix pion"
    text4 = "retirer dernier pion"
    myfont = pygame.font.SysFont("monospace", 15)
    label1 = myfont.render(text1, 1, Noir)
    label2 = myfont.render(text2, 1, Noir)
    label3 = myfont.render(text3, 1, Noir)
    label4 = myfont.render(text4, 1, Noir)
    f.blit(label3, (100, 200))
    f.blit(label4, (100, 430))
    f.blit(label1, (570, 200))
    f.blit(label2, (570, 220))
    pygame.display.update()


def afficherChoixCouleur(f: pygame.Surface) -> None:
    for i in range(len(TabCouleur)):
        pygame.draw.circle(f, TabCouleur[i], [75, 80 + 40 * i], 15)
        pygame.draw.circle(f, Noir, [75, 80 + 40 * i], 15, 1)
    pygame.draw.circle(f, Marron, [75, 80 + 40 * 9], 15)
    pygame.draw.circle(f, Noir, [75, 80 + 40 * 9], 15, 1)
    pygame.display.update()


def distance(a: list, b: list) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def getChoixCouleur() -> None:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("c'est fini!!!")
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                positionSouris = pygame.mouse.get_pos()
                if distance(positionSouris, [75, 80 + 40 * 9]) < 15:
                    return None
                for i in range(len(TabCouleur)):
                    if distance(positionSouris, [75, 80 + 40 * i]) < 15:
                        return TabCouleur[i]


def construireProposition(f: pygame.Surface, ligne: int) -> list:
    proposition = []

    while len(proposition) < 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        couleur = getChoixCouleur()
        if couleur == None:
            if len(proposition) > 0:
                del proposition[-1]
        else:
            proposition.append(couleur)
        afficherCombinaison(f, proposition, ligne)
        pygame.display.update()

    return proposition


def afficherResultat(f: pygame.Surface, res, ligne):
    x = 520
    y = 20 + 40 * (ligne - 1)
    centres = [
        (x + 6, y + 6),
        (x + 6, y + 34),
        (x + 20, y + 20),
        (x + 34, y + 6),
        (x + 34, y + 34),
    ]
    i = 0
    while i < res[0]:
        pygame.draw.circle(f, Blanc, centres[i], 4)
        i = i + 1
    j = 0
    while j < res[1]:
        pygame.draw.circle(f, Noir, centres[i], 4)
        i = i + 1
        j = j + 1
    pygame.display.update()