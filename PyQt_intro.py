import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from searchWidget import SearchWidget
from mapboxWidget import MapboxWidget

class MapboxApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Airport Beagle")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        self.mapbox_widget = MapboxWidget()
        layout.addWidget(self.mapbox_widget)

        self.search_widget = SearchWidget("airports.csv", "ident")
        layout.addWidget(self.search_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MapboxApp()
    main_window.show()
    sys.exit(app.exec())
