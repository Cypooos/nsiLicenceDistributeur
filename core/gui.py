
from core.dataclasses.game import Game
from core.dataclasses.licence import Licence
from core.dataclasses.revue import Revue
from core.dataclasses.user import User

import sys

from PyQt5.QtWidgets import (
    QApplication, QFileDialog , QMainWindow, QMessageBox, QInputDialog
)
from PyQt5.uic import loadUi

from core.gui_compiled import Ui_Interface
import pyqtgraph as pg

class Window(QMainWindow, Ui_Interface):
    def __init__(self, licenceManager, debug=False, parent=None):
        print("Init called")

        super().__init__(parent)
        print("Init super done")

        self.licenceManager = licenceManager
        self.activeMenu = Game
        self.debug = debug

        self.setupUi(self)
        self.graphPlot=pg.PlotWidget()
        self.verticalLayout_5.addWidget(self.graphPlot)

        print("Init setup Ui done")
        self.connectSignalsSlots()
        print("Connect done")
        self.reloadGenerics()

    def connectSignalsSlots(self):
        self.actionClose.triggered.connect(self.close)

        self.comboBox.currentIndexChanged.connect(self.changeType)
        self.comboBox_2.currentIndexChanged.connect(self.reloadEleData)
        
        self.pushButton_7.clicked.connect(self.addEle)
        self.pushButton_9.clicked.connect(self.removeEle)
        self.pushButton_10.clicked.connect(self.editEle)

        self.actionCr_dits.triggered.connect(self.Credit)
        self.actionAide.triggered.connect(self.Aide)

        self.actionPasswordHash.triggered.connect(self.passwordHash)
        self.actionPasswordCheck.triggered.connect(self.passwordCheck)
        self.actionLicenceCheck.triggered.connect(self.licenceCheck)
        self.actionCertificateCreate.triggered.connect(self.certificateCreate)
        # self.RenameBtn.clicked.connect(self.ins_rename)

        # self.actionNew_instrument.triggered.connect(self.ins_new)
        # self.actionDelete_Instrument.triggered.connect(self.ins_del)
        # self.actioncompile.triggered.connect(self.compile)
        # self.actionCompile_And_Run.triggered.connect(self.compile_run)
        # self.action_Stop.triggered.connect(self.stop_sound)

        # self.ChooseIns.currentIndexChanged.connect(self.select)

    def certificateCreate(self):
        text, ok = QInputDialog.getText(self, 'Certificate Generator', 'Please enter the id of the licence :')
        if ok:
            result = self.licenceManager.generateCertificate(text)
            print("---")
            print(result)
            print("---")
            if result == False:
                QMessageBox.about(
                self,
                "Certificate Generator [résultat]",
                "Licence inconnue"
                )
            else:
                QMessageBox.about(
                self,
                "Certificate Generator [résultat]",
                result
                )

    def licenceCheck(self):
        text, ok = QInputDialog.getText(self, 'Licence Checker', 'Veuillez insérer le certificat :')
        if ok:
            print("---")
            print(text.replace("; ",";\n"))
            print("---")
            if self.licenceManager.checkHashedCertificate(text.replace("; ",";\n")):
                QMessageBox.about(
                self,
                "Licence Checker [résultat]",
                "La licence est valide !"
                )
            else:
                QMessageBox.about(
                self,
                "Licence Checker [résultat]",
                "La licence est invalide !"
                )


    def passwordHash(self):
        text, ok = QInputDialog.getText(self, 'Password Hasher', 'Veuillez insérer le mot de passe à hasher :')
        if ok:
            hashed = str(self.licenceManager.hashString(text))
            print("Hash is:",hashed)
            QMessageBox.about(
            self,
            "Password Hasher [résultat]",
            "Le hash est :"+hashed
            )

    
    def passwordCheck(self):
        pass_, ok = QInputDialog.getText(self, 'Password Checker', 'Veuillez insérer le mot de passe à vérifier :')
        if not ok: return
        username, ok = QInputDialog.getText(self, 'Password Checker', 'Veuillez insérer le nom d\'utilisateur à vérifier :')
        if not ok: return
        ret = self.licenceManager.checkPassword(username,pass_)
        if ret == True:
            QMessageBox.about(
            self,
            "Password Checker [résultat]",
            "Le mot de passe est correct !"
            )
        elif ret == False:
            QMessageBox.about(
            self,
            "Password Checker [résultat]",
            "Le mot de passe est incorrect !"
            )
        else:
            QMessageBox.about(
            self,
            "Password Checker [résultat]",
            "L'utillisateur est inconnu !"
            )
    
    def reloadGenerics(self):
        infoGeneric = self.licenceManager.getStats()
        print(infoGeneric)

        self.nbLicences.setText(str(infoGeneric["info_down"]["nbLicences"]))
        self.nbPrets.setText(str(infoGeneric["info_down"]["nbPrets"]))
        self.NBlicencesAct.setText(str(infoGeneric["info_down"]["NBlicencesAct"]))
        self.nblicenceActPretees.setText(str(infoGeneric["info_down"]["nblicenceActPretees"]))

        self.graphPlot.setXRange(infoGeneric["graph_min_x"], infoGeneric["graph_max_x"], padding=0)
        for k,v in infoGeneric["graph"].items():
            AbsX = [x[0] for x in v]
            AbsY = [y[1] for y in v]
            print(AbsX,AbsY)
            self.graphPlot.plot(AbsX, AbsY)
        if self.debug:
            print(self.licenceManager.users)
            print(self.licenceManager.games)
            print(self.licenceManager.licences)
            print(self.licenceManager.revues)
        self.changeType()


    def addEle(self):
        try:
            self.licenceManager.add(self.activeMenu,self.textEdit.toPlainText().split("\n"))
            self.reloadElesList()
        except Exception as e:
            print("ERROR:",e)

    def editEle(self):
        try:
            self.licenceManager.edit(self.activeMenu,self.textEdit.toPlainText().split("\n"))
            self.reloadElesList()
        except Exception as e:
            print("ERROR:",e)
        
    def removeEle(self):
        try:
            self.licenceManager.remove(self.activeMenu,self.comboBox_2.currentText())
            self.reloadElesList()
        except Exception as e:
            print("ERROR:",e)
        
    def changeType(self):
        wanted = self.comboBox.currentText()
        if wanted == "Jeux": self.activeMenu = Game
        elif wanted == "Utillisateurs": self.activeMenu = User
        elif wanted == "Licences": self.activeMenu = Licence
        elif wanted == "Revues": self.activeMenu = Revue
        self.reloadElesList()

    def reloadElesList(self):
        self.comboBox_2.clear()
        if self.activeMenu == Game:
            self.comboBox_2.addItems([x.name for x in self.licenceManager.games])
        elif self.activeMenu == User:
            self.comboBox_2.addItems([x.name for x in self.licenceManager.users])
        elif self.activeMenu == Licence:
            self.comboBox_2.addItems([str(x.id) for x in self.licenceManager.licences])
        elif self.activeMenu == Revue:
            self.comboBox_2.addItems([str(x.id) for x in self.licenceManager.revues])
            
        # self.comboBox_3.clear()
        # self.comboBox_3.addItems([x.name for x in self.licenceManager.games])

    
    def reloadEleData(self):
        ele = self.comboBox_2.currentText()
        if ele == None or ele == "":return
        if self.activeMenu == Game:
            data = [x for x in self.licenceManager.games if x.name == ele][0].getData()
        elif self.activeMenu == User:
            data = [x for x in self.licenceManager.users if x.name == ele][0].getData()
        elif self.activeMenu == Licence:
            data = [x for x in self.licenceManager.licences if x.id == int(ele)][0].getData()
        elif self.activeMenu == Revue:
            data = [x for x in self.licenceManager.revues if x.id == int(ele)][0].getData()
        
        self.textEdit.setText("\n".join([str(x) for x in data]))
        

    def Credit(self):
        QMessageBox.about(
            self,
            "Crédits LicenceDistributeur",
            "<p>Réalisé par Laetitia, Cyprien, Angelina</p>"
            "<p>Fais avec Python, Qt, SQLite</p>"
            "<p>PS: Pas ouf, à ne pas utilliser</p>"
        )
    
    def Aide(self):
        QMessageBox.about(
            self,
            "Aide LicenceDistributeur",
            "<p>Mot de passe de Cypooos: `Test`</p>"
            "<p>Mot de passe de Angel: `12345`</p>"
        )


def setup(*arg,**kwargs):
    app = QApplication(sys.argv)
    win = Window(*arg,**kwargs)
    win.show()
    sys.exit(app.exec())


