from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QHBoxLayout, QWidget

def ganti_pesan():
    label_pesan.setText("Semangat Praktikum Hari Ini!")
app = QApplication([])
window = QMainWindow()
window.setMinimumSize(500,400)

layout = QHBoxLayout()
center_widget = QWidget()
label_pesan = QLabel("Selamat Datang di Lap PTI")
button = QPushButton("Ubah Pesan")

layout.addWidget(label_pesan)
layout.addWidget(button)
center_widget.setLayout(layout)
window.setCentralWidget(center_widget)

button.clicked.connect(ganti_pesan)

window.show()
app.exec()
