import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QVBoxLayout,QWidget,QComboBox,QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
    # ===== Konvigurasi Awal dan Layout =====
        # set nama dan ukuran window
        self.setWindowTitle("Gatauy")
        self.setMinimumSize(400,300)

        # set central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # set layout untuk widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

    # ===== Set Component Widget =====
        # set QLineEdit untuk memasukkan input
        self.input_awal = QLineEdit()
        self.input_awal.setPlaceholderText("Masukkan Panjang Awal di Sini!!")

        # set menu drop down pakai QComboBox
        self.pilihan_konversi = QComboBox()
        daftar_pilihan_konversi = ["Kilometer ke Mill","Mill ke Kilometer"]
        self.pilihan_konversi.addItems(daftar_pilihan_konversi)

        # set tombol konversi
        self.tombol_konversi = QPushButton("Konversi")
        
        # set label output
        self.label_output = QLabel(".......")

        # perulangan untuk meambahkan widget ke layout
        daftar_widget = [self.input_awal,self.pilihan_konversi,self.tombol_konversi,self.label_output]
        for widget in daftar_widget:
            layout.addWidget(widget)

    # ===== Connect Logika ke Widget =====
        self.tombol_konversi.clicked.connect(self.lakukan_konversi)

    # ===== Set Logika =====
    def lakukan_konversi(self):
        data_input_awal = float(self.input_awal.text())
        if self.pilihan_konversi.currentText() == "Kilometer ke Mill" and data_input_awal:
            hasil_konversi = data_input_awal * 0.621371
            self.label_output.setText(f"{data_input_awal} kilometer = {hasil_konversi} mill")
        else:
            hasil_konversi = data_input_awal / 0.621371
            self.label_output.setText(f"{data_input_awal} mill = {hasil_konversi} kilometer")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())