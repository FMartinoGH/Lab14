import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        stores = self._model._stores
        #storeDD = list(map(lambda x: ft.dropdown.Option(data=x, key=x.store_name), stores))
        storeDD = list(map(lambda x: ft.dropdown.Option(x), stores))
        self._view._ddStore.options = storeDD
        self._view.update_page()

    def handleCreaGrafo(self, e):
        self._model._graph.clear()
        print(self._view._ddStore.value)
        self._view.txt_result.controls.clear()
        if self._view._ddStore.value == None or self._view._txtIntK.value == "":
            self._view.txt_result.controls.append(ft.Text("Scegliere UNO STORE e un K."))
            self._view.update_page()
            return
        self._model.buildGraph(self._view._ddStore.value, self._view._txtIntK.value)
        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo ha {self._model.getNumNodes()} nodi e {self._model.getNumEdges()} archi"))
        self._view.update_page()

    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass
