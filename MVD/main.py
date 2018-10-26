#programa principal

#importacao de classes
from view import View
from control import Control
from model import Model

#instanciar a model
m = Model()
#Instanciar a View
v = View()
#instanciar a Control
c = Control(v,m)
v.set_control(c)

#Exibir o menu
c.exibir_menu()