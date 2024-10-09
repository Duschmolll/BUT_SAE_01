import main
import mm
import math


def testerChoixPlayer():
    secretCode = [mm.Noir, mm.Blanc, mm.Vert, mm.Vert, mm.Rouge]
    propPlayer1 = [mm.Noir, mm.Blanc, mm.Vert, mm.Vert, mm.Rouge]
    propPlayer2 = [mm.Gris, mm.Blanc, mm.Noir, mm.Vert, mm.Vert]
    propPlayer3 = [mm.Orange, mm.Orange, mm.Orange, mm.Orange, mm.Vert]

    if main.checkanswerPlayer(propPlayer1, secretCode) == (5, 0):
        print("Test 1 OK")
    else:
        print("Test 1 KAPUT")
    if main.checkanswerPlayer(propPlayer2, secretCode) == (2, 2):
        print("Test 2 OK")
    else:
        print("Test 2 KAPUT")
    if main.checkanswerPlayer(propPlayer3, secretCode) == (0, 1):
        print("Test 3 OK")
    else:
        print("Test 3 KAPUT")


def testDistance():
    if mm.distance([0, 0], [1, 1]) == math.sqrt(2):
        print("Test MM 01 OK")
    else:
        print("Test MM 01 KAPUT")
    if mm.distance([1, 1], [1, 1]) == math.sqrt(0):
        print("Test MM 01 OK")
    else:
        print("Test MM 01 KAPUT")
    if mm.distance([0, 0], [-1, -1]) == math.sqrt(2):
        print("Test MM 01 OK")
    else:
        print("Test MM 01 KAPUT")
    if mm.distance([1, 1], [0, 0]) == math.sqrt(2):
        print("Test MM 01 OK")
    else:
        print("Test MM 01 KAPUT")
    if mm.distance([0, 0], [0, 0]) == math.sqrt(0):
        print("Test MM 01 OK")
    else:
        print("Test MM 01 KAPUT")
    if mm.distance([-1, -1], [-1, -1]) == 0:
        print("Test MM 01 OK")
    else:
        print("Test MM 01 KAPUT")


testerChoixPlayer()
testDistance()
print(mm.distance([-1, -1], [-1, -1]))
