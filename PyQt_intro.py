import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from dotenv import load_dotenv

class MapboxApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MapboxGL with PyQt6")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        
        self.load_mapbox()

    def load_mapbox(self):
        mapbox_html = """
        <!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Display a map on a webpage</title>
<meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no">
<link href="https://api.mapbox.com/mapbox-gl-js/v3.9.1/mapbox-gl.css" rel="stylesheet">
<script src="https://api.mapbox.com/mapbox-gl-js/v3.9.1/mapbox-gl.js"></script>
<style>
body { margin: 0; padding: 0; }
#map { position: absolute; top: 0; bottom: 0; width: 100%; }
</style>
</head>
<body>
<div id="map"></div>
<script>
	mapboxgl.accessToken = '';
    const map = new mapboxgl.Map({
        container: 'map', 
        center: [-74.5, 40], 
        zoom: 9 
    });
</script>

</body>
</html>
        """
        
        self.web_view.setHtml(mapbox_html)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MapboxApp()
    main_window.show()
    sys.exit(app.exec())
