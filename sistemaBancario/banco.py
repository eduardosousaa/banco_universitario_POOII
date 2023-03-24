from conta import Conta, Cliente
from random import randint

class Banco:

    __slots__ = ['_contas']
    
    def __init__(self):
        self._contas = [Conta('carlos', 'lacrel', 200, Cliente('Carlos', 'Henrique', '123'), 100.00)]

    @property
    def contas(self):
        return self._contas

    @contas.setter
    def contas(self, contas):
        self._contas = contas
    

    def cadastrarConta(self, usuario, senha, nome, sobrenome, cpf, saldo = 0.00, limite = 1000.00):
        try:
            titular = Cliente(nome, sobrenome, cpf)
            existeConta = True
            if len(self.contas) > 0:
                if self.verificaCPF(cpf) == True: #Verifica se cpf já está cadastrado
                    return False, 'O CPF informado já está cadastrado' 
                for x in self.contas:
                    if x.verificaUsuario(usuario): #Verifica se usuário existe
                        existeConta = False
                        return False, 'O usuário informado já existe'
                if existeConta: #usuário não existe
                    aux = True
                    while aux == True:
                        numero = randint(100, 999)
                        aux, aux2 = self.verificaNum(numero)
                    #print(f'Aux2: {aux2}')
                    self.contas.append(Conta(usuario, senha, numero, titular, saldo, limite))
                    return True, 'Conta Criada :)'
            else:
                numero = randint(100, 999)
                self.contas.append(Conta(usuario, senha, numero, titular, saldo, limite))
                return True, 'Conta Criada :)'

        except ValueError:
            return False

    
    def verificarLogin(self, usuario, senha):
        verifica = False
        for user, x in enumerate(self.contas):
            if x.verificaUsuario(usuario):
                aux = user
                verifica = True
        if verifica == True:
            if self.contas[aux].verificaSenha(senha):
                return True, 'Login bem sucedido :)', aux
            else:
                return False, 'Senha inválida! '
        else:
            return False, 'Usuário inválido! '
                    

    def verificaNum(self, numero): # verificar numero da conta
        try:
            for num, x in enumerate(self.contas):
                if x.verificaNumero(numero):
                    return True, num
            return False, -1
        except ValueError:
            return False
        
    def verificaCPF(self, cpf):
        try:
            for x in self.contas:
                if x.verificaCpf(cpf):
                    return True
            return False
        except ValueError:
            return False

    def verificaSENHA(self, senha):
        try:
            for x in self.contas:
                if x.verificaSenha(senha):
                    return True
            return False
        except ValueError:
            return False

    '''def verifica(self, numero):
        for x in self.contas:
            if x.numero == numero:
                return x'''

    def imprime(self):
        print(self.contas)

    def excluir(self, numero):
        cont = 0
        for x in self.contas:
            if x.numero == numero:
                self.contas.pop(cont)
                return True, 'Conta excluída! '
            cont += 1
        return False, 'Conta não encontrada! '

    def buscar(self, numero):
        for x in self.contas:
            if x.numero == numero:
                print(f'Titular da conta: {x.titular.nome}')
                print(f'Número da conta: {x.numero}')
                return x
        print('Erro, conta não encontrada! :(')