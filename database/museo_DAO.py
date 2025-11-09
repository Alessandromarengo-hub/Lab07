from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    def get_all_musei(self) -> list[Museo]:
        """
        Restituisce una lista di oggetti Museo presenti nel database.
        """
        musei = []
        conn = ConnessioneDB.get_connection()
        if conn is None:
            print("Errore: impossibile ottenere connessione al database")
            return musei

        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, nome, tipologia FROM museo")
            risultati = cursor.fetchall()
            for row in risultati:
                museo = Museo(
                    id=row['id'],
                    nome=row['nome'],
                    tipologia=row['tipologia'])
                musei.append(museo)
        finally:
            cursor.close()
            conn.close()
        return musei
    # TODO
