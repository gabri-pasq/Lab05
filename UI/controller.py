import flet as ft

import UI
from UI import view
from model import model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def popolaCorsi(self):
        lista = self._model.getListaCorsi()
        for corso in lista:
            self._view.ddCorsi.options.append(ft.dropdown.Option(key=corso.codIns, text=str(corso)))

    def handle_iscritti(self, e):
        if self._view.ddCorsi.value is None:
            self._view.open_dlgCorso()
            return
        else:
            for studente in self._model.getStudentiCorso(self._view.ddCorsi.value):
                self._view.list_result.controls.append(ft.Text(str(studente)))
                self._view.update_page()
            return

    def handleStudente(self, e):
        self._view.fieldNome.value = None
        self._view.fieldCognome.value = None
        self._view.update_page()
        print(self._view.fieldMatricola.value)
        t = False
        for studente in self._model.getListaStudenti():
            if str(studente.matricola) == self._view.fieldMatricola.value:
                print('trovato')
                self._view.fieldNome.value = studente.nome
                self._view.fieldCognome.value = studente.cognome
                self._view.update_page()
                t = True
        if t == False:
            self._view.open_dlgStudente()
            return

    def handleCorsiStudente(self, e):
        self.handleStudente("")
        print('entra corsi')
        lista = self._model.getCorsidaStudente(self._view.fieldMatricola.value)
        if len(lista) == 0:
            self._view.list_result.controls.append(ft.Text('nessun Risultato'))
            self._view.update_page()
            return
        else:
            for corso in lista:
                self._view.list_result.controls.append(ft.Text(str(corso)))
                self._view.update_page()
            return

    def handleIscrivi(self,e ):
    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()
