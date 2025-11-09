from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        lista_artefatti = self._artefatto_dao.get_artefatti_DB(museo, epoca)
        lista = list({artefatto.nome for artefatto in lista_artefatti})
        return lista
        # TODO

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        lista_artefatti = self._artefatto_dao.get_all_epoche()
        nomi_epoche = list({epoca.epoca for epoca in lista_artefatti})
        return nomi_epoche
        # TODO

    # --- MUSEI ---
    def get_musei(self):
        lista_musei = self._museo_dao.get_all_musei()
        nomi_musei = [museo.nome for museo in lista_musei]
        return nomi_musei

        """ Restituisce la lista di tutti i musei."""
        # TODO
