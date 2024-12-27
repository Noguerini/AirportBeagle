import pandas as pd
from PyQt6.QtWidgets import QLineEdit, QLabel, QVBoxLayout, QWidget, QCompleter

class SearchWidget(QWidget):
    def __init__(self, csv_file, search_column, parent=None):
        super().__init__(parent)

        self.df = pd.read_csv(csv_file)
        self.search_column = search_column
        self.options = self.df[self.search_column].dropna().astype(str).unique()

        layout = QVBoxLayout()

        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText(f"Search {self.search_column}...")
        layout.addWidget(self.search_bar)

        completer = QCompleter(self.options, self)
        self.search_bar.setCompleter(completer)

        self.result_label = QLabel("Results will appear here.")
        layout.addWidget(self.result_label)

        self.search_bar.textChanged.connect(self.perform_search)

        self.setLayout(layout)

    def perform_search(self, text):
        """Airport ICAO code"""
        if text.strip():  
            matches = self.df[self.df[self.search_column].str.contains(text, case=False, na=False)]
            if not matches.empty:
                self.result_label.setText(f"Found {len(matches)} result(s):\n{matches.to_string(index=False)}")
            else:
                self.result_label.setText("No results found.")
        else:
            self.result_label.setText("Results will appear here.")
