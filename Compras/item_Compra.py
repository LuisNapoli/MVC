#class item_compra
class Item_Compra():
    #metodo construtor
    def __init__(self,nome,qtde):
        #Atributos
        self.nome = nome
        self.qtde = qtde
    #metodo que converte a classe em texto
    def to_string(self):
        return self.nome + ';' + self.qtde

    #metodo para retornar o nome
    def get_nome(self):
        return self.nome

    #retornar quantidade
    def get_qtde(self):
        return self.qtde