class Game:

    def __init__(self, name, description, prix, reduction=None) -> None:
        self.name = name
        self.description = description
        self.prix = float(prix)
        if reduction == None: reduction = 0
        self.reduction = float(reduction)
    
    def getData(self):
        return [self.name,self.description,self.prix,self.reduction]
    