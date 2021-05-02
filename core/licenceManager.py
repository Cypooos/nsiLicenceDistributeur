import sqlite3

import hashlib

from core.dataclasses.game import Game
from core.dataclasses.licence import Licence
from core.dataclasses.revue import Revue
from core.dataclasses.user import User

from datetime import date,timedelta

class LicenceManager:

    path = "./projet.db" # Table
    SALT = "licenceManagerProject4832769195287" # Clé privé
    date = (2021,1,1) # Date 0
    # nous utillisons la date du date(2021,1,1) comme "synchronisation relative"

    def __init__(self):
        self.users = []
        self.games = []
        self.licences = []
        self.revues = []

        # faire la connexion avec la db
        self.reload()

    # Ajouter une valeure, dépendant de la table et des données
    def add(self,classToAdd,data):
        if classToAdd == Game:
            self.connexion.execute("INSERT INTO Jeux VALUES (\""+'","'.join(data)+"\")")
            self.games.append(Game(*data))
        elif classToAdd == Licence:
            self.connexion.execute("INSERT INTO Licences VALUES (\""+'","'.join(data)+"\")")
            data[3] = [x for x in self.users if x.name == data[3]][0]
            self.licences.append(Licence(*data))
        elif classToAdd == Revue:
            self.connexion.execute("INSERT INTO Revues VALUES (\""+'","'.join(data)+"\")")
            self.revues.append(Revue(*data))
        elif classToAdd == User:
            self.connexion.execute("INSERT INTO Users VALUES (\""+'","'.join(data)+"\")")
            self.users.append(User(*data))
        else:
            raise Exception("Unknow class named '"+str(classToAdd)+"' for database")
        self.connexion.commit()

    # Retire une valeure, dépendant de la table et des données
    def remove(self,classToRemove,id):
        # id est int ou str dépendant du contexte 
        if classToRemove == Game:
            # le retirer de la base de donnée
            self.connexion.execute("DELETE FROM Jeux WHERE NAME =\""+str(id)+"\"")
            # le retirer de la liste des jeux
            for game in self.games:
                if game.name == id:
                    self.games.remove(game)
        
        elif classToRemove == Licence:
            # la retirer de la base de donnée
            self.connexion.execute("DELETE FROM Licences WHERE ID ="+str(id))
            # la retirer de la liste des jeux
            for licence in self.licences:
                if licence.id == id:
                    self.licences.remove(licence)
    
        elif classToRemove == Revue:
            # la retirer de la base de donnée
            self.connexion.execute("DELETE FROM Revues WHERE id ="+str(id))
            # la retirer de la liste des jeux
            for revue in self.revues:
                if revue.id == id:
                    self.revues.remove(revue)

        elif classToRemove == User:
            # la retirer de la base de donnée
            self.connexion.execute("DELETE FROM Users WHERE name = \""+str(id)+"\"")
            # la retirer de la liste des jeux
            for user in self.users:
                if user.name == id:
                    self.users.remove(user)
        else:
            raise Exception("Unknow class named '"+str(classToRemove)+"' for database")
        
        # On applique les changements
        self.connexion.commit()

    
    # Modifier une valeure
    def edit(self,classToEdit,newdata):
        self.remove(classToEdit,newdata[0]) # quelquesoit la classe, la clé primaire est l'élément 0
        self.add(classToEdit, newdata)


    # Vérifie un certificat
    def checkHashedCertificate(self,certificate):
        # check if a license has valid hash, not if it is still valid
        data, hash = certificate.split("\nhash is ")
        trueHash = hashlib.md5((data+self.SALT).encode('utf-8')).hexdigest() 
        return hash == trueHash

    # génère un certificat avec l'ID d'une licence
    def generateCertificate(self,licenceID):
        licence=[x for x in self.licences if x.id == int(licenceID)]
        if licence == []: return False
        licence = licence[0]

        data = licence.generateCertificate()
        hash = self.hashString(data)

        return data +"\nhash is "+hash

    # Fonction de cryptographie
    def hashString(self,string):
        return hashlib.md5((string+self.SALT).encode('utf-8')).hexdigest()

    # Vérifie que un utillisateur à le bon mot de passe
    def checkPassword(self,username,password):

        # Password of Cypooos: `Test`
        # Password of Angel: `12345`

        result = self.hashString(password)
        for user in self.users:
            if user.name == username:
                return user.password == result
        return None 

    # Convertie une date en nombre (split puis créé une date)
    def strToDateInt(self,_string):
        t = _string.split("/")
        if len(t) != 3: return False
        try:
            j,m,y = int(t[0]), int(t[1]), int(t[2])
            return (date(y,m,j) - date(*self.date)).days
        except Exception as e:
            print(e)
            return False
        
    # Convertie un nombre en date (prend la date 0 et ajoute x jours)
    def dateIntToStr(self,_int):
        _date = (date(*self.date) + timedelta(days=_int))

        return str(_date.day)+"/"+ str(_date.month)+"/"+ str(_date.year)
        

    # Obetention des informations pour le graphique / les statistiques
    def getStats(self,add_after=9999):
        now = (date.today() - date(*self.date)).days

        # Création du dictionnaire d'informations
        returning = {}
        
        returning["info_down"] = {
            "nbLicences":len(self.licences),
            "nbPrets":0,
            "NBlicencesAct":0,
            "nblicenceActPretees":0,
        }

        # Création du dictionnaire nom d'un jeu => liste de licences
        game_to_licences = {x.name:[] for x in self.games}

        # Obtention d'informations sur les licences + ajout au dict game_to_licences
        for licence in self.licences:
            game_to_licences[licence.game].append(licence)
            is_time = licence.date_debut <= now <= licence.date_fin
            is_pretee = licence.user_pret != None
            if is_time:returning["info_down"]["NBlicencesAct"] += 1
            if is_time and is_pretee:returning["info_down"]["nblicenceActPretees"] += 1
            if is_pretee:returning["info_down"]["nbPrets"] += 1

        
        # Création de la partie graph
        returning["graph"] = {}
        minimum = 99999999999
        maximum = -99999999999
        # POur chaque jeu, nouveau tableau
        for game,licences in game_to_licences.items():

            # Point : POur chaque licence, ajouter un + au début et un - à la fin au niveau des dates
            points = []
            for licence in licences:
                if licence.date_debut <= now+add_after:
                    points.append([licence.date_debut," "])
                    points.append([licence.date_debut,"+"])
                if licence.date_fin <= now+add_after:
                    points.append([licence.date_fin," "])
                    points.append([licence.date_fin,"-"])
            
            if points == []:continue
            print(points)

            # Trier les points par les dates
            points.sort(key=lambda x:x[0])

            # Remplacement des + par +1 de l'ancien, et - par -1 relatif à l'ancien
            active_value = 0
            for i,point in enumerate(points):
                if point[1] == "+": active_value += 1
                if point[1] == "-": active_value -= 1

                points[i][1] = active_value



            # calcul du min et max pour bien cadré le graphisme.
            if points[0][0] <= minimum: minimum = points[0][0]
            if points[-1][0] >= maximum: maximum = points[-1][0]
            
            returning["graph"][game] = [(x[0],x[1]) for x in points]
        
        returning["graph_min_x"] = minimum
        returning["graph_middle"] = now
        returning["graph_max_x"] = maximum

        return returning
 
    # Rehcargement de la base de donnée
    def reload(self):
        self.connexion = sqlite3.connect('projet.db')
        self.connexion.execute('PRAGMA foreign_keys = ON')

        # obtenir la liste des jeux, la mettre sous une liste d'instances de Game()
        games = self.connexion.execute("SELECT * FROM Jeux")
        self.games = []
        for row in games:
            self.games.append(Game(*row))

        # obtenir la liste des users, la mettre sous une liste d'instances de Users()
        users = self.connexion.execute("SELECT * FROM Users")
        self.users = []
        for row in users:
            self.users.append(User(*row))
        print("users:",self.users)

        # obtenir la liste des licences, la mettre sous une liste d'instances de Licence()
        licences = self.connexion.execute("SELECT * FROM Licences")
        self.licences = []
        for row in licences:
            row = list(row)
            row[3] = [x for x in self.users if x.name == row[3]][0]
            self.licences.append(Licence(*row))

        # obtenir la liste des revues, la mettre sous une liste d'instances de Revue()
        revues = self.connexion.execute("SELECT * FROM Revues")
        self.revues = []
        for row in revues:
            self.revues.append(Revue(*row))

        return



