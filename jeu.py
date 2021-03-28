class Game:
    def __init__(self):
        self.board=[[0 for i in range(7)] for j in range(6)]
    #Exerci 2
    def afficher(self):
        for i in range (len (self.board)):
            line="|"
            for j in range (len(self.board[0])):
                if self.board[len (self.board)-1-i][j]==0:
                    line+=" |"
                if self.board[len (self.board)-1-i][j]==1:
                    line+="X|"
                if self.board[len (self.board)-1-i][j]==2:
                    line+="O|"
            print(line)
        print(" - - - - - - - ")
        print(" 1 2 3 4 5 6 7 ")
    def checkersInColmun(self,numColumn):
        i=0
        for k in range (len(self.board)):
            if self.board[k][numColumn]!=0:
                i+=1
        return(i)
    def empiler(self,colour,numColumn):
        nb_column=self.checkersInColmun(numColumn)
        self.board[nb_column][numColumn]=colour
        self.afficher()
    def checkersInDirection(self,t,i,j,delta_i, delta_j):
#arguments: board, numéro de line, numéro de column,delta_i, delta_j
        counter=0 #nombre de pions identiques selon la directiondemandée
        colour=t[i][j]
        while i+delta_i>=0 and i+delta_i<len(t) and j+delta_j>=0 and j+delta_j<len(t[i]) and t[i+delta_i][j+delta_j]==colour:
#tant que la case voisine est dans le board et est de lamême colour
            counter+=1 #on comte le pion dans cette case voisine
#on doit aussi décaler la case dans la directiondemandée pour préparer le prochain test (le voisin du voisin):
            i=i+delta_i
            j=j+delta_j
        return counter

    def test_lines(self,column,line):
        nb1=self.checkersInDirection(self.board,line,column,0,1)
        nb2=self.checkersInDirection(self.board,line,column,0,-1)
        if nb1+nb2+1==4:
            print("The player ",self.board[line][column]," won! Bravo! ")
            return(True)
        return(False)

    def test_column(self,column,line):
        nb1=self.checkersInDirection(self.board,line,column,1,0)
        nb2=self.checkersInDirection(self.board,line,column,-1,0)
        if nb1+nb2+1==4:
            print("The player ",self.board[line][column]," won! Bravo!")
            return(True)
        return(False)

    def test_diagonal(self,column,line):
        nb1=self.checkersInDirection(self.board,line,column,1,1)
        nb2=self.checkersInDirection(self.board,line,column,-1,-1)
        if nb1+nb2+1==4:
            print("The player ",self.board[line][column]," won ! Bravo!")
            return(True)
        nb1=self.checkersInDirection(self.board,line,column,-1,1)
        nb2=self.checkersInDirection(self.board,line,column,1,-1)
        if nb1+nb2+1==4:
            print("The player ",self.board[line][column]," won! Bravo!")
            return(True)
        return(False)

    def testAll(self,chosenColumn):
        k=0
        while self.board[k][chosenColumn-1]!=0 and k<5:
            k+=1
        line=k-1
        column=chosenColumn-1
        if self.test_lines(column,line):
            return(True)
        if self.test_column(column,line):
            return(True)
        if self.test_diagonal(column,line):
            return(True)
        return(False)
MyGame=Game()
MyGame.afficher()
print(MyGame.board)
