# Classe de modelo
class Model:
    #Metodo construtor
    def __init__(self):
        self.lista_compras = {'Omo': 1, 'Arroz': 2, 'Bombril': 10}

    #metodo que recupera a lista
    def get_lista_compras(self):
        return self.lista_compras