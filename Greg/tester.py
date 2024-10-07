from main import checkanswerPlayer


def testerChoixPlayer():
    secretCode = [
        (255, 0, 127),
        (255, 255, 255),
        (255, 255, 255),
        (255, 0, 0),
        (0, 0, 0),
    ]
    propPlayer1 = [
        (255, 0, 127),
        (255, 0, 127),
        (255, 0, 127),
        (255, 0, 127),
        (255, 0, 127),
    ]
    propPlayer2 = [
        (255, 0, 127),
        (255, 255, 255),
        (255, 255, 255),
        (255, 0, 0),
        (0, 0, 0),
    ]
    propPlayer3 = []
    if checkanswerPlayer(propPlayer1)[0] == 1:
        print("Test 1 OK")
    else:
        print("Test 1 KAPUT")


testerChoixPlayer()
