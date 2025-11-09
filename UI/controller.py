import flet as ft
from UI.view import View
from model.model import Model
from model.museoDTO import Museo

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_musei(self):
        lista_musei = self._model.get_musei()
        for museo in lista_musei:
            self._view.museo_dropdown.options.append(ft.dropdown.Option(museo))
        self._view.update()

    def popola_epoche(self):
        lista_epoche = self._model.get_epoche()
        for epoca in lista_epoche:
            self._view.epoca_dropdown.options.append(ft.dropdown.Option(epoca))
        self._view.update()
    # TODO

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self, e):
        self._view.lista_artefatti.controls.clear()
        self._view.update()

        self.epoca_selezionata = self._view.epoca_dropdown.value
        self.museo_selezionato = self._view.museo_dropdown.value

        lista_artefatt = self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)
        for nome in lista_artefatt:
            self._view.lista_artefatti.controls.append(ft.Text(nome))
        self._view.update()

    # TODO
