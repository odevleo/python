# como declarar uma classe 


# sintaxe simplificada
#class ExemploClasse:
 #   ''' docstring (opcional) serve para documentar a classe, explicar o que cada metodo vai fazer e para que serve a classe '''
 #   pass # classe sem nenhuma função definida ainda

#print(type(ExemploClasse)) # classe do elemento




class Cubo:
    '''  docstring  classe criada para calcular o valor do cubo de um valor passado no metodo construtor'''

    def __init__(self, valor):    # metodo construtor
        self.x = valor
        print("objeto criado!")
    
    def calcula_cubo(self):
        cubo = self.x * self.x * self.x        # a variavel x pode ser usada aqui devido ao self
        return 'Valor do cubo: ' + str(cubo)

#    def metodo_teste(self):
#        self.membro = 'valor'    # dado de instancia



objeto = Cubo(5)   # objeto criado, o valor entre os parenteses é o parametro passado para o metodo construtor
c = objeto.calcula_cubo()
print(c)