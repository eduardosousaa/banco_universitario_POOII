# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaTransfere.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Transferencia(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 480)
        MainWindow.setMinimumSize(QtCore.QSize(650, 480))
        MainWindow.setMaximumSize(QtCore.QSize(650, 480))
        MainWindow.setStyleSheet("background-color: rgb(100, 61, 135);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(130, 100, 411, 331))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0, 0.4);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_transferir = QtWidgets.QPushButton(self.frame)
        self.btn_transferir.setGeometry(QtCore.QRect(170, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_transferir.setFont(font)
        self.btn_transferir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_transferir.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 255, 127);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.btn_transferir.setObjectName("btn_transferir")
        self.btn_voltar = QtWidgets.QPushButton(self.frame)
        self.btn_voltar.setGeometry(QtCore.QRect(180, 290, 75, 23))
        self.btn_voltar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 0, 0);    \n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 85, 0);\n"
"}")
        self.btn_voltar.setObjectName("btn_voltar")
        self.txt_saldo = QtWidgets.QLineEdit(self.frame)
        self.txt_saldo.setGeometry(QtCore.QRect(30, 40, 113, 20))
        self.txt_saldo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.txt_saldo.setObjectName("txt_saldo")
        self.txt_nomeSaldo = QtWidgets.QLabel(self.frame)
        self.txt_nomeSaldo.setGeometry(QtCore.QRect(30, 20, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txt_nomeSaldo.setFont(font)
        self.txt_nomeSaldo.setStyleSheet("background-color: rgba(0, 0, 0, 0.4);\n"
"color: rgb(255, 255, 255);")
        self.txt_nomeSaldo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_nomeSaldo.setObjectName("txt_nomeSaldo")
        self.txt_valorTransferencia = QtWidgets.QLineEdit(self.frame)
        self.txt_valorTransferencia.setGeometry(QtCore.QRect(90, 80, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_valorTransferencia.setFont(font)
        self.txt_valorTransferencia.setStyleSheet("color: rgb(255, 255, 255);")
        self.txt_valorTransferencia.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_valorTransferencia.setObjectName("txt_valorTransferencia")
        self.txt_contaDestino = QtWidgets.QLineEdit(self.frame)
        self.txt_contaDestino.setGeometry(QtCore.QRect(90, 130, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_contaDestino.setFont(font)
        self.txt_contaDestino.setStyleSheet("color: rgb(255, 255, 255);")
        self.txt_contaDestino.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_contaDestino.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_contaDestino.setObjectName("txt_contaDestino")
        self.txt_senha = QtWidgets.QLineEdit(self.frame)
        self.txt_senha.setGeometry(QtCore.QRect(90, 180, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet("color: rgb(255, 255, 255);")
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_senha.setObjectName("txt_senha")
        self.txt_nomeTelaTransferencia = QtWidgets.QLabel(self.centralwidget)
        self.txt_nomeTelaTransferencia.setGeometry(QtCore.QRect(220, 20, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.txt_nomeTelaTransferencia.setFont(font)
        self.txt_nomeTelaTransferencia.setStyleSheet("color: rgb(255, 85, 0);\n"
"")
        self.txt_nomeTelaTransferencia.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_nomeTelaTransferencia.setObjectName("txt_nomeTelaTransferencia")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_transferir.setText(_translate("MainWindow", "Transferir"))
        self.btn_voltar.setText(_translate("MainWindow", "Voltar"))
        self.txt_nomeSaldo.setText(_translate("MainWindow", "Saldo:"))
        self.txt_valorTransferencia.setPlaceholderText(_translate("MainWindow", "R$ Valor da transferência"))
        self.txt_contaDestino.setPlaceholderText(_translate("MainWindow", "Nº Conta de destino"))
        self.txt_senha.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.txt_nomeTelaTransferencia.setText(_translate("MainWindow", "Tela de Transferência"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Transferencia()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
