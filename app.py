
import jeu
from tkinter import *
class Application:
    def __init__(self,ligne,colonne):
        self.jeu=jeu.Jeu()
        self.joueur=1
        self.fen=Tk()
        self.fen.title("Le jeu de Puissance 4")
        self.can=Canvas(self.fen,width=400,height=430,bg='blue')
        self.can.pack(side=TOP,padx=5,pady=5)
        self.can.create_rectangle(5,380,80,420,fill="cyan",tags="rec")
        self.can.create_text(30,395,tags="rec",text="Joueur")
        if self.joueur==1:
            self.can.create_oval(55,385,75,405,fill="red")
        if self.joueur==2:
            self.can.create_oval(55,385,75,405,fill="yellow")
        Bouton_nv=Button(self.fen,text="Nouveau Jeu",command=self.nouveau_jeu)
        Bouton_quit=Button(self.fen,text="Quitter",command=self.fen.destroy)
        Bouton_nv.pack()
        Bouton_quit.pack()
        self.fen.mainloop()
    def dessiner_plateau(self):
        x1=-25
        y1=0
        x2=25
        y2=50
        for i in range(6):
            y1=y1+50
            y2=y2+50
            x1=-25
            x2=25
            for j in range (7):
                x1=x1+50
                x2=x2+50
                self.can.create_oval(x1,y1,x2,y2,fill="white")
    def nouveau_jeu(self):
        jeu.MonJeu.__init__()
        #self.__init__(6,7)
        self.dessiner_plateau()
        self.victoire=False
        self.can.create_rectangle(150,380,350,420,fill="blue",outline="blue")
        self.can.bind('<Button-1>',self.clic)
    def clic(self,event):
        if not self.victoire:
            x=event.x
            x=x-25
            colonne=x//50
            jeu.MonJeu.empiler(self.joueur,colonne)
            ligne=jeu.MonJeu.combiendanscolonne(colonne)-1
            if self.joueur==1:
                x1=25+(colonne)*50
                x2=75+(colonne)*50
                y1=350-(ligne)*50
                y2=300-(ligne)*50
                self.can.create_oval(x1,y1,x2,y2,fill="red")
                if jeu.MonJeu.test_tout(colonne+1):
                    self.can.create_text(250,395,text="Victoire du Joueur 1")
                    self.victoire=True
            else:
                x1=25+(colonne)*50
                x2=75+(colonne)*50
                y1=350-(ligne)*50
                y2=300-(ligne)*50
                self.can.create_oval(x1,y1,x2,y2,fill="yellow")
                if jeu.MonJeu.test_tout(colonne+1):
                    self.can.create_text(250,395,text="Victoire du Joueur 2")
                    self.victoire=True
            if self.joueur==1:
                self.joueur=2
                self.can.create_oval(55,385,75,405,fill="yellow")
            else:
                self.joueur=1
                self.can.create_oval(55,385,75,405,fill="red")
Application(6,7)
