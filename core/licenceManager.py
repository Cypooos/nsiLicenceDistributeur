from core.dataclass.game import Game
from core.dataclass.licence import Licence
from core.dataclass.revue import Revue
from core.dataclass.user import User

from datetime import date

class LicenceManager:

    path = "./projet.db"

    def __init__(self):
        self.users = []
        self.games = []
        self.licences = []
        self.revues = []
        
        # faire la connexion à la db
        self.connexion = ...
        
        self.reload()


    def getStats(self,add_after=10):

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
                if licence.date_debut <= now+add_after:points.append([licence.date_debut,"+"])
                if licence.date_fin <= now+add_after:points.append([licence.date_fin,"-"])
            
            if points == []:continue

            points.sort(key=lambda x:x[0])
            
            active_value = 0
            for i,point in enumerate(points):
                if point[1] == "+": active_value += 1
                if point[1] == "-": active_value -= 1
                
                points[i][1] = active_value
            
            if points[0][0] <= minimum: minimum = points[0][0]
            if points[-1][0] >= maximum: maximum = points[-1][0]
            
            returning["graph"][game.name] = [(x[0],x[1]) for x in points]
        
        returning["graph_min_x"] = minimum
        returning["graph_middle"] = now
        returning["graph_max_x"] = maximum

        return returning



    def save(self):
        # en ayant la liste de jeux, revues, users et licences, retocké tout dans la base de donné - l'opposé de reload() -
        pass

    def reload(self):
        # obtenir la liste des jeux, la mettre sous une liste d'instances de Game()
        # obtenir la liste des revues, la mettre sous une liste d'instances de Revue()
        # obtenir la liste des users, la mettre sous une liste d'instances de Users()
        # obtenir la liste des licences, la mettre sous une liste d'instances de Licence()
        
        self.games = [
            Game(1,"BigBoy","A BIG GAME BOY",69,0),
            Game(2,"BigBoy2","A BIG GAME BOY 2",79,0),
            Game(3,"BigBoy3","A BIG GAME BOY 3",89,0),
            Game(5,"small boy","A small GAME BOY",19,20)
        ]
        
        self.users = [
            User("Cypooos","hashed1"),
            User("Admin","hashed2"),
            ]

        self.licences = [
            Licence(1,80,90,self.users[0],self.games[0],"69FUEHF"),
            Licence(1,83,90,self.users[0],self.games[0],"69FUEHF"),
            Licence(1,85,95,self.users[0],self.games[0],"69FUEHF"),

            # Pret de Admin d'une licence à Cypooos
            Licence(1,82,100,self.users[1],self.games[0],"69FUEHF",self.users[0],False),
            Licence(1,82,100,self.users[0],self.games[0],"69FUEHF",self.users[1]),
            
            Licence(1,80,90,self.users[0],self.games[1],"69FUEHF"),
            Licence(1,80,90,self.users[0],self.games[2],"69FUEHF"),
            Licence(1,80,90,self.users[0],self.games[2],"69FUEHF"),
        ]
        self.revues = []
