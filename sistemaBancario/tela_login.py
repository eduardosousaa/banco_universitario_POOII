# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(700, 500)
        login.setMinimumSize(QtCore.QSize(700, 500))
        login.setMaximumSize(QtCore.QSize(700, 500))
        login.setStyleSheet("background-color: rgb(100, 61, 135);")
        self.frame = QtWidgets.QFrame(login)
        self.frame.setGeometry(QtCore.QRect(150, 130, 411, 351))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0, 0.4);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txt_usuario = QtWidgets.QLineEdit(self.frame)
        self.txt_usuario.setGeometry(QtCore.QRect(80, 60, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_usuario.setFont(font)
        self.txt_usuario.setStyleSheet("color: rgb(255, 255, 255);")
        self.txt_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_usuario.setObjectName("txt_usuario")
        self.txt_senha = QtWidgets.QLineEdit(self.frame)
        self.txt_senha.setGeometry(QtCore.QRect(80, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet("color: rgb(255, 255, 255);")
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_senha.setObjectName("txt_senha")
        self.btn_entrar = QtWidgets.QPushButton(self.frame)
        self.btn_entrar.setGeometry(QtCore.QRect(170, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_entrar.setFont(font)
        self.btn_entrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(0, 0, 0);    \n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.btn_entrar.setObjectName("btn_entrar")
        self.btn_sair_2 = QtWidgets.QPushButton(self.frame)
        self.btn_sair_2.setGeometry(QtCore.QRect(320, 320, 75, 23))
        self.btn_sair_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 85, 0);\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.btn_sair_2.setObjectName("btn_sair_2")
        self.txt_ou = QtWidgets.QLabel(self.frame)
        self.txt_ou.setGeometry(QtCore.QRect(210, 220, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txt_ou.setFont(font)
        self.txt_ou.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0);")
        self.txt_ou.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_ou.setObjectName("txt_ou")
        self.btn_cadastro = QtWidgets.QPushButton(self.frame)
        self.btn_cadastro.setGeometry(QtCore.QRect(170, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_cadastro.setFont(font)
        self.btn_cadastro.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.btn_cadastro.setObjectName("btn_cadastro")
        self.txt_nomeTelaLogin = QtWidgets.QLabel(login)
        self.txt_nomeTelaLogin.setGeometry(QtCore.QRect(240, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setItalic(True)
        self.txt_nomeTelaLogin.setFont(font)
        self.txt_nomeTelaLogin.setStyleSheet("color: rgb(255, 85, 0);\n"
"")
        self.txt_nomeTelaLogin.setScaledContents(False)
        self.txt_nomeTelaLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_nomeTelaLogin.setObjectName("txt_nomeTelaLogin")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(300, 50, 131, 131))
        self.label.setObjectName("label")
        self.label.raise_()
        self.frame.raise_()
        self.txt_nomeTelaLogin.raise_()

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.txt_usuario.setPlaceholderText(_translate("login", "Usuário"))
        self.txt_senha.setPlaceholderText(_translate("login", "Senha"))
        self.btn_entrar.setText(_translate("login", "Entrar"))
        self.btn_sair_2.setText(_translate("login", "Sair"))
        self.txt_ou.setText(_translate("login", "Ou"))
        self.btn_cadastro.setText(_translate("login", "Criar cadastro"))
        self.txt_nomeTelaLogin.setText(_translate("login", "Tela de Login"))
        self.label.setText(_translate("login", "<html><head/><body><p><img src=\"C:/Users/eduar/OneDrive/Documentos/3periodo/programacao-orientada-a-objetos/poo/poo2/sistemaBancario/img/perfil.png\"/></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Tela_Login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
