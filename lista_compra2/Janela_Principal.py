#importando as bibliotecas
from tkinter import *
from tkinter import messagebox
from segunda_janela import Segunda_Janela

#classe janela_principal
class Janela_principal(Tk):
    #metodo construtor
    def __init__(self):
        #executar o metodo da calasse mae
        super().__init__()
        #ajustar tamanho
        self.geometry('300x300+200+200')
        #colocar um titulo na janela
        self.title('Me salve')

        #widgets da tela
        self.btn_close = Button(self, width=10, text="Adeus", command=self.destroy)

        self.btn_ok = Button(self,width=10,text='Tirar de lá', command=self.btn_ok_click)
        self.txt_ok = Entry(self)
        self.lbl_ok = Label(self,text='Me tira daqui')

        #posicionando os widgets
        self.btn_close.place(x=10, y=250)
        self.btn_ok.place(x=140, y=250)
        self.lbl_ok.place(x=140, y=200)
        self.txt_ok.place(x=140, y=150)

        # == Menu ==
        #Criando um menu
        self.menu = Menu(self)
        #Criando um item de menu e subtitens
        self.menu_principal = Menu(self.menu, tearoff=0)
        self.menu_principal.add_command(label= 'Segunda Janela', command=self.criar_segunda_janela)
        self.menu_principal.add_command(label= 'Terceirizar Correios',command=self.menu_click)
        self.menu_principal.add_command(label= 'Bater no Quarto',command=self.menu_click)
        self.menu_principal.add_separator()
        self.menu_principal.add_command(label='Sair',command=self.destroy)
        self.menu.add_cascade(label='Modos de Salvar',menu=self.menu_principal)
        #mostrando o menu
        self.config(menu=self.menu)

    #metodo para fechar a janela
    def destroy(self):
       #janela de confirmação
        if messagebox.askokcancel('Deixar o Local','Não me abandone!'):
            super().destroy()

    #metodo para btn_ok
    def btn_ok_click(self):
        #mudar o texto do lbl_ok
        self.lbl_ok['text'] = self.txt_ok.get()

    #metodo para click no item de menu
    def menu_click(self):
        messagebox.showinfo('Menu')


    #metodo para criar a segnda janela
    def criar_segunda_janela(self):
        Segunda_Janela(self)