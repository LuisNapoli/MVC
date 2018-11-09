

#classe BD_Simulado
class BD_Simulado():
    #metodo construtor
    def __init__(self):
        #atributos
        self.lista_compra = []
        self.carregar_lista_compra()

        #metodo carregar lista de compra
    def carregar_lista_compra(self):
        #colocar aqui codigo para abrir arquivo
        #cada linha do arquivo separar nomee qtde split(';')
        #cada linha do arquivo criar um objeto de Item_Compra
        #Iserir o objeto na lista de compra

        #remover essa parte
        item1 = Item_Compra('tomate',10)
        item2 = Item_Compra('banana',5)
        item3 = Item_Compra('cafe',1)

        self.lista_compra.append(item1)
        self.lista_compra.append(item2)
        self.lista_compra.append(item3)
        #remover ate aqui

    def gravar_lista_compra(self):
        #abrir arquivo para gravaçao (apagar o conteud)
        # percorrer lista
        #para cada item da lista converter em string
        #salvar no arquivo

        #remover essa parte
        for item in self.lista_compra:
            print(item.to_string())
        #remover ate aqu

    #metodo para retornar um Item_Compra de acordo com seu nome
    def get_item_compra(self,nome):
        #percorrer a lista
        for item in self.lista_compra:
            #se nome for igaul
            if (item.get_nome() == nome):
                return item
        #se nao encontrar
        return None
    #metodo para retornar lista de compras
    def get_lista_compras