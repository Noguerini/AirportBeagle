from PyQt6.QtWebEngineWidgets import QWebEngineView

class MapboxWidget(QWebEngineView):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.load_mapbox()

    def load_mapbox(self):
        mapbox_html_path = "mapbox.html"

        with open(mapbox_html_path, "r", encoding="utf-8") as file: 
            mapbox_html = file.read()
        
        self.setHtml(mapbox_html)

