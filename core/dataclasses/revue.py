class Revue:
    def __init__(self, id, name, description, note, jeu):
        self.id = id
        self.name = name
        self.description = description
        self.note = note
        self.jeu = jeu

    def getData(self):
        return [self.id,self.name,self.description,self.note,self.jeu]