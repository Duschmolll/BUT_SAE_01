from mm import*
# décla variables globale
secretCode = []
secretCode = [Noir, Blanc, Vert, Vert, Rouge]
essaiJoueur:int=2




def randomSecret() -> list:#Fonction permettant de créer la combinaison secrétes de pion a trouver par le joueur

    for i in range(5):
        secretCode.append(TabCouleur[random.randint(0, 7)])
    return secretCode


def check(laProposition:list)->None:#Fonction vérifiant  le nb de pion bien placé ou non entre la combinaison créer par le joueur et le code Secret
    wellPlaced=0
    wrongPlace=0
    print(len(secretCode))
    for i in range (5):
        if secretCode[i]==laProposition[i]:
            wellPlaced+=1
            for k in range (i+1,5):
                if secretCode[i]==laProposition[k]:
                    wrongPlace+=1
    return (wellPlaced,wrongPlace)

def main():
    pygame.init()
    screen:pygame = pygame.display.set_mode((1000, 750))
    screen.fill(Blanc)
    game_is_running = True
    #secretCode = randomSecret()
    print(secretCode)
    afficherPlateau(screen)
    afficherChoixCouleur(screen)
    afficherSecret(screen,secretCode)
    essaiJoueur=2
    while game_is_running :
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                running=False
                pygame.quit()
            prop = construireProposition(screen,essaiJoueur)
            print(check(prop))
            while prop !=secretCode and essaiJoueur<5:
                    afficherResultat(screen,check(prop),essaiJoueur)
                    essaiJoueur+=1
                    prop = construireProposition(screen,essaiJoueur)        
            if prop == secretCode:
                afficherResultat(screen,check(prop),essaiJoueur)
            
    
main()


