class Jeu:
    def __init__(self):
        self.plateau=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

    #Exerci 2
    def afficher(self):
        for i in range (len (self.plateau)):
            ligne="|"
            for j in range (len(self.plateau[0])):
                if self.plateau[len (self.plateau)-1-i][j]==0:
                    ligne+=" |"
                if self.plateau[len (self.plateau)-1-i][j]==1:
                    ligne+="X|"
                if self.plateau[len (self.plateau)-1-i][j]==2:
                    ligne+="O|"
            print(ligne)
        print(" - - - - - - - ")
        print(" 1 2 3 4 5 6 7 ")
    def combiendanscolonne(self,numcolonne):
        i=0
        for k in range (len(self.plateau)):
            if self.plateau[k][numcolonne]!=0:
                i+=1
        return(i)
    def empiler(self,couleur,numcolonne):
        nb_colonne=self.combiendanscolonne(numcolonne)
        self.plateau[nb_colonne][numcolonne]=couleur
        self.afficher()
    def combien_dans_la_direction(self,t,i,j,delta_i, delta_j):
#arguments: plateau, numéro de ligne, numéro de colonne,delta_i, delta_j
        compteur=0 #nombre de pions identiques selon la directiondemandée
        couleur=t[i][j]
        while i+delta_i>=0 and i+delta_i<len(t) and j+delta_j>=0 and j+delta_j<len(t[i]) and t[i+delta_i][j+delta_j]==couleur:
#tant que la case voisine est dans le plateau et est de lamême couleur
            compteur+=1 #on comte le pion dans cette case voisine
#on doit aussi décaler la case dans la directiondemandée pour préparer le prochain test (le voisin du voisin):
            i=i+delta_i
            j=j+delta_j
        return compteur

    def test_lignes(self,colonne,ligne):
        nb1=self.combien_dans_la_direction(self.plateau,ligne,colonne,0,1)
        nb2=self.combien_dans_la_direction(self.plateau,ligne,colonne,0,-1)
        if nb1+nb2+1==4:
            print("Le joueur ",self.plateau[ligne][colonne]," gagne ! Bravo !")
            return(True)
        return(False)

    def test_colonne(self,colonne,ligne):
        nb1=self.combien_dans_la_direction(self.plateau,ligne,colonne,1,0)
        nb2=self.combien_dans_la_direction(self.plateau,ligne,colonne,-1,0)
        if nb1+nb2+1==4:
            print("Le joueur ",self.plateau[ligne][colonne]," gagne ! Bravo !")
            return(True)
        return(False)

    def test_diagonale(self,colonne,ligne):
        nb1=self.combien_dans_la_direction(self.plateau,ligne,colonne,1,1)
        nb2=self.combien_dans_la_direction(self.plateau,ligne,colonne,-1,-1)
        if nb1+nb2+1==4:
            print("Le joueur ",self.plateau[ligne][colonne]," gagne ! Bravo !")
            return(True)
        nb1=self.combien_dans_la_direction(self.plateau,ligne,colonne,-1,1)
        nb2=self.combien_dans_la_direction(self.plateau,ligne,colonne,1,-1)
        if nb1+nb2+1==4:
            print("Le joueur ",self.plateau[ligne][colonne]," gagne ! Bravo !")
            return(True)
        return(False)

    def test_tout(self,colonne_choisi):
        k=0
        while self.plateau[k][colonne_choisi-1]!=0 and k<5:
            k+=1
        ligne=k-1
        colonne=colonne_choisi-1
        if self.test_lignes(colonne,ligne):
            return(True)
        if self.test_colonne(colonne,ligne):
            return(True)
        if self.test_diagonale(colonne,ligne):
            return(True)
        return(False)
MonJeu=Jeu()
MonJeu.afficher()
print(MonJeu.plateau)