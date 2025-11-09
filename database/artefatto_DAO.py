from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    def get_all_epoche(self) -> list[Artefatto]:
        """
        Restituisce una lista di oggetti Museo presenti nel database.
        """
        epoche = []
        conn = ConnessioneDB.get_connection()
        if conn is None:
            print("Errore: impossibile ottenere connessione al database")
            return epoche

        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, nome, tipologia, epoca, id_museo FROM artefatto")
            risultati = cursor.fetchall()
            for row in risultati:
                epoca = Artefatto(
                    id=row['id'],
                    nome=row['nome'],
                    tipologia=row['tipologia'],
                    epoca = row["epoca"],
                    id_museo = row["id_museo"])
                epoche.append(epoca)
        finally:
            cursor.close()
            conn.close()
        return epoche


    def get_artefatti_DB(self, museo, epoca):
        lista_artefatti = []
        conn = ConnessioneDB.get_connection()
        if conn is None:
            print("Errore: impossibile ottenere connessione al database")
            return lista_artefatti

        try:
            cursor = conn.cursor(dictionary=True)
            if museo == "Museo" and epoca == "Epoca":
                query = ("SELECT * "
                         "FROM artefatto A "
                         )
                cursor.execute(query)
            elif museo == "Museo":
                query = ("SELECT * "
                         "FROM artefatto A "
                         "WHERE epoca = %s "
                         )
                cursor.execute(query, (epoca, ))
            elif epoca == "Epoca":
                query = ("SELECT * "
                         "FROM artefatto A "
                         "WHERE id_museo = "
                         "(SELECT id FROM museo WHERE nome = %s )"
                         )
                cursor.execute(query, ( museo,))
            else:
                query = ("SELECT * "
                         "FROM artefatto A "
                         "WHERE epoca = %s "
                         "AND id_museo = "
                         "(SELECT id FROM museo WHERE nome = %s )"
                         )
                cursor.execute(query, (epoca, museo,))


            risultati = cursor.fetchall()
            for row in risultati:
                epocas = Artefatto(
                    id=row['id'],
                    nome=row['nome'],
                    tipologia=row['tipologia'],
                    epoca=row["epoca"],
                    id_museo=row["id_museo"])
                lista_artefatti.append(epocas)
        finally:
            cursor.close()
            conn.close()
        return lista_artefatti

    # TODO