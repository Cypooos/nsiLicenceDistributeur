from core.dataclass.game import Game
from core.dataclass.licence import Licence
from core.dataclass.revue import Revue
from core.dataclass.user import User


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
    
    def getStats(self):

        returning = {}

        game_to_licences = {x:[] for x in self.games}
        for licence in self.licences:game_to_licences[licence.game].append(licence)


        returning["graph"] = {}
        for game,licences in game_to_licences.items():

            points = []
            for licence in licences:
                points.append([licence.date_debut,"+"])
                points.append([licence.date_fin,"-"])
            
            points.sort(key=lambda x:x[0])
            
            active_value = 0
            for i,point in enumerate(points):
                if point[1] == "+": active_value += 1
                if point[1] == "-": active_value -= 1
                
                points[i][1] = active_value
            

            
            returning["graph"][game.name] = [(x[0],x[1]) for x in points]
        
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
            Licence(1,100,120,self.users[0],self.games[0],"69FUEHF"),
            Licence(1,103,110,self.users[0],self.games[0],"69FUEHF"),
            Licence(1,105,115,self.users[0],self.games[0],"69FUEHF"),
            Licence(1,102,150,self.users[0],self.games[0],"69FUEHF"),
            
            Licence(1,100,120,self.users[0],self.games[1],"69FUEHF"),
            Licence(1,100,120,self.users[0],self.games[2],"69FUEHF"),
            Licence(1,100,130,self.users[0],self.games[2],"69FUEHF"),
        ]
        self.revues = []
