class Corso:
    def __init__(self, codIns, nome, crediti, periodo):
        self.codIns = codIns
        self.nome = nome
        self.crediti = crediti
        self.periodo = periodo
        self.codIns: str
        self.nome: str
        self.crediti: int
        self.periodo: int

    def __str__(self):
        return f"{self.nome} ({self.codIns})"