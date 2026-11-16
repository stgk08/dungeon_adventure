class Karakter:
    def __init__(self, navn:str, liv:int):
        self.navn = navn
        self.liv = liv

    def hent_liv(self):
        return self.liv
    def oppdater_liv(self, endring:int):
        self.liv -= endring

hero = Karakter("Ukjent", 22)
