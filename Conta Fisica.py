from Conta import Conta
#pessoa fisica
class Fisica(Conta):
    def __init__(self,sexo,idade,cpf,nconta,nome,tipo):
        self.sexo = sexo
        self.idade = idade
        self.cpf = cpf
        self.nconta = nconta
        super().__init__(nome,tipo)