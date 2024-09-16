import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Información Personal')

        # Crear etiquetas con nombre y edad
        nombre = QLabel('Juan Pérez')  # Cambia "Juan Pérez" por tu nombre completo
        edad = QLabel('25 años')  # Cambia "25 años" por tu edad

        # Crear un layout vertical y añadir las etiquetas
        layout = QVBoxLayout()
        layout.addWidget(nombre)
        layout.addWidget(edad)

        # Centrar el texto
        nombre.setAlignment(Qt.AlignCenter)
        edad.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
        self.resize(300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
