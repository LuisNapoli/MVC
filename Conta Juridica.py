from Conta import Conta
#conta pessoa juridica
class Juridica(Conta):
    def __init__(self,cnpj,nome, tipo):
        self.cnpj = cnpj
