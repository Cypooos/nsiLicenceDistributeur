import sqlite3

import hashlib

from core.dataclasses.game import Game
from core.dataclasses.licence import Licence
from core.dataclasses.revue import Revue
from core.dataclasses.user import User


from datetime import date

class LicenceManager:

    path = "./projet.db"
    SALT = "licenceManagerProject4832769195287"

    def __init__(self):
        self.users = []
        self.games = []
        self.licences = []
        self.revues = []

        # faire la connexion avec la db
        self.connexion = sqlite3.connect('projet.db')
        self.connexion.execute('PRAGMA foreign_keys = ON')
        self.reload()

    def add(self,classToAdd,data):
        if classToAdd == Game:
            self.connexion.execute("INSERT INTO Jeux VALUES (\""+'","'.join(data)+"\")")
            self.games.append(Game(*data))
        elif classToAdd == Licence:
            self.connexion.execute("INSERT INTO Licences VALUES (\""+'","'.join(data)+"\")")
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

    def remove(self,classToRemove,id):
        # id est int ou str dépendant du contexte 
        if classToRemove == Game:
            # le retirer de la base de donnée
            self.connexion.execute("DELETE FROM Jeux WHERE ID ="+str(id))
            # le retirer de la liste des jeux
            for game in self.games:
                if game.id == id:
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

        elif classToRemove == Revue:
            # la retirer de la base de donnée
            self.connexion.execute("DELETE FROM Users WHERE Nom ="+str(id))
            # la retirer de la liste des jeux
            for user in self.users:
                if user.name == id:
                    self.users.remove(user)
        else:
            raise Exception("Unknow class named '"+str(classToRemove)+"' for database")
        
        # On applique les changements
        self.connexion.commit()

    
    def edit(self,classToEdit,newdata):
        self.remove(classToEdit,newdata[0]) # quelquesoit la classe, la clé primaire est l'élément 0
        self.add(classToEdit, newdata)


    def checkHashedCertificate(self,certificate):
        # check if a license has valid hash, not if it is still valid
        data, hash = certificate.split("\nhash is ")
        trueHash = hashlib.md5((data+self.SALT).encode('utf-8')).hexdigest() 
        return hash == trueHash

    def generateCertificate(self,licence):
        data = licence.generateCertificate()
        hash = hashlib.md5((data+self.SALT).encode('utf-8')).hexdigest() 
        licence.hash = hash
        self.edit(Licence,licence.getData())

        return data +"\nhash is "+hash

    def checkPassword(self,username,password):

        # Password of Cypooos: `Test`
        # Password of Angel: `12345`

        result = hashlib.md5((password+self.SALT).encode('utf-8')).hexdigest()
        print("hashed is :",result)
        for user in self.users:
            if user.name == username:
                return user.password == result
        return False 


    def getStats(self,add_after=10):
        # nous utillisons la date du date(2021,1,1) comme synchronisation relative
        now = (date.today() - date(2021,1,1)).days

        returning = {}
        
        returning["info_down"] = {
            "Nombre de licences en total":len(self.licences),
            "Nombre de pret en total":0,
            "Nombre de licences active":0,
            "Nombre de licences active pretee":0,
        }

        game_to_licences = {x:[] for x in self.games}

        for licence in self.licences:
            game_to_licences[licence.game].append(licence)
            is_time = licence.date_debut <= now <= licence.date_fin
            is_pretee = licence.user_pret != None and not licence.is_recive
            if is_time:returning["info_down"]["Nombre de licences active"] += 1
            if is_time and is_pretee:returning["info_down"]["Nombre de licences active pretee"] += 1
            if is_pretee:returning["info_down"]["Nombre de pret en total"] += 1

                

        returning["graph"] = {}
        minimum = 99999999999
        maximum = -99999999999
        for game,licences in game_to_licences.items():


            points = []
            for licence in licences:
                points.append([licence.date_debut,"+"])
                points.append([licence.date_fin,"-"])
                if licence.date_debut <= now+add_after:points.append([licence.date_debut,"+"])
                if licence.date_fin <= now+add_after:points.append([licence.date_fin,"-"])
            
            if points == []:continue

            points.sort(key=lambda x:x[0])

            active_value = 0
            for i,point in enumerate(points):
                if point[1] == "+": active_value += 1
                if point[1] == "-": active_value -= 1

                points[i][1] = active_value



            returning["graph"][game.name] = [(x[0],x[1]) for x in points]
            
            if points[0][0] <= minimum: minimum = points[0][0]
            if points[-1][0] >= maximum: maximum = points[-1][0]
            
            returning["graph"][game.name] = [(x[0],x[1]) for x in points]
        
        returning["graph_min_x"] = minimum
        returning["graph_middle"] = now
        returning["graph_max_x"] = maximum

        return returning
 

    def reload(self):

        # obtenir la liste des jeux, la mettre sous une liste d'instances de Game()
        games = self.connexion.execute("SELECT * FROM Jeux")
        self.games = []
        for row in games:
            self.games.append(Game(*row))

        # obtenir la liste des revues, la mettre sous une liste d'instances de Revue()
        revues = self.connexion.execute("SELECT * FROM Revues")
        self.revues = []
        for row in revues:
            self.revues.append(Revue(*row))

        # obtenir la liste des users, la mettre sous une liste d'instances de Users()
        users = self.connexion.execute("SELECT * FROM Users")
        self.users = []
        for row in users:
            self.revues.append(User(*row))

        # obtenir la liste des licences, la mettre sous une liste d'instances de Licence()
        licences = self.connexion.execute("SELECT * FROM Licences")
        self.licences = []
        for row in licences:
            self.revues.append(Licence(*row))

        return



