from core.dataclasses.game import Game
from core.dataclasses.licence import Licence
from core.dataclasses.revue import Revue
from core.dataclasses.user import User

import sys
import math 

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QInputDialog
)

from core.gui_compiled import Ui_Interface
import pyqtgraph as pg

# Classe GUI principale
class Window(QMainWindow, Ui_Interface):

    # Liste des couleurs dans l'ordre pour le graphique 
    colors = ["y","r","b","o","k"]

    def __init__(self, licenceManager, debug=False, parent=None):
        print("Init called")

        super().__init__(parent)
        print("Init super done")

        self.licenceManager = licenceManager
        self.activeMenu = Game
        self.debug = debug

        self.setupUi(self)
        self.graphPlot=pg.PlotWidget(title="Graphique des licences par rapport au temps", background='w')

        self.verticalLayout_5.addWidget(self.graphPlot)

        print("Init setup Ui done")
        self.connectSignalsSlots() 
        print("Connect done")
        self.reloadGenerics()

    # Connexion des boutons / menu au fonctions dans le code
    def connectSignalsSlots(self):
        self.actionClose.triggered.connect(self.close)

        self.comboBox.currentIndexChanged.connect(self.changeType)
        self.comboBox_2.currentIndexChanged.connect(self.reloadEleData)
        self.comboBox_3.currentIndexChanged.connect(self.reloadGameInfo)
        
        self.pushButton_7.clicked.connect(self.addEle)
        self.pushButton_9.clicked.connect(self.removeEle)
        self.pushButton_10.clicked.connect(self.editEle)

        self.actionCr_dits.triggered.connect(self.Credit)
        self.actionAide.triggered.connect(self.Aide)

        self.actionDate_to_int.triggered.connect(self.dateToInt)
        self.action_Int_to_date.triggered.connect(self.intToDate)
        self.actionRecharger.triggered.connect(self.reloadGenerics)
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


    # Fonction qui ouvre une fenaitre pour convertir une date en nombre en utillisant licenceManger.strToDateInt
    def dateToInt(self):
        text, ok = QInputDialog.getText(self, 'Date en nombre', 'Veuillez entrer une date (J/M/Y) :')
        if ok:
            result = self.licenceManager.strToDateInt(text)
            print("---")
            print(result)
            print("---")
            if result == False:
                QMessageBox.about(
                self,
                "Date en nombre [r??sultat]",
                "Format inconnu ?"
                )
            else:
                QMessageBox.about(
                self,
                "Date en nombre [r??sultat]",
                "Le nombre de la date est de: "+str(result)
                )

    # Fonction qui ouvre une fenaitre pour convertir un nombre en date en utillisant licenceManger.dateIntToStr
    def intToDate(self):
        text, ok = QInputDialog.getText(self, 'Nombre en date', 'Veuillez entrer un nombre :')
        if ok:
            try:
                textInt = int(text)
            except Exception as e:
                print(e)
                QMessageBox.about(self,"Nombre en date [r??sultat]","Mauvais format de nombre !")
                return

            result = self.licenceManager.dateIntToStr(textInt)
            print("---")
            print(result)
            print("---")
            QMessageBox.about(self,"Nombre en date [r??sultat]","La date est le: "+str(result))

    # Fonction qui ouvre une fenaitre pour g??n??r?? un certificat en utillisant licenceManger.generateCertificate
    def certificateCreate(self):
        text, ok = QInputDialog.getText(self, 'G??nerateur de Certificat', 'Veuillez entrer l\'ID de la licence :')
        if ok:
            result = self.licenceManager.generateCertificate(text)
            print("---")
            print(result)
            print("---")
            if result == False:
                QMessageBox.about(
                self,
                "G??nerateur de Certificat [r??sultat]",
                "Licence inconnue"
                )
            else:
                QMessageBox.about(
                self,
                "G??nerateur de Certificat [r??sultat]",
                result
                )

    # Fonction qui ouvre une fenaitre pour v??rifi?? un certificat en utillisant licenceManger.checkHashedCertificate
    def licenceCheck(self):
        text, ok = QInputDialog.getText(self, 'V??rificateur de Licence', 'Veuillez ins??rer le certificat :')
        if ok:
            print("---")
            print(text.replace("; ",";\n"))
            print("---")
            if self.licenceManager.checkHashedCertificate(text.replace("; ",";\n")):
                QMessageBox.about(
                self,
                "V??rificateur de Licence [r??sultat]",
                "La licence est valide !"
                )
            else:
                QMessageBox.about(
                self,
                "V??rificateur de Licence [r??sultat]",
                "La licence est invalide !"
                )


    # Fonction qui ouvre une fenaitre pour hasher un mot de passe en utillisant licenceManger.hashString
    def passwordHash(self):
        text, ok = QInputDialog.getText(self, 'Password Hasher', 'Veuillez ins??rer le mot de passe ?? hasher :')
        if ok:
            hashed = str(self.licenceManager.hashString(text))
            print("Hash is:",hashed)
            QMessageBox.about(
            self,
            "Password Hasher [r??sultat]",
            "Le hash est :"+hashed
            )

    
    # Fonction qui ouvre une fenaitre pour v??rifier un mot de passe en utillisant licenceManger.checkPassword
    def passwordCheck(self):
        pass_, ok = QInputDialog.getText(self, 'Password Checker', 'Veuillez ins??rer le mot de passe ?? v??rifier :')
        if not ok: return
        username, ok = QInputDialog.getText(self, 'Password Checker', 'Veuillez ins??rer le nom d\'utilisateur ?? v??rifier :')
        if not ok: return
        ret = self.licenceManager.checkPassword(username,pass_)
        if ret == True:
            QMessageBox.about(
            self,
            "Password Checker [r??sultat]",
            "Le mot de passe est correct !"
            )
        elif ret == False:
            QMessageBox.about(
            self,
            "Password Checker [r??sultat]",
            "Le mot de passe est incorrect !"
            )
        else:
            QMessageBox.about(
            self,
            "Password Checker [r??sultat]",
            "L'utillisateur est inconnu !"
            )
    
    # Fonction qui recharge les donn??es du graphique
    def reloadGenerics(self):
        infoGeneric = self.licenceManager.getStats() # On r??cup??re les donn??es
        print(infoGeneric)

        self.nbLicences.setText(str(infoGeneric["info_down"]["nbLicences"]))
        self.nbPrets.setText(str(infoGeneric["info_down"]["nbPrets"]))
        self.NBlicencesAct.setText(str(infoGeneric["info_down"]["NBlicencesAct"]))
        self.nblicenceActPretees.setText(str(infoGeneric["info_down"]["nblicenceActPretees"]))

        self.graphPlot.clear()
        self.graphPlot.setXRange(infoGeneric["graph_min_x"], infoGeneric["graph_max_x"], padding=0)
        self.graphPlot.addLegend()

        counter = 0
        for k,v in infoGeneric["graph"].items():

            pen = pg.mkPen(self.colors[counter], width=3)
            # self.graphPlot.addLegend(offset=(30, counter*30), )
            counter += 1

            AbsX = [x[0] for x in v]
            AbsY = [y[1] for y in v]
            print(AbsX,AbsY)
            self.graphPlot.plot(AbsX, AbsY, pen=pen, name=k)
        if self.debug:
            print(self.licenceManager.users)
            print(self.licenceManager.games)
            print(self.licenceManager.licences)
            print(self.licenceManager.revues)
        self.changeType()


    # Fonction qui ajoute un ??l??ment ?? la base de donn??e
    def addEle(self):
        try:
            self.licenceManager.add(self.activeMenu,self.textEdit.toPlainText().split("\n"))
            self.reloadElesList()
        except Exception as e:
            print("ERROR:",e)

    # Fonction qui modifie un ??l??ment ?? la base de donn??e
    def editEle(self):
        try:
            self.licenceManager.edit(self.activeMenu,self.textEdit.toPlainText().split("\n"))
            self.reloadElesList()
        except Exception as e:
            print("ERROR:",e)
        
    # Fonction qui retire un ??l??ment ?? la base de donn??e
    def removeEle(self):
        try:
            self.licenceManager.remove(self.activeMenu,self.comboBox_2.currentText())
            self.reloadElesList()
        except Exception as e:
            print("ERROR:",e)
        
    # Fonction pour recharger la table active dans e cas d'ajout / modofication de mes donn??es
    def changeType(self):
        wanted = self.comboBox.currentText()
        if wanted == "Jeux": self.activeMenu = Game
        elif wanted == "Utillisateurs": self.activeMenu = User
        elif wanted == "Licences": self.activeMenu = Licence
        elif wanted == "Revues": self.activeMenu = Revue
        self.reloadElesList()

    # Fonction qui recharge la liste des ??l??ments selon la table selectionn??e
    def reloadElesList(self):
        
        self.comboBox_2.clear()
        if self.activeMenu == Game:
            self.comboBox_2.addItems([x.name for x in self.licenceManager.games])
            self.comboBox_3.clear() # On reset aussi la liste des jeux pour les statistiques
            self.comboBox_3.addItems([x.name for x in self.licenceManager.games])
            self.reloadGameInfo()
        elif self.activeMenu == User:
            self.comboBox_2.addItems([x.name for x in self.licenceManager.users])
        elif self.activeMenu == Licence:
            self.comboBox_2.addItems([str(x.id) for x in self.licenceManager.licences])
            self.reloadGenerics() # rechargement du graphique
        elif self.activeMenu == Revue:
            self.comboBox_2.addItems([str(x.id) for x in self.licenceManager.revues])
            
    # Fonction qui recharge les statistiques sur les revues
    def reloadGameInfo(self):
        name = self.comboBox_3.currentText()
        if name == "":
            self.reducRecom.setText("Unknow Game")
            self.revuesMoy.setText("Unknow Game")
            self.revuesNb.setText("Unknow Game")
            return
            
        print(name, [x.name for x in self.licenceManager.games])
        price = [x for x in self.licenceManager.games if x.name == name][0].prix

        total = 0
        nbRev = 0
        for rev in self.licenceManager.revues:
            if rev.jeu == name:
                total += rev.note
                nbRev += 1

        self.revuesNb.setText(str(nbRev))
        if total <= 2:
            self.reducRecom.setText("?? ???")
            self.revuesMoy.setText("?? %")
        else:
            # Prix recommend?? :
            # 10/20 => 2.5???
            # 12/20 => 5???
            # 14/20 => 10???
            # 16/20 => 20???
            # 18/20 => 40???
            # Soit 80 * 2**(-10+notePourcent*10))
            priceGoal = math.floor(80 * 2**(-10+total/(nbRev*2)) )
            print(priceGoal)
            self.reducRecom.setText(str(round(price-priceGoal,2))+" ???")
            self.revuesMoy.setText(str(5*total/nbRev)+" %")
        
    
    # Fonction qui recharge les donn??es d'un ??lement selon la table et l'??l??ment selectionn??
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
        
    # Affichage d'une fen??tre de cr??dits
    def Credit(self):
        QMessageBox.about(
            self,
            "Cr??dits LicenceDistributeur",
            "<p>R??alis?? par Laetitia, Cyprien, Angelina</p>"
            "<p>Fais avec Python, Qt, SQLite</p>"
        )
    
    # Affichage d'une fen??tre d'aide
    def Aide(self):
        QMessageBox.about(
            self,
            "Aide LicenceDistributeur",
            "<p>Mot de passe de Cypooos: `Test`</p>"
            "<p>Mot de passe de Angel: `12345`</p>"
        )


# Instantation de la classe, (comment ??a fonctionne avec QT)
def setup(*arg,**kwargs):
    app = QApplication(sys.argv)
    win = Window(*arg,**kwargs)
    win.show()
    sys.exit(app.exec())


