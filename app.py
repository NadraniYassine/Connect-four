
import game
from tkinter import *
class Application:
    def __init__(self,line,column):
        self.game=game.Game()
        self.player=1
        self.fen=Tk()
        self.fen.title("Connect 4")
        self.can=Canvas(self.fen,width=400,height=430,bg='blue')
        self.can.pack(side=TOP,padx=5,pady=5)
        self.can.create_rectangle(5,380,80,420,fill="cyan",tags="rec")
        self.can.create_text(30,395,tags="rec",text="Player")
        if self.player==1:
            self.can.create_oval(55,385,75,405,fill="red")
        if self.player==2:
            self.can.create_oval(55,385,75,405,fill="yellow")
        Bouton_nv=Button(self.fen,text="New Game",command=self.newGame)
        Bouton_quit=Button(self.fen,text="Quit",command=self.fen.destroy)
        Bouton_nv.pack()
        Bouton_quit.pack()
        self.fen.mainloop()
    def createBoard(self):
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
    def newGame(self):
        game.MyGame.__init__()
        #self.__init__(6,7)
        self.createBoard()
        self.victory=False
        self.can.create_rectangle(150,380,350,420,fill="blue",outline="blue")
        self.can.bind('<Button-1>',self.clic)
    def clic(self,event):
        if not self.victory:
            x=event.x
            x=x-25
            column=x//50
            game.MyGame.empiler(self.player,column)
            line=game.MyGame.checkersInColmun(column)-1
            line=game.MyGame.checkersInColmun(column)-1
            if self.player==1:
                x1=25+(column)*50
                x2=75+(column)*50
                y1=350-(line)*50
                y2=300-(line)*50
                self.can.create_oval(x1,y1,x2,y2,fill="red")
                if game.MyGame.testAll(column+1):
                    self.can.create_text(250,395,text="Player 1 won!")
                    self.victory=True
            else:
                x1=25+(column)*50
                x2=75+(column)*50
                y1=350-(line)*50
                y2=300-(line)*50
                self.can.create_oval(x1,y1,x2,y2,fill="yellow")
                if game.MyGame.testAll(column+1):
                    self.can.create_text(250,395,text="Player 2 won!")
                    self.victory=True
            if self.player==1:
                self.player=2
                self.can.create_oval(55,385,75,405,fill="yellow")
            else:
                self.player=1
                self.can.create_oval(55,385,75,405,fill="red")
Application(6,7)
