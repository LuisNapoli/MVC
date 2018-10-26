#classe de visualizacao
class View:
    #metodo construtor
    def __init__(self):
        self.control = None

    #guarda a control associada
    def set_control(self,control):
        self.control = control

    #Metodo de exibicao do menu
    def exibir_menu(self):
        resposta = True
        #exibir menu
        while resposta:
            print('''
            1. Exibir Lista
            2. Incluir Item
            3. Excluir Item
            4. Sair
            ''')
        #solicitar opcao
            resposta = input('Digite um número: ')

        #verificando a resposta
            if resposta == '1':
                print('\n Lista de itens')
                self.exibir_lista_compras()
            elif resposta == '2':
                print('\n Item incluído')
            elif resposta == '3':
                print('\n Item excluído')
            elif resposta == '4':
                print('\n Tchau!')
                resposta = False
            else:
                print('\n Valor incorreto!')

    #metodo para exibir lista de compras
    def exibir_lista_compras(self):
        #a lista de compras é um dicionario
        #percorrer o dicionario
        for chave, valor in self.control.get_lista_compras().items():
            print(f'\n- {chave} : {valor}')


