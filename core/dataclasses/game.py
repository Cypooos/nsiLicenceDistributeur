class Game:

    def __init__(self, id, name, description, prix, reduction=None) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.prix = prix
        if reduction == None: reduction = 0
        self.reduction = reduction