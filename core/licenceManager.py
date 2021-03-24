from core.dataclasses.game import Game
from core.dataclasses.licence import Licence
from core.dataclasses.revue import Revue
from core.dataclasses.user import User


class LicenceManager:

    path = "./projet.db"

    def __init__():
        self.users = []
        self.games = []
        self.liences = []
        self.revues = []
        
        # faire la connexion à la db
        self.connexion = ...
        
        self.reload()


    def reload(self):
        # obtenir la liste des jeux, la mettre sous une liste d'instances de Game()
        # obtenir la liste des revues, la mettre sous une liste d'instances de Revue()
        # obtenir la liste des users, la mettre sous une liste d'instances de Users()
        # obtenir la liste des licences, la mettre sous une liste d'instances de Licence()
