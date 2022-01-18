import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

####################################################

class Janela(QWidget):
    __op=0
    __select=1
    total=0
    actual=0.0
    __LEd_valor1=[]
    __LEd_valor2=[]
    __LEd_result=[]
    __LEd_op=[]
#####################
#####################
    __Bt_select1=[]
    __Bt_select2=[]
#####################
    __Bt_Calc=[]
    __Bt_Clean=[]
#####################
    __Bt_adic=[]
    __Bt_sub=[]
    __Bt_div=[]
    __Bt_mult=[]
#####################
    __Bt_1=[]
    __Bt_10=[]
    __Bt_100=[]
    __Bt_1000=[]
    __Bt_10000=[]
    __Bt_100000=[]
####################################################
    def __init__(self,Str):
        super().__init__()
        super().setWindowTitle(Str)
        super().setGeometry(400,200,480,200)
        
        self.setAutoFillBackground(True)
        p=self.palette()
        p.setColor(self.backgroundRole(), QColor('lightgreen'))
        self.setPalette(p)
        
        self.inicialize()

    ####################################################
    ####################################################

    #FUNÇÕES DE AÇÕES DOS BOTÕES SELECT
    def action__Bt_select1(self):
        self.__select=1

    def action__Bt_select2(self):
        self.__select=2

    ####################################################
    ####################################################

    #FUNÇÕES DE AÇÕES DOS BOTÕES QUE DEFINEM OS VALORES
    def action__Bt_1(self):
        actual=0.0
        if self.__select==1:
            actual = float(self.__LEd_valor1.text())
            actual = actual + 1.0
            self.__LEd_valor1.setText("%5.0f"%actual)
        elif self.__select==2:
            actual = float(self.__LEd_valor2.text())
            actual = actual + 1.0
            self.__LEd_valor2.setText("%5.0f"%actual)
    
    def action__Bt_10(self):
        actual=0.0
        if self.__select==1:
            actual = float(self.__LEd_valor1.text())
            actual = actual + 10.0
            self.__LEd_valor1.setText("%5.0f"%actual)
        elif self.__select==2:
            actual = float(self.__LEd_valor2.text())
            actual = actual + 10.0
            self.__LEd_valor2.setText("%5.0f"%actual)
    
    def action__Bt_100(self):
        actual=0.0
        if self.__select==1:
            actual = float(self.__LEd_valor1.text())
            actual = actual + 100.0
            self.__LEd_valor1.setText("%5.0f"%actual)
        elif self.__select==2:
            actual = float(self.__LEd_valor2.text())
            actual = actual + 100.0
            self.__LEd_valor2.setText("%5.0f"%actual)
    
    def action__Bt_1000(self):
        actual=0.0
        if self.__select==1:
            actual = float(self.__LEd_valor1.text())
            actual = actual + 1000.0
            self.__LEd_valor1.setText("%5.0f"%actual)
        elif self.__select==2:
            actual = float(self.__LEd_valor2.text())
            actual = actual + 1000.0
            self.__LEd_valor2.setText("%5.0f"%actual)
    
    def action__Bt_10000(self):
        actual=0.0
        if self.__select==1:
            actual = float(self.__LEd_valor1.text())
            actual = actual + 10000.0
            self.__LEd_valor1.setText("%5.0f"%actual)
        elif self.__select==2:
            actual = float(self.__LEd_valor2.text())
            actual = actual + 10000.0
            self.__LEd_valor2.setText("%5.0f"%actual)
    
    def action__Bt_100000(self):
        actual=0.0
        if self.__select==1:
            actual = float(self.__LEd_valor1.text())
            actual = actual + 100000.0
            self.__LEd_valor1.setText("%5.0f"%actual)
        elif self.__select==2:
            actual = float(self.__LEd_valor2.text())
            actual = actual + 100000.0
            self.__LEd_valor2.setText("%5.0f"%actual)

    ####################################################
    ####################################################

    #FUNÇÕES DE AÇÕES DOS BOTÕES OPERACIONAIS
    def action__Bt_adic(self):
        self.__op = 1
        self.__LEd_op.setText('+')
    
    def action__Bt_sub(self):
        self.__op = 2
        self.__LEd_op.setText('-')
    
    def action__Bt_div(self):
        self.__op = 3
        self.__LEd_op.setText('÷')
    
    def action__Bt_mult(self):
        self.__op = 4
        self.__LEd_op.setText('×')
        
    ####################################################
    ####################################################

    def action__Bt_Calc(self,__op):
        total=0.0
        try:
            valor1 = float(self.__LEd_valor1.text())
            valor2 = float(self.__LEd_valor2.text())

            if self.__op == 1:
                total = valor1 + valor2

            elif self.__op == 2:
                total = valor1 - valor2

            elif self.__op == 3:
                total = valor1 / valor2
        
            elif self.__op ==4:
                total = valor1 * valor2
        except:
            return

        self.__LEd_result.setText("%5.1f"%total)
        
    ####################################################

    def action__Bt_Clean(self):
        self.__LEd_valor1.setText('%5.0f'%0)
        self.__LEd_valor2.setText('%5.0f'%0)
        self.__LEd_result.setText('%5.0f'%0.0)

    ####################################################

    #FUNÇÃO DE DESTRUÇÃO DA JANELA
    def closeEvent(self,event):
        self.destroy()
        sys.exit(0)

    ####################################################

    def inicialize(self):
        Grid=QGridLayout()

        p1=self.palette()
        p1.setColor(self.backgroundRole(),Qt.gray)

        ####################################################

        #CRIANDO AS LABELS
        self.__Lb_valor1=QLabel(self,text='1st VALUE')
        self.__Lb_valor2=QLabel(self,text='2nd VALUE')
        self.__Lb_op=QLabel(self,text='OPERATION')
        self.__Lb_valor1.setAlignment(QtCore.Qt.AlignCenter)
        self.__Lb_valor2.setAlignment(QtCore.Qt.AlignCenter)
        self.__Lb_op.setAlignment(QtCore.Qt.AlignCenter)
        self.__Lb_valor1.setStyleSheet('background-color : darkgray')
        self.__Lb_valor2.setStyleSheet('background-color : darkgray')
        self.__Lb_op.setStyleSheet('background-color : darkgray')

        ####################################################

        #CRIANDO OS LINE EDITS
        self.__LEd_op=QLineEdit(self)
        self.__LEd_result=QLineEdit(self)
        self.__LEd_result.setText('0.0')
        self.__LEd_valor1=QLineEdit(self)
        self.__LEd_valor1.setText("%5.0f"%0)
        self.__LEd_valor2=QLineEdit(self)
        self.__LEd_valor2.setText("%5.0f"%0)
        self.__LEd_op.setReadOnly(True)
        self.__LEd_result.setReadOnly(True)
        self.__LEd_valor1.setReadOnly(True)
        self.__LEd_valor2.setReadOnly(True)
        self.__LEd_op.setAlignment(QtCore.Qt.AlignCenter)
        self.__LEd_valor1.setAlignment(QtCore.Qt.AlignCenter)
        self.__LEd_valor2.setAlignment(QtCore.Qt.AlignCenter)

        ####################################################
        ####################################################

        #CRIANDO TODOS OS BOTOES

        self.__Bt_select1=QPushButton(self,text='SELECT')
        self.__Bt_select1.setStyleSheet('background-color : lightgray')
        self.__Bt_select1.clicked.connect(self.action__Bt_select1)

        self.__Bt_select2=QPushButton(self,text='SELECT')
        self.__Bt_select2.setStyleSheet('background-color : lightgray')
        self.__Bt_select2.clicked.connect(self.action__Bt_select2)

        self.__Bt_Calc=QPushButton(self,text='CALCULATE')
        self.__Bt_Calc.setStyleSheet('background-color : gray')
        self.__Bt_Calc.clicked.connect(self.action__Bt_Calc)

        self.__Bt_Clean=QPushButton(self,text='CLEAN')
        self.__Bt_Clean.setStyleSheet('background-color : darkred')
        self.__Bt_Clean.clicked.connect(self.action__Bt_Clean)

        ####################################################

        self.__Bt_adic=QPushButton(self,text='+')
        self.__Bt_adic.setStyleSheet('background-color : green')
        self.__Bt_adic.clicked.connect(self.action__Bt_adic)

        self.__Bt_sub=QPushButton(self,text='-')
        self.__Bt_sub.setStyleSheet('background-color : green')
        self.__Bt_sub.clicked.connect(self.action__Bt_sub)

        self.__Bt_div=QPushButton(self,text='÷')
        self.__Bt_div.setStyleSheet('background-color : green')
        self.__Bt_div.clicked.connect(self.action__Bt_div)

        self.__Bt_mult=QPushButton(self,text='×')
        self.__Bt_mult.setStyleSheet('background-color : green')
        self.__Bt_mult.clicked.connect(self.action__Bt_mult)

        ####################################################

        self.__Bt_1=QPushButton(self,text='1')
        self.__Bt_1.clicked.connect(self.action__Bt_1)

        self.__Bt_10=QPushButton(self,text='10')
        self.__Bt_10.clicked.connect(self.action__Bt_10)

        self.__Bt_100=QPushButton(self,text='100')
        self.__Bt_100.clicked.connect(self.action__Bt_100)

        self.__Bt_1000=QPushButton(self,text='1000')
        self.__Bt_1000.clicked.connect(self.action__Bt_1000)

        self.__Bt_10000=QPushButton(self,text='10000')
        self.__Bt_10000.clicked.connect(self.action__Bt_10000)

        self.__Bt_100000=QPushButton(self,text='100000')
        self.__Bt_100000.clicked.connect(self.action__Bt_100000)

        ####################################################
        ####################################################
        
        #INTEGRANDO OS LABELS
        Grid.addWidget(self.__Lb_valor1,0,1)
        Grid.addWidget(self.__Lb_valor2,0,3)
        Grid.addWidget(self.__Lb_op,0,2)

        ####################################################
        ####################################################
        
        #INTEGRANDO OS BOTOES
        Grid.addWidget(self.__Bt_1, 3, 1)
        Grid.addWidget(self.__Bt_10, 3, 2)
        Grid.addWidget(self.__Bt_100, 3, 3)
        Grid.addWidget(self.__Bt_1000, 4, 1)
        Grid.addWidget(self.__Bt_10000, 4, 2)
        Grid.addWidget(self.__Bt_100000, 4, 3)

        Grid.addWidget(self.__Bt_adic, 1, 4)
        Grid.addWidget(self.__Bt_sub, 2, 4)
        Grid.addWidget(self.__Bt_div, 3, 4)
        Grid.addWidget(self.__Bt_mult, 4, 4)

        Grid.addWidget(self.__Bt_select1, 2, 1)
        Grid.addWidget(self.__Bt_select2, 2, 3)

        Grid.addWidget(self.__Bt_Calc, 5, 1)

        Grid.addWidget(self.__Bt_Clean, 5, 4)

        ####################################################
        ####################################################

        #INTEGRANDO OS LINE EDITS
        Grid.addWidget(self.__LEd_op,1,2)
        Grid.addWidget(self.__LEd_result,5,2,1,2)
        Grid.addWidget(self.__LEd_valor1,1,1)
        Grid.addWidget(self.__LEd_valor2,1,3)
        
        ####################################################
        ####################################################

        self.setLayout(Grid)
        self.show()




