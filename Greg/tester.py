import main
import mm
import math
import random


# Test de la fonction de comparaison du code secret et de la proposition du joueur.
def testerChoixPlayer():
    secretCode = [mm.Noir, mm.Blanc, mm.Vert, mm.Vert, mm.Rouge]
    propPlayer1 = [mm.Noir, mm.Blanc, mm.Vert, mm.Vert, mm.Rouge]
    propPlayer2 = [mm.Gris, mm.Blanc, mm.Noir, mm.Vert, mm.Vert]
    propPlayer3 = [mm.Orange, mm.Orange, mm.Orange, mm.Orange, mm.Vert]
    propPlayer4 = [mm.Rouge, mm.Rouge, mm.Rouge, mm.Rouge, mm.Rouge]

    result = main.checkanswerPlayer(propPlayer1, secretCode)
    if result == (5, 0):
        print("Test 1 OK")
    else:
        print("Test 1 KAPUT: ", result, "| Expected : (5, 0)")

    result = main.checkanswerPlayer(propPlayer2, secretCode)
    if main.checkanswerPlayer(propPlayer2, secretCode) == (2, 2):
        print("Test 2 OK")
    else:
        print("Test 2 KAPUT: ", result, "| Expected : (2, 2)")

    result = main.checkanswerPlayer(propPlayer3, secretCode)
    if main.checkanswerPlayer(propPlayer3, secretCode) == (0, 1):
        print("Test 3 OK")
    else:
        print("Test 3 KAPUT: ", result, "| Expected : (0, 1)")

    result = main.checkanswerPlayer(propPlayer4, secretCode)
    if main.checkanswerPlayer(propPlayer4, secretCode) == (1, 0):
        print("Test 4 OK")
    else:
        print("Test 4 KAPUT: ", result, "| Expected : (1, 0)")


# Test de la fonction distance.
def testDistance():
    if mm.distance([0, 0], [1, 1]) == math.sqrt(2):
        print("Test MM 01 OK")
    else:
        print("Test MM 01 KAPUT")
    if mm.distance([1, 1], [1, 1]) == math.sqrt(0):
        print("Test MM 02 OK")
    else:
        print("Test MM 02 KAPUT")
    if mm.distance([0, 0], [-1, -1]) == math.sqrt(2):
        print("Test MM 03 OK")
    else:
        print("Test MM 03 KAPUT")
    if mm.distance([1, 1], [0, 0]) == math.sqrt(2):
        print("Test MM 04 OK")
    else:
        print("Test MM 04 KAPUT")
    if mm.distance([0, 0], [0, 0]) == math.sqrt(0):
        print("Test MM 05 OK")
    else:
        print("Test MM 05 KAPUT")
    if mm.distance([-1, -1], [-1, -1]) == 0:
        print("Test MM 06 OK")
    else:
        print("Test MM 06 KAPUT")


# Test que la randomisation du code secret prends bien toutes les couleurs possible.
def testRandom():
    rangeofRand = []
    for i in range(1000):
        rand = random.randint(0, 7)
        if rand not in rangeofRand:
            rangeofRand.append(rand)
    rangeofRand.sort()
    if rangeofRand == [0, 1, 2, 3, 4, 5, 6, 7]:
        print("Test Random Range OK")
    else:
        print("Random Range KAPUT: ", rangeofRand, " | Expected: [0,1,2,3,4,5,6]")


testerChoixPlayer()
testRandom()
testDistance()
