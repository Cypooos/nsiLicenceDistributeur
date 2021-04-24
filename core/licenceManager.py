import sqlite3

<<<<<<< HEAD
from core.dataclasses.game import Game
from core.dataclasses.licence import Licence
from core.dataclasses.revue import Revue
from core.dataclasses.user import User


=======
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159
from datetime import date

class LicenceManager:

    path = "./projet.db"

    def __init__(self):
        self.users = []
        self.games = []
        self.licences = []
        self.revues = []

        # faire la connexion ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â  la db
        self.connexion = sqlite3.connect('projet.db')
        self.connexion.execute('PRAGMA foreign_keys = ON')
        self.reload()

<<<<<<< HEAD
<<<<<<< HEAD
    def getStats(self):
=======
=======
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159

    def getStats(self,add_after=10):

        now = (date.today() - date(2021,1,1)).days
<<<<<<< HEAD
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159
=======
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159

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
<<<<<<< HEAD
<<<<<<< HEAD
                points.append([licence.date_debut,"+"])
                points.append([licence.date_fin,"-"])
=======
=======
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159
                if licence.date_debut <= now+add_after:points.append([licence.date_debut,"+"])
                if licence.date_fin <= now+add_after:points.append([licence.date_fin,"-"])
            
            if points == []:continue
<<<<<<< HEAD
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159
=======
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159

            points.sort(key=lambda x:x[0])

            active_value = 0
            for i,point in enumerate(points):
                if point[1] == "+": active_value += 1
                if point[1] == "-": active_value -= 1

                points[i][1] = active_value
<<<<<<< HEAD
<<<<<<< HEAD



            returning["graph"][game.name] = [(x[0],x[1]) for x in points]
=======
=======
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159
            
            if points[0][0] <= minimum: minimum = points[0][0]
            if points[-1][0] >= maximum: maximum = points[-1][0]
            
            returning["graph"][game.name] = [(x[0],x[1]) for x in points]
        
        returning["graph_min_x"] = minimum
        returning["graph_middle"] = now
        returning["graph_max_x"] = maximum
<<<<<<< HEAD
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159
=======
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159

        return returning



    def save(self):
        # en ayant la liste de jeux, revues, users et licences, retockÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© tout dans la base de donnÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© - l'opposÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© de reload() -
        pass

    def reload(self):
        # obtenir la liste des jeux, la mettre sous une liste d'instances de Game()
        # obtenir la liste des revues, la mettre sous une liste d'instances de Revue()
        # obtenir la liste des users, la mettre sous une liste d'instances de Users()
        # obtenir la liste des licences, la mettre sous une liste d'instances de Licence()

        retour = []


        self.games = [
            Game(1,"Pacman","Le but du jeu est de manger les 126 pac-gommes (appelÃ©s gaufres sur la jaquette du jeu) Ã©parpillÃ©es dans les couloirs du labyrinthe, en faisant passer Pac-Man dessus.",69,0),
            Game(2,"Space Invader","L'objectif est de dÃƒÆ’Ã‚Â©truire avec le canon laser une vague ennemie, qui se compose de cinq rangÃƒÆ’Ã‚Â©es de onze aliens chacune, avant qu'elle n'atteigne le bas de l'ÃƒÆ’Ã‚Â©cran. Le joueur gagne des points ÃƒÆ’Ã‚Â  chaque fois qu'il dÃƒÆ’Ã‚Â©truit un envahisseur.",79,0),
            Game(3,"DÃƒÆ’Ã‚Â©mineur","Le DÃƒÆ’Ã‚Â©mineur (Minesweeper) est un jeu vidÃƒÆ’Ã‚Â©o de rÃƒÆ’Ã‚Â©flexion dont le but est de localiser des mines cachÃƒÆ’Ã‚Â©es dans une grille reprÃƒÆ’Ã‚Â©sentant un champ de mines virtuel, avec pour seule indication le nombre de mines dans les zones adjacentes.",89,0),
            Game(4,"Puissance 4","Le but du jeu est d'aligner une suite de 4 pions de mÃƒÆ’Ã‚Âªme couleur sur une grille comptant 6 rangÃƒÆ’Ã‚Â©es et 7 colonnes. Chaque joueur dispose de 21 pions d'une couleur (par convention, en gÃƒÆ’Ã‚Â©nÃƒÆ’Ã‚Â©ral jaune ou rouge).",19,20)
            Game(5,"Snake","Le but du jeu est de faire manger les plus de pommes (en rouge) ÃƒÆ’Ã‚Â  votre serpent pour le faire grandir. Plus il mange de pommes, plus il grandit. Mais attention ne foncez pas dans un mur et ne vous mordez pas la queue sinon c'est perdu. ÃƒÆ’Ã¢â€šÂ¬ chaque fois que le serpent attrape une pomme, votre score augmente d'un point. DÃƒÆ’Ã‚Â¨s que votre serpent entre en collision avec un bord ou avec lui-mÃƒÆ’Ã‚Âªme la partie est finie et votre score retombe ÃƒÆ’Ã‚Â  zÃƒÆ’Ã‚Â©ro. Votre meilleur score reste affichÃƒÆ’Ã‚Â© pendant votre partie. Essayez d'avoir le meilleur score possible!",19,20)
        ]

        self.users = [
            User("Cypooos","hashed1"),
            User("Admin","hashed2"),
            ]

        self.licences = [
<<<<<<< HEAD
<<<<<<< HEAD
            Licence(1,100,120,self.users[0],self.games[0],"69FUEHF"),
            Licence(1,103,110,self.users[0],self.games[0],"69FUEHF"),
            Licence(1,105,115,self.users[0],self.games[0],"69FUEHF"),
            Licence(1,102,150,self.users[0],self.games[0],"69FUEHF"),

            Licence(1,100,120,self.users[0],self.games[1],"69FUEHF"),
            Licence(1,100,120,self.users[0],self.games[2],"69FUEHF"),
            Licence(1,100,130,self.users[0],self.games[2],"69FUEHF"),
=======
=======
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159
            Licence(1,80,90,self.users[0],self.games[0],"69FUEHF"),
            Licence(1,83,90,self.users[0],self.games[0],"69FUEHF"),
            Licence(1,85,95,self.users[0],self.games[0],"69FUEHF"),

            # Pret de Admin d'une licence à Cypooos
            Licence(1,82,100,self.users[1],self.games[0],"69FUEHF",self.users[0],False),
            Licence(1,82,100,self.users[0],self.games[0],"69FUEHF",self.users[1]),
            
            Licence(1,80,90,self.users[0],self.games[1],"69FUEHF"),
            Licence(1,80,90,self.users[0],self.games[2],"69FUEHF"),
            Licence(1,80,90,self.users[0],self.games[2],"69FUEHF"),
<<<<<<< HEAD
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159
=======
>>>>>>> d2497bbdea871b9abefe74b78b0d4ff8eab65159
        ]
        self.revues = []


    self.connexion.commit()
    self.connexion.close()

