class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def __str__(self):
        return self.name

    def getData(self):
        return [self.name,self.password]