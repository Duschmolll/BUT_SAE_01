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
    secretCodeCopy=secretCode.copy()            #VARIABLES LOCALES
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

def afficherFin(f: pygame.Surface,txt:str,fontSize) -> None: #Fonction permettant d'afficher le message de fin de partie 
    text01 = txt
    myfont = pygame.font.SysFont("monospace", fontSize)    
    label1 = myfont.render(text01, 1, Noir)
    f.blit(label1, (150, 710))
    pygame.display.update()

def main():

    pygame.init()
    screen:pygame = pygame.display.set_mode((1000, 750))#AFFICHAGE
    screen.fill(Blanc)

    game_is_running = True
    secretBroken=False          #VARIABLES
    gameEnded=False
    secretCode = randomSecret()
    essaiJoueur=2
    alrDon=False

    print(secretCode)
    afficherPlateau(screen)                 #AFFICHAGE
    afficherChoixCouleur(screen)
    afficherSecret(screen,secretCode)
    
    while game_is_running :
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                game_is_running=False
                pygame.quit()       
        if not secretBroken and not gameEnded and game_is_running:
            laproposition = construireProposition(screen,essaiJoueur)
            checkResultat = check(laproposition)
            afficherResultat(screen,checkResultat,essaiJoueur)
           
            if essaiJoueur == 16:
                gameEnded = True
            elif checkResultat[0] == 5:
                secretBroken = True
            else:
                essaiJoueur += 1   
        if secretBroken == True and not alrDon:
            text = (
                "Bravo ! Vous avez trouvé la combinaison en "  #alrDon permet qui si le if a déja était fais une fois de ne plus le faire 
                + str(essaiJoueur - 1)
                + " coups !"
            )
            afficherFin(screen, text, 18)
            alrDon = True

        elif gameEnded == True and not alrDon:
            text = "Perdu, vous avez dépassé vos 15 coups." 
            afficherFin(screen, text, 18)
            alrDon = True
            


if __name__=="__main__":
    main()


