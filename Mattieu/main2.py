from mm import*
# décla variables globale
secretCode = []
#secretCode = [Noir, Blanc, Vert, Vert, Rouge]
testprop=[Vert,Vert,Vert,Blanc,Vert]
essaiJoueur:int=2

def randomSecret() -> list:#Fonction permettant de créer la combinaison secrétes de pion a trouver par le joueur
    for i in range(5):
        secretCode.append(TabCouleur[random.randint(0, 7)])
    return secretCode

def check(laProposition:list)->None:#Fonction vérifiant  le nb de pion bien placé ou non entre la combinaison créer par le joueur et le code Secret
    wellPlaced=0
    wrongPlace=0
    secretCodeCopy=secretCode.copy()
    propCopy=laProposition.copy()

    print(len(secretCodeCopy))
    i=0
    while i< len(secretCodeCopy):        
        if secretCodeCopy[i]==propCopy[i]:
            secretCodeCopy.pop(i)
            propCopy.pop(i)
            wellPlaced+=1             
        else:
            i+=1
    i=0
    while i<len(secretCodeCopy):
        k=0
        while k<len(secretCodeCopy):
            if secretCodeCopy[i]==propCopy[k] :
                    secretCodeCopy.pop(i)
                    propCopy.pop(k)
                    i-=1
                    wrongPlace+=1
                    k=len(secretCodeCopy)
            else:
                k+=1
        i+=1
        
    return (wellPlaced,wrongPlace)

def main():
    pygame.init()
    screen:pygame = pygame.display.set_mode((1000, 750))
    screen.fill(Blanc)
    game_is_running = True
    secretCode = randomSecret()
    print(secretCode)
    afficherPlateau(screen)
    afficherChoixCouleur(screen)
    #afficherSecret(screen,secretCode)
    essaiJoueur=2
    while game_is_running :
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                game_is_running=False
                pygame.quit()
        prop = construireProposition(screen,essaiJoueur)
        print(check(prop))
        afficherResultat(screen,check(prop),essaiJoueur)
        essaiJoueur+=1
        pygame.display.update()       
        if prop == secretCode:
            afficherResultat(screen,check(prop),essaiJoueur)

if __name__=="__main__":
    main()


