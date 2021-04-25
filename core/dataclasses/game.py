class Game:

    def __init__(self, name, description, prix, reduction=None) -> None:
        self.name = name
        self.description = description
        self.prix = prix
        if reduction == None: reduction = 0
        self.reduction = reduction
    
    def getData(self):
        return [self.name,self.description,self.prix,self.reduction]
    