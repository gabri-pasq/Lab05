# Add whatever it is needed to interface with the DB Table corso
import model.corso as c
from database import DB_connect


def getCorsi():
    corsi = []
    cnx = DB_connect.DBConnect.get_connection()
    if cnx is None:
        print('errore connessione')
        return
    else:
        cursor = cnx.cursor(dictionary=True)
        query = '''SELECT * FROM corso'''
        cursor.execute(query)
        for i in cursor:
            corsi.append(c.Corso(i['codins'],i['nome'] , i['crediti'], i['pd']))
        cursor.close()
        cnx.close()
        return corsi
