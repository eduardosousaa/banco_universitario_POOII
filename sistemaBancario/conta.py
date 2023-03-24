import datetime
from cliente import *

class Conta():

    _total_contas = 0

    __slots__ = ['_usuario', '_senha', '_numero', '_titular', '_saldo', '_limite', '_historico', '_confere']

    def __init__(self, usuario, senha, numero, cliente, saldo = 0.00, limite = 1000.00):
        self._usuario = usuario
        self._senha = senha
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta._total_contas += 1
        self._confere = False
    
    @staticmethod
    def get_total_contas():
        return Conta._total_contas

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha
        
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self, historico):
        self._historico = historico

    @property
    def confere(self):
        return self._confere

    @confere.setter
    def confere(self, confere):
        self._confere = confere

    def verificaUsuario(self, usuario):
        if self.usuario == usuario:
            return True
        else:
            return False
    
    def verificaSenha(self, senha):
        if self.senha == senha:
            return True
        else:
            return False

    def verificaCpf(self, cpf):
        if self.titular.cpf == cpf:
            return True
        else:
            return False

    def verificaNumero(self, numero):
        if self.numero == numero:
            return True
        else:
            return False

    def deposita(self, deposito):
        if deposito > 0 and self._saldo + deposito <= self.limite:
            self.saldo += deposito
            if self.confere == False:
                self.historico.transacoes.append(f'Depósito de R${deposito} realizado com sucesso em {datetime.datetime.today()}')
            else:
                self._historico.transacoes.append(f'Transferencia recebida de R${deposito} em {datetime.datetime.today()}: ')
                self.confere = False
            return True
        else:
            self.historico.transacoes.append(f'Erro no deposito - Data: {datetime.datetime.today()}')
            return False

    def saca(self, valor):
        if self.saldo < valor or valor <= 0.01:
            if self.confere == False:
                self.historico.transacoes.append(f'Erro no saque - Data: {datetime.datetime.today()}')
            else:
                self.confere = False
            return False
        else:
            self.saldo -= valor
            if self.confere == False:
                self.historico.transacoes.append(f'Saque de R${valor} realizado com sucesso em {datetime.datetime.today()}')
            else:
                self.confere = False
            return True

    def transfere(self, destino, valor):
        self.confere = True
        retirou = self.saca(valor)
        if retirou == False:
            self.historico.transacoes.append(f'Erro na transferencia - Data: {datetime.datetime.today()}')
            return False, 'Erro na transferencia'
        else:
            destino.confere = True
            destino.deposita(valor)
            self.historico.transacoes.append(f'Transferencia de R${valor} para a conta Nº {destino.numero} realizado com sucesso em {datetime.datetime.today()}') 
            return True, 'Sucesso na transferencia' 
    

    def extrato(self):
        print(f'Titular: {self.titular.nome}\nNúmero: {self.numero}\nSaldo: {self.saldo}')
        self.historico.transacoes.append(f'Tirou extrato - Saldo: R${self.saldo} em {datetime.datetime.today()}')
        return True, f'{self.titular.nome}', f'{self.numero}', f'{self.saldo}'

class Historico():
    def __init__(self):
        self.data_abertura = datetime.datetime.now()
        self.transacoes = []

    def imprime(self):
        x = (f'Data de abertura: {self.data_abertura}\nTransações:\n')
        for t in self.transacoes:
            x += f'- {t}\n'
        return x

if __name__ == '__main__':
    conta = Conta('Usuario', 'senha', 'numero', 'cliente', 'saldo')
    print(conta.usuario)