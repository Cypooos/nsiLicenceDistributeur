class Licence:

    def __init__(self, id, date_debut, date_fin, user, jeu, hash, user_pret=None, is_recive=True) -> None:
        self.id = id
        self.date_debut = int(date_debut)
        self.date_fin = int(date_fin)
        self.user = user # Pas un int, donner directment l'objet user associé ^^
        self.game = jeu # Pareil
        self.hash = hash
        self.user_pret = user_pret
        self.is_recive = is_recive
    
    def getData(self):
        return [self.id,self.date_debut,self.date_fin,self.user,self.game,self.hash,self.user_pret,self.is_recive]
    
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

