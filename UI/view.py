from cProfile import label

import flet as ft
from flet.core.types import MainAxisAlignment
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        def dropdown_changed(e):
            pass

        self.museo_dropdown = ft.Dropdown(
            options=[
                ft.dropdown.Option("Museo"),
            ],
            value="Museo",
            on_change=dropdown_changed  # callback quando cambia selezione
        )

        self.epoca_dropdown = ft.Dropdown(
            options=[
                ft.dropdown.Option("Epoca"),
            ],
            value="Epoca",
            on_change=dropdown_changed  # callback quando cambia selezione
        )

        # TODO

        # Sezione 3: Artefatti
        self.bottone_mostra = ft.ElevatedButton("Mostra artefatti", on_click=self.controller.mostra_artefatti)
        self.lista_artefatti = ft.ListView(expand=True, spacing=5, padding=10,)
        # TODO

        self.controller.popola_musei()
        self.controller.popola_epoche()


        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            ft.Row(spacing=10, controls= [self.museo_dropdown, self.epoca_dropdown]
                   , alignment= MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Artefatti
            self.bottone_mostra,
            self.lista_artefatti,
            # TODO
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
