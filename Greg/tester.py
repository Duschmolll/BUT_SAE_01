from main import checkanswerPlayer

Noir = (0, 0, 0)
Blanc = (255, 255, 255)
Gris = (128, 128, 128)
Bleu = (0, 0, 255)
Rouge = (255, 0, 0)
Vert = (0, 255, 0)
Orange = (225, 127, 0)
Rose = (255, 0, 127)

Marron = (160, 60, 0)


def testerChoixPlayer():
    secretCode = [Noir, Blanc, Vert, Vert, Rouge]
    propPlayer1 = [Noir, Blanc, Vert, Vert, Rouge]
    propPlayer2 = [Gris, Blanc, Noir, Vert, Vert]
    propPlayer3 = [Orange, Orange, Orange, Orange, Vert]
    if checkanswerPlayer(propPlayer1, secretCode) == (5, 0):
        print("Test 1 OK")
    else:
        print("Test 1 KAPUT")
    if checkanswerPlayer(propPlayer2, secretCode) == (2, 2):
        print("Test 2 OK")
    else:
        print("Test 2 KAPUT")
    if checkanswerPlayer(propPlayer3, secretCode) == (0, 1):
        print("Test 3 OK")
    else:
        print("Test 3 KAPUT")


testerChoixPlayer()
