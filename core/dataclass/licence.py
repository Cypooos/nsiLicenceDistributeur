class Licence:

    def __init__(self, id, date_debut, date_fin, user, jeu, hash, pret_by=None) -> None:
        self.id = id
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.user = user # Pas un int, donner directment l'objet user associé ^^
        self.game = jeu # Pareil
        self.hash = hash
        self.pret_by = pret_by
