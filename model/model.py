import database.corso_DAO
import database.studente_DAO


class Model:
    def __init__(self):
        pass

    def getListaCorsi(self):
        return database.corso_DAO.getCorsi()

    def getListaStudenti(self):
        return database.studente_DAO.getStudenti()

    def getStudentiCorso(self, codIns):
        result = []
        for studente in database.studente_DAO.getIscrizioni(codIns):
            result.append(studente)
        return result

    def getCorsidaStudente(self,matr):
        result = []
        for corso in database.studente_DAO.getCorsidaStud(matr):
            result.append(corso)
        return result

