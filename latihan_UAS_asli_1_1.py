import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QHBoxLayout,QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Gatauy")
        self.setMinimumSize(400,300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout()
        central_widget.setLayout(layout)

        self.label = QLabel("Selamat Datang di Lap PTI")
        self.button = QPushButton("Ubah Pesan")

        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.ganti_pesan)

    def ganti_pesan(self):
        self.label.setText("Semangat Praktikum Hari Ini!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())