from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from random import randint

from tela_login import Tela_Login
from tela_principal import Tela_Principal
from tela_cadastro import Tela_Cadastro
from tela_saque import Tela_Saque
from tela_deposito import Tela_Deposito
from tela_transferencia import Tela_Transferencia
from tela_excluir import Tela_Excluir
from tela_historico import Tela_Historico

from banco import Banco
from cliente import Cliente
from conta import Conta, Historico

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        self.tela_login = Tela_Login()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_principal = Tela_Principal()
        self.tela_principal.setupUi(self.stack2)

        self.tela_saque = Tela_Saque()
        self.tela_saque.setupUi(self.stack3)

        self.tela_deposito = Tela_Deposito()
        self.tela_deposito.setupUi(self.stack4)

        self.tela_transferencia = Tela_Transferencia()
        self.tela_transferencia.setupUi(self.stack5)

        self.tela_excluir = Tela_Excluir()
        self.tela_excluir.setupUi(self.stack6)

        self.tela_historico = Tela_Historico()
        self.tela_historico.setupUi(self.stack7)


        self.QtStack.addWidget(self.stack0) #Tela de Login
        self.QtStack.addWidget(self.stack1) #Tela de Cadastro
        self.QtStack.addWidget(self.stack2) #Tela de Principal
        self.QtStack.addWidget(self.stack3) #Tela Saque
        self.QtStack.addWidget(self.stack4) #Tela de Deposito
        self.QtStack.addWidget(self.stack5) #Tela de Transferência
        self.QtStack.addWidget(self.stack6) #Tela de Excluir
        self.QtStack.addWidget(self.stack7) #Tela Histórico 



class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

        self.cad = Banco()
        self.tela_login.btn_entrar.clicked.connect(self.botaoLogin)
        self.tela_login.btn_cadastro.clicked.connect(self.abrirTelaCadastro)
        self.tela_login.btn_sair_2.clicked.connect(self.sair)

        self.tela_cadastro.btn_cadastrar.clicked.connect(self.botaoCadastrar)
        self.tela_cadastro.btn_sair.clicked.connect(self.botaoSair)

        self.tela_principal.btn_sacar.clicked.connect(self.abrirTelaSaque)
        self.tela_principal.btn_depositar.clicked.connect(self.abrirTelaDeposito)
        self.tela_principal.btn_transferir.clicked.connect(self.abrirTelaTransferencia)
        self.tela_principal.btn_excluirConta.clicked.connect(self.abrirTelaExcluir)
        self.tela_principal.btn_historico.clicked.connect(self.botaoVerHistorico)
        self.tela_principal.btn_sair.clicked.connect(self.abrirTelaLogin)

        self.tela_saque.btn_sacar.clicked.connect(self.botaoSacar)
        self.tela_saque.btn_voltar.clicked.connect(self.voltarTelaPrincipal)

        self.tela_deposito.btn_depositar.clicked.connect(self.botaoDepositar)
        self.tela_deposito.btn_voltar.clicked.connect(self.voltarTelaPrincipal)

        self.tela_transferencia.btn_transferir.clicked.connect(self.botaoTransferir)
        self.tela_transferencia.btn_voltar.clicked.connect(self.voltarTelaPrincipal)
        
        self.tela_excluir.btn_excluir.clicked.connect(self.botaoExcluir)
        self.tela_excluir.btn_voltar.clicked.connect(self.voltarTelaPrincipal)

        self.tela_historico.btn_voltar.clicked.connect(self.botaoVoltardaTelaHistorico)


    def botaoSair(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaLogin(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaPrincipal(self):
        self.QtStack.setCurrentIndex(2)

    def voltarTelaPrincipal(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTelaSaque(self):
        self.QtStack.setCurrentIndex(3)

    def abrirTelaDeposito(self):
        self.QtStack.setCurrentIndex(4)

    def abrirTelaTransferencia(self):
        self.QtStack.setCurrentIndex(5)

    def abrirTelaExcluir(self):
        self.QtStack.setCurrentIndex(6)

    def abrirTelaHistorico(self):
        self.QtStack.setCurrentIndex(7)


    def botaoCadastrar(self):
        usuario = self.tela_cadastro.txt_usuario.text()
        senha = self.tela_cadastro.txt_senha.text()
        nome = self.tela_cadastro.txt_nome.text()
        sobrenome = self.tela_cadastro.txt_sobrenome.text()
        cpf = self.tela_cadastro.txt_cpf.text()
        saldo = 0.00
        limite = 1000.00
        if not(usuario == '' or senha == '' or nome == '' or sobrenome == '' or cpf == ''):
            aux = self.cad.cadastrarConta(usuario, senha, nome, sobrenome, cpf, saldo, limite)
            if aux[0]:
                self.tela_cadastro.txt_usuario.setText('')
                self.tela_cadastro.txt_senha.setText('')
                self.tela_cadastro.txt_nome.setText('')
                self.tela_cadastro.txt_sobrenome.setText('')
                self.tela_cadastro.txt_cpf.setText('')
                QMessageBox.information(None, 'Banco', aux[1])
                self.botaoLogin(usuario, senha)
            else:
                self.tela_cadastro.txt_usuario.setText('')
                self.tela_cadastro.txt_senha.setText('')
                self.tela_cadastro.txt_nome.setText('')
                self.tela_cadastro.txt_sobrenome.setText('')
                self.tela_cadastro.txt_cpf.setText('')
                QMessageBox.information(None, 'Banco', aux[1])
        else:
            QMessageBox.information(None, 'Banco', 'Ops, todos os valores devem ser preenchidos :(')

    def botaoLogin(self, usuario = False, senha = False):
        if usuario == False and senha == False:
            usuario = self.tela_login.txt_usuario.text()
            senha = self.tela_login.txt_senha.text()
        aux = self.cad.verificarLogin(usuario, senha)
        #print(aux)
        if not(usuario == '' and senha == ''):
            if aux[0]:
                self.aux = aux[2]
                self.tela_login.txt_usuario.setText('')
                self.tela_login.txt_senha.setText('')
                #Limpei os dados da tela de login
                self.abrirTelaPrincipal()
                self.tela_principal.txt_nomeUsuario.setText(f'{self.cad.contas[self.aux].usuario}')
                self.tela_principal.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                self.tela_principal.txt_limite.setText(f'R$ %.2f' % self.cad.contas[self.aux].limite)
                self.tela_principal.txt_numeroConta.setText(f'{self.cad.contas[self.aux].numero}')
                self.tela_saque.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                self.tela_deposito.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                self.tela_transferencia.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                self.tela_excluir.txt_numeroConta.setText(f'{self.cad.contas[self.aux].numero}')
            else:
                self.tela_login.txt_usuario.setText('')
                self.tela_login.txt_senha.setText('')
                QMessageBox.information(None, 'Banco', aux[1])
        else:
            QMessageBox.information(None, 'Banco', 'Ops, todos os valores devem ser preenchidos :(')

    def botaoSacar(self):
        #print(f'{self.cad.contas[self.aux].saldo}')
        valor = self.tela_saque.txt_valorSaque.text()
        try:
            float(valor.replace(',', '.'))
            confere = True
        except ValueError:
            confere = False
        if confere:
            valorFloat = '%.2f' % float(valor.replace(',', '.'))
            #print(f'Valor saque: {valorFloat}')
            senha = self.tela_saque.txt_senha.text()
            if self.cad.contas[self.aux].verificaSenha(senha):
                aux = self.cad.contas[self.aux].saca(float(valorFloat))
                if aux == True:
                    self.tela_principal.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                    self.tela_saque.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                    self.tela_deposito.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                    self.tela_transferencia.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                    self.tela_saque.txt_valorSaque.setText('')
                    self.tela_saque.txt_senha.setText('')
                    QMessageBox.information(None, 'Banco', 'Saque realizado com sucesso! ')
                else:
                    self.tela_saque.txt_valorSaque.setText('')
                    self.tela_saque.txt_senha.setText('')
                    QMessageBox.information(None, 'Banco', 'Ops, erro no saque! ')
            else:
                #self.tela_saque.txt_valorSaque.setText('')
                self.tela_saque.txt_senha.setText('')
                QMessageBox.information(None, 'Banco', 'Senha inválida! ')
        else:
            self.tela_saque.txt_valorSaque.setText('')
            QMessageBox.information(None, 'Banco', 'Tente novamente!')
        #print(f'{self.cad.contas[self.aux].saldo}')
    
    def botaoDepositar(self):
        #print(f'Antes do deposito: {self.cad.contas[self.aux].saldo}')
        valor = self.tela_deposito.txt_valorDeposito.text()
        try:
            float(valor.replace(',', '.'))
            confere = True
        except ValueError:
            confere = False
        if confere:
            valorFloat = '%.2f' % float(valor.replace(',', '.'))
            #print(f'Valor deposito: {valorFloat}')
            senha = self.tela_deposito.txt_senha.text()
            if self.cad.contas[self.aux].verificaSenha(senha):
                aux = self.cad.contas[self.aux].deposita(float(valorFloat))
                if aux == True:
                    self.tela_principal.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                    self.tela_saque.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                    self.tela_deposito.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                    self.tela_transferencia.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                    self.tela_deposito.txt_valorDeposito.setText('')
                    self.tela_deposito.txt_senha.setText('')
                    QMessageBox.information(None, 'Banco', 'Deposito realizado com sucesso! ')
                else:
                    self.tela_deposito.txt_valorDeposito.setText('')
                    self.tela_deposito.txt_senha.setText('')
                    QMessageBox.information(None, 'Banco', 'Ops, erro no deposito! ')
            else:
                #self.tela_deposito.txt_valorDeposito.setText('')
                self.tela_deposito.txt_senha.setText('')
                QMessageBox.information(None, 'Banco', 'Senha inválida! ')
        else:
            self.tela_deposito.txt_valorDeposito.setText('')
            QMessageBox.information(None, 'Banco', 'Tente novamente!')
        
        #print(f'Depois do deposito: {self.cad.contas[self.aux].saldo}')

    def botaoTransferir(self):
        #print(f'{self.cad.contas[self.aux].saldo}')
        valor = self.tela_transferencia.txt_valorTransferencia.text()
        contaDestino = self.tela_transferencia.txt_contaDestino.text()
        try:
            float(valor.replace(',', '.'))
            confere = True
        except ValueError:
            confere = False
        if confere:
            valorFloat = '%.2f' % float(valor.replace(',', '.'))
            print(f'Valor transferencia: {valorFloat}')
            if contaDestino.isdigit():
                numeroContaDestino = int(contaDestino)
                senha = self.tela_transferencia.txt_senha.text()
                if self.cad.contas[self.aux].verificaSenha(senha):
                    x = self.cad.verificaNum(numeroContaDestino)
                    aux = self.cad.contas[self.aux].transfere(self.cad.contas[x[1]], float(valorFloat))
                    if aux[0]:
                        self.tela_principal.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                        self.tela_saque.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                        self.tela_deposito.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                        self.tela_transferencia.txt_saldo.setText(f'R$ %.2f' % self.cad.contas[self.aux].saldo)
                        self.tela_transferencia.txt_valorTransferencia.setText('')
                        self.tela_transferencia.txt_contaDestino.setText('')
                        self.tela_transferencia.txt_senha.setText('')
                        QMessageBox.information(None, 'Banco', 'Transferência realizada com sucesso! ')
                    else:
                        self.tela_transferencia.txt_valorTransferencia.setText('')
                        self.tela_transferencia.txt_contaDestino.setText('')
                        self.tela_transferencia.txt_senha.setText('')
                        QMessageBox.information(None, 'Banco', 'Ops, erro na transferência! ')
                else:
                    #self.tela_transferencia.txt_valorTransferencia.setText('')
                    #self.tela_transferencia.txt_contaDestino.setText('')
                    self.tela_transferencia.txt_senha.setText('')
                    QMessageBox.information(None, 'Banco', 'Senha inválida! ')
            else:
                self.tela_transferencia.txt_contaDestino.setText('')
                QMessageBox.information(None, 'Banco', 'Digite o Nº da Conta destino novamente!')
        else:
            self.tela_transferencia.txt_valorTransferencia.setText('')
            QMessageBox.information(None, 'Banco', 'Tente novamente!')
        
        #print(f'{self.cad.contas[self.aux].saldo}')

    
    def botaoExcluir(self):
        numero = self.tela_excluir.txt_numeroConta.text()
        senha = self.tela_excluir.txt_senha.text()
        confirmaSenha = self.tela_excluir.txt_senhaConfirmacao.text()
        numeroConta = int(numero)
        if senha == confirmaSenha:
            if self.cad.contas[self.aux].verificaSenha(senha):
                aux = self.cad.excluir(numeroConta)
                if aux:
                    self.tela_excluir.txt_senha.setText('')
                    self.tela_excluir.txt_senhaConfirmacao.setText('')
                    QMessageBox.information(None, 'Banco', 'Conta Excluída')
                    self.abrirTelaLogin()
                else:
                    self.tela_excluir.txt_senha.setText('')
                    self.tela_excluir.txt_senhaConfirmacao.setText('')
                    QMessageBox.information(None, 'Banco', 'Ops, algo deu errado :( ')
        else:
            self.tela_excluir.txt_senha.setText('')
            self.tela_excluir.txt_senhaConfirmacao.setText('')
            QMessageBox.information(None, 'Banco', 'Senhas incompatíveis, tente novamente! ')

    
    def botaoVerHistorico(self):
        self.abrirTelaHistorico()
        self.tela_historico.txt_historico.setText((self.cad.contas[self.aux].historico.imprime()))

    def botaoVoltardaTelaHistorico(self):
        self.tela_historico.txt_historico.setText('')
        self.abrirTelaPrincipal()

    @staticmethod
    def sair():
        sys.exit(app.exec_())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())