import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

##################################################

class Janela(QWidget):
    __Lb_TituloRegiao=None
    __Lb_TituloPeixe=None
    __Lb_TituloCamarao=None
    __Lb_TotalProd=None

    __Lb_Regiao=[]
    __LEd_Peixe=[]
    __LEd_Camarao=[]
    __LEd_TotalProd=[]

    __LEd_MaiorRegiao=None
    __Bt_Calc=None

    def __init__(self,Str='Janela'):
        super().__init__()
        super().setWindowTitle(Str)
        super().setGeometry(400,200,480,200)
        
        self.setAutoFillBackground(True)
        p=self.palette()
        p.setColor(self.backgroundRole(), QColor('orange'))
        self.setPalette(p)
        
        self.inicialize()
        
    def total_producao(self):
        try:
            n1 = len(self.__LEd_Peixe)
            for i in range(0,n1,1):
                val1=float(self.__LEd_Peixe[i].text())
                val2=float(self.__LEd_Camarao[i].text())
                total=val1+val2
                self.__LEd_TotalProd[i].setText('%4.2f' % total)
        except:
            return

    def maior_regiao(self):
        try:
            max=0
            n1=len(self.__LEd_TotalProd)
            for i in range(0,n1,1):
                val=float(self.__LEd_TotalProd[i].text())
                if max<val:
                    max=val
                    ii=i
            self.__LEd_MaiorRegiao.setText(self.__Lb_Regiao[ii].text())
        except:
            return

    def closeEvent(self, event):
        self.destroy()
        sys.exit(0)

    def action_Bt_Calc(self):
        self.total_producao()
        self.maior_regiao()

    def inicialize(self):
        Grid=QGridLayout()

        p1=self.palette()
        p1.setColor(self.backgroundRole(),Qt.yellow)

        self.__Lb_TituloRegiao=QLabel(self,text='Região')
        self.__Lb_TituloPeixe=QLabel(self,text='Peixe')
        self.__Lb_TituloCamarao=QLabel(self,text='Camarão')
        self.__Lb_TotalProd=QLabel(self,text='Total da Prod.')
        
        self.__Lb_TituloRegiao.setAlignment(Qt.AlignLeft)
        self.__Lb_TituloPeixe.setAlignment(Qt.AlignLeft)
        self.__Lb_TituloCamarao.setAlignment(Qt.AlignLeft)
        self.__Lb_TotalProd.setAlignment(Qt.AlignLeft)
        
        self.__Lb_TituloRegiao.setAutoFillBackground(True)
        self.__Lb_TituloRegiao.setPalette(p1)
        self.__Lb_TituloPeixe.setAutoFillBackground(True)
        self.__Lb_TituloPeixe.setPalette(p1)
        self.__Lb_TituloCamarao.setAutoFillBackground(True)
        self.__Lb_TituloCamarao.setPalette(p1)
        self.__Lb_TotalProd.setAutoFillBackground(True)
        self.__Lb_TotalProd.setPalette(p1)

        Regiao = ['Norte','Nordeste','Centro-Oeste','Sudeste','Sul']
        
        nl=len(Regiao)
        for i in range(0,nl,1):
            Lb=QLabel(self,text=Regiao[i])
            Lb.setAlignment(Qt.AlignLeft)
            Lb.setAutoFillBackground(True)
            Lb.setPalette(p1)
            self.__Lb_Regiao.append(Lb)
            
            LEd=QLineEdit(self,width=52)
            self.__LEd_Peixe.append(LEd)
            
            LEd=QLineEdit(self,width=52)
            self.__LEd_Camarao.append(LEd)
            
            LEd=QLineEdit(self,width=52)
            self.__LEd_TotalProd.append(LEd)
            
        self.__Bt_Calc=QPushButton(self,text='Calcular')
        self.__Bt_Calc.clicked.connect(self.action_Bt_Calc)
        
        self.__LEd_MaiorRegiao=QLineEdit(self,width=52)
        
        Grid.addWidget(self.__Lb_TituloRegiao,0,0)
        Grid.addWidget(self.__Lb_TituloPeixe,0,1)
        Grid.addWidget(self.__Lb_TituloCamarao,0,2)
        Grid.addWidget(self.__Lb_TotalProd,0,3)
        
        nl = len(self.__Lb_Regiao)
        for i in range(0,nl,1):
            Grid.addWidget(self.__Lb_Regiao[i],i+1,0)
            Grid.addWidget(self.__LEd_Peixe[i],i+1,1)
            Grid.addWidget(self.__LEd_Camarao[i],i+1,2)
            Grid.addWidget(self.__LEd_TotalProd[i],i+1,3)
        
        Grid.addWidget(self.__Bt_Calc, nl+1, 1)
        Grid.addWidget(self.__LEd_MaiorRegiao,nl+1,2)
            
        self.setLayout(Grid)
        self.show()

##################################################