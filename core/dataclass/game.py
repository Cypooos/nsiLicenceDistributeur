class Game:

    def __init__(self, id, name, description, prix, reduction=0) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.prix = prix
        self.reduction = reduction