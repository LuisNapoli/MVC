


#classe controle
class Controle():
    #medoto contrutor
    def __init__(self):
        #atributos
        self.bg = BD_Simulado
        self.jnl = Janela_Principal(self)
        self.jnl.mainloop()

    #Metodo para retornar a lista de compra
    def get_lista_compra(self):
        return self.bd.get_lista_compra()