# Classe de controle
class Control:
    #Metodo construtor
    def __init__(self,view,model):
        #Atributos
        self.view = view
        self.model = model

    #metodo exibir menu
    def exibir_menu(self):
        #adcionar o metodo da classe view
        self.view.exibir_menu()

    #Metodo para recuperar lista de compras
    def get_lista_compras(self):
        #adcionar o metodo da classe model
        return self.model.get_lista_compras()
