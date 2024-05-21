import flet as ft

from UI import controller
from UI.controller import Controller


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddCorsi = None
        self.btn_hello = None
        self.list_result = None
        self.txt_container = None
        self.dlgCorso = None
        self.dlgStudente = None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        self.dlgCorso = ft.AlertDialog(title=ft.Text("Corso non inserito"))
        self.dlgStudente = ft.AlertDialog(title=ft.Text("Studente inesistente"))


        #Riga per i corsi
        self.ddCorsi = ft.Dropdown(options=[],
                                    label="Corso",
                                    width=775,
                                    hint_text="Seleziona corso")
        self._controller.popolaCorsi()

        self.btnSearchIscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handle_iscritti)
        row1 = ft.Row([self.ddCorsi, self.btnSearchIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)


        #Riga Studenti
        self.fieldMatricola= ft.TextField(label='Matricola', hint_text='Inserisci matricola')
        self.fieldNome = ft.TextField(label='Nome', read_only=True)
        self.fieldCognome = ft.TextField(label='Cognome', read_only=True)

        row2 = ft.Row([self.fieldMatricola,self.fieldNome,self.fieldCognome],alignment=ft.MainAxisAlignment.CENTER)

        #Riga bottoni
        self.btnSearchStudenti = ft.ElevatedButton(text='cerca Studente', on_click=self._controller.handleStudente)
        self.btnSearchCorsi = ft.ElevatedButton(text='cerca Corsi', on_click= self._controller.handleCorsiStudente)
        self.btnIscrivi = ft.ElevatedButton(text='iscrivi', on_click= self._controller.handleIscrivi)

        row3 = ft.Row([self.btnSearchStudenti,self.btnSearchCorsi,self.btnIscrivi],alignment=ft.MainAxisAlignment.CENTER)

        # List View where the reply is printed
        self.list_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.add(row1, row2, row3, self.list_result, self.dlgCorso,self.dlgStudente)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def open_dlgCorso(self):
        self.dlgCorso.open = True
        self.update_page()

    def open_dlgStudente(self):
        self.dlgStudente.open = True
        self.update_page()