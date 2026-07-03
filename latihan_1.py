from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

app = QApplication([])
window = QMainWindow()

# Area koding

# setting window
window.setMinimumSize(400, 300)

layout = QVBoxLayout()

center_widget = QWidget()
center_widget.setLayout(layout)

button1 = QPushButton("Button 1")
button2 = QPushButton("button 2")

layout.addWidget(button1)
layout.addWidget(button2)

window.setCentralWidget(center_widget)



# akhir area koding
window.show()
app.exec()


