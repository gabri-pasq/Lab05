# Add whatever it is needed to interface with the DB Table studente
import model.studente
import model.corso
from database import DB_connect


def getStudenti():
    studenti = []
    cnx = DB_connect.DBConnect.get_connection()
    if cnx is None:
        print('errore connessione')
        return
    else:
        cursor = cnx.cursor(dictionary=True)
        query = '''SELECT * FROM studente'''
        cursor.execute(query)
        for i in cursor:
            studenti.append(model.studente.Studente(i['matricola'], i['cognome'], i['nome'], i['CDS']))
        cursor.close()
        cnx.close()
        return studenti


def getIscrizioni(codIns):
    iscrizioni = []
    cnx = DB_connect.DBConnect.get_connection()
    if cnx is None:
        print('errore connessione')
        return
    else:
        cursor = cnx.cursor(dictionary=True)
        query = '''SELECT * FROM iscrizione i , studente s WHERE s.matricola=i.matricola and i.codins = %s '''
        cursor.execute(query, (codIns,))
        for i in cursor:
            iscrizioni.append(model.studente.Studente(i['matricola'], i['cognome'], i['nome'], i['CDS']))
        cursor.close()
        cnx.close()
        return iscrizioni


def getCorsidaStud(matr):
    iscrizioni = []
    cnx = DB_connect.DBConnect.get_connection()
    if cnx is None:
        print('errore connessione')
        return
    else:
        cursor = cnx.cursor(dictionary=True)
        query = '''SELECT * FROM iscrizione i , corso c WHERE c.codins=i.codins and  i.matricola= %s '''
        cursor.execute(query, (int(matr),))
        for i in cursor:
            iscrizioni.append(model.corso.Corso(i['codins'], i['nome'], i['crediti'], i['pd']))
        cursor.close()
        cnx.close()
        return iscrizioni
