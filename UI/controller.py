import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        self._view.txt_result.controls.clear()
        distanza = self._view.txt_distanza.value
        if distanza is None or distanza == "":
            self._view.create_alert("Inserire la distanza")
            return
        numNodi, numArchi, grafo=self._model.build_graph(distanza)
        self._view.txt_result.controls.append(ft.Text(f"Il numero di nodi è {numNodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Il numero di archi è {numArchi}"))
        for aeroP in grafo:
            for aeroA in grafo[aeroP]:
                self._view.txt_result.controls.append(ft.Text(f"La distanza media tra {aeroP} e {aeroA} è di {grafo[aeroP][aeroA]["weight"]}"))

        self._view.update_page()
