class Licence:

    def __init__(self, id, date_debut, date_fin, user, jeu, hash, user_pret=None, is_recive=True) -> None:
        self.id = id
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.user = user # Pas un int, donner directment l'objet user associé ^^
        self.game = jeu # Pareil
        self.hash = hash
        self.user_pret = user_pret
        self.is_recive = is_recive
