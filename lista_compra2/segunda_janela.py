#importacao das bibliotecas
from tkinter import *
from tkinter import messagebox


#classe segunda_janela
class Segunda_Janela(Toplevel):
    #metodo construtor
    def __init__(self,parent):
        #chamar o init da calasse mae
        super().__init__(parent)
        self.geometry('200x200+200+200')
        self.title('Segunda Janela')
        self.transient(parent)
        self.grab_set()
        self.btn_close = Button(self, width=10, text="Jogar pela Janela", command=self.destroy)
        # posicionando os widgets
        self.btn_close.place(x=10, y=150)

    #metodo para fechar a janela
    def destroy(self):
        #janela de confirmação
        if messagebox.askokcancel("Vai jogar pela janela?", "A janela não!"):
            super().destroy()


###




















    #