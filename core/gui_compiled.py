# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Interface(object):
    def setupUi(self, Interface):
        Interface.setObjectName("Interface")
        Interface.resize(1246, 579)
        self.centralwidget = QtWidgets.QWidget(Interface)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_5.addWidget(self.line_3)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.verticalLayout_12.addLayout(self.verticalLayout_5)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_12.addWidget(self.line_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_10.addWidget(self.label_9)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.nbLicences = QtWidgets.QLabel(self.centralwidget)
        self.nbLicences.setObjectName("nbLicences")
        self.verticalLayout_11.addWidget(self.nbLicences)
        self.nbPrets = QtWidgets.QLabel(self.centralwidget)
        self.nbPrets.setObjectName("nbPrets")
        self.verticalLayout_11.addWidget(self.nbPrets)
        self.NBlicencesAct = QtWidgets.QLabel(self.centralwidget)
        self.NBlicencesAct.setObjectName("NBlicencesAct")
        self.verticalLayout_11.addWidget(self.NBlicencesAct)
        self.nblicenceActPretees = QtWidgets.QLabel(self.centralwidget)
        self.nblicenceActPretees.setObjectName("nblicenceActPretees")
        self.verticalLayout_11.addWidget(self.nblicenceActPretees)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_3.addWidget(self.line_6)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_9.addWidget(self.comboBox_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.revuesNb = QtWidgets.QLabel(self.centralwidget)
        self.revuesNb.setObjectName("revuesNb")
        self.verticalLayout_8.addWidget(self.revuesNb)
        self.revuesMoy = QtWidgets.QLabel(self.centralwidget)
        self.revuesMoy.setObjectName("revuesMoy")
        self.verticalLayout_8.addWidget(self.revuesMoy)
        self.reducRecom = QtWidgets.QLabel(self.centralwidget)
        self.reducRecom.setObjectName("reducRecom")
        self.verticalLayout_8.addWidget(self.reducRecom)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_12.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        Interface.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Interface)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1246, 21))
        self.menubar.setObjectName("menubar")
        self.menuInterface = QtWidgets.QMenu(self.menubar)
        self.menuInterface.setObjectName("menuInterface")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuOutils = QtWidgets.QMenu(self.menubar)
        self.menuOutils.setObjectName("menuOutils")
        self.menu_Graphique = QtWidgets.QMenu(self.menubar)
        self.menu_Graphique.setObjectName("menu_Graphique")
        Interface.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Interface)
        self.statusbar.setObjectName("statusbar")
        Interface.setStatusBar(self.statusbar)
        self.actionOuvrir = QtWidgets.QAction(Interface)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionClose = QtWidgets.QAction(Interface)
        self.actionClose.setObjectName("actionClose")
        self.actionAide = QtWidgets.QAction(Interface)
        self.actionAide.setObjectName("actionAide")
        self.actionCr_dits = QtWidgets.QAction(Interface)
        self.actionCr_dits.setObjectName("actionCr_dits")
        self.actionPasswordHash = QtWidgets.QAction(Interface)
        self.actionPasswordHash.setObjectName("actionPasswordHash")
        self.actionLicenceCheck = QtWidgets.QAction(Interface)
        self.actionLicenceCheck.setObjectName("actionLicenceCheck")
        self.actionCertificateCreate = QtWidgets.QAction(Interface)
        self.actionCertificateCreate.setObjectName("actionCertificateCreate")
        self.actionPasswordCheck = QtWidgets.QAction(Interface)
        self.actionPasswordCheck.setObjectName("actionPasswordCheck")
        self.actionRecharger = QtWidgets.QAction(Interface)
        self.actionRecharger.setObjectName("actionRecharger")
        self.actionDate_to_int = QtWidgets.QAction(Interface)
        self.actionDate_to_int.setObjectName("actionDate_to_int")
        self.action_Int_to_date = QtWidgets.QAction(Interface)
        self.action_Int_to_date.setObjectName("action_Int_to_date")
        self.menuInterface.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAide)
        self.menuHelp.addAction(self.actionCr_dits)
        self.menuOutils.addAction(self.actionPasswordHash)
        self.menuOutils.addAction(self.actionPasswordCheck)
        self.menuOutils.addSeparator()
        self.menuOutils.addAction(self.actionLicenceCheck)
        self.menuOutils.addAction(self.actionCertificateCreate)
        self.menu_Graphique.addAction(self.actionRecharger)
        self.menu_Graphique.addAction(self.actionDate_to_int)
        self.menu_Graphique.addAction(self.action_Int_to_date)
        self.menubar.addAction(self.menuInterface.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuOutils.menuAction())
        self.menubar.addAction(self.menu_Graphique.menuAction())

        self.retranslateUi(Interface)
        QtCore.QMetaObject.connectSlotsByName(Interface)

    def retranslateUi(self, Interface):
        _translate = QtCore.QCoreApplication.translate
        Interface.setWindowTitle(_translate("Interface", "MainWindow"))
        self.label.setText(_translate("Interface", "Mangement"))
        self.comboBox.setItemText(0, _translate("Interface", "Jeux"))
        self.comboBox.setItemText(1, _translate("Interface", "Utillisateurs"))
        self.comboBox.setItemText(2, _translate("Interface", "Licences"))
        self.comboBox.setItemText(3, _translate("Interface", "Revues"))
        self.pushButton_7.setText(_translate("Interface", "Ajouter"))
        self.pushButton_9.setText(_translate("Interface", "Supprimer"))
        self.pushButton_10.setText(_translate("Interface", "Modifier"))
        self.label_2.setText(_translate("Interface", "Graphique"))
        self.label_3.setText(_translate("Interface", "Informations générales"))
        self.label_7.setText(_translate("Interface", "Nombre De licences"))
        self.label_9.setText(_translate("Interface", "Pret total"))
        self.label_11.setText(_translate("Interface", "Licences actives"))
        self.label_12.setText(_translate("Interface", "Licences actives pretées"))
        self.nbLicences.setText(_translate("Interface", "45"))
        self.nbPrets.setText(_translate("Interface", "56"))
        self.NBlicencesAct.setText(_translate("Interface", "56"))
        self.nblicenceActPretees.setText(_translate("Interface", "56"))
        self.label_5.setText(_translate("Interface", "Nombre de revues"))
        self.label_4.setText(_translate("Interface", "Moyenne des revues"))
        self.label_6.setText(_translate("Interface", "Reduction Recommendée"))
        self.revuesNb.setText(_translate("Interface", "48525"))
        self.revuesMoy.setText(_translate("Interface", "48%"))
        self.reducRecom.setText(_translate("Interface", "-10"))
        self.menuInterface.setTitle(_translate("Interface", "&Fichier"))
        self.menuHelp.setTitle(_translate("Interface", "&Aide"))
        self.menuOutils.setTitle(_translate("Interface", "&Outils"))
        self.menu_Graphique.setTitle(_translate("Interface", "&Graphique"))
        self.actionOuvrir.setText(_translate("Interface", "Ouvrir"))
        self.actionClose.setText(_translate("Interface", "Quitter"))
        self.actionAide.setText(_translate("Interface", "Aide"))
        self.actionCr_dits.setText(_translate("Interface", "Crédits"))
        self.actionPasswordHash.setText(_translate("Interface", "PasswordHash"))
        self.actionLicenceCheck.setText(_translate("Interface", "LicenceCheck"))
        self.actionCertificateCreate.setText(_translate("Interface", "&CertificateCreate"))
        self.actionPasswordCheck.setText(_translate("Interface", "PasswordCheck"))
        self.actionRecharger.setText(_translate("Interface", "&Recharger"))
        self.actionDate_to_int.setText(_translate("Interface", "&Date en nombre"))
        self.action_Int_to_date.setText(_translate("Interface", "&Nombre en date"))
