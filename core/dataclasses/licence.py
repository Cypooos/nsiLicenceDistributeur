class Licence:

    def __init__(self, id, date_debut, date_fin, user, jeu, hash, user_pret=None) -> None:
        self.id = int(id)
        self.date_debut = int(date_debut)
        self.date_fin = int(date_fin)
        self.user = user # Pas un int, donner directment l'objet user associé ^^
        self.game = jeu # Nom du jeu ici
        self.hash = hash
        self.user_pret = user_pret
    
    def getData(self):
        return [self.id,self.date_debut,self.date_fin,self.user,self.game,self.hash,self.user_pret]
    
    def generateCertificate(self):
        return """Certificate for `{self.game}`;
;
user: `{self.user}`;
game: `{self.game}`;
pret: `{self.user_pret}`;
from: `{self.date_debut}`;
to  : `{self.date_fin}`;
;""".replace("{self.game}",self.game) \
    .replace("{self.user}",str(self.user)) \
    .replace("{self.user_pret}",str(self.user_pret)) \
    .replace("{self.date_debut}",str(self.date_debut)) \
    .replace("{self.date_fin}",str(self.date_fin))

