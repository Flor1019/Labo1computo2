import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QWidget

class DialogoInformacion(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Ingreso de Información')

        # Crear widgets
        self.etiqueta_cedula = QLabel('Introduce tu número de cédula:')
        self.entrada_cedula = QLineEdit()
        self.etiqueta_nombre = QLabel('Introduce tu nombre completo:')
        self.entrada_nombre = QLineEdit()
        self.boton_aceptar = QPushButton('Aceptar')
        self.boton_cancelar = QPushButton('Cancelar')

        # Crear layout
        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta_cedula)
        layout.addWidget(self.entrada_cedula)
        layout.addWidget(self.etiqueta_nombre)
        layout.addWidget(self.entrada_nombre)
        layout.addWidget(self.boton_aceptar)
        layout.addWidget(self.boton_cancelar)
        self.setLayout(layout)

        # Conectar señales
        self.boton_aceptar.clicked.connect(self.aceptar)
        self.boton_cancelar.clicked.connect(self.cancelar)

    def aceptar(self):
        self.cedula = self.entrada_cedula.text()
        self.nombre = self.entrada_nombre.text()
        self.accept()

    def cancelar(self):
        self.cedula = None
        self.nombre = None
        self.reject()

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.leer_informacion()

    def leer_informacion(self):
        dialogo = DialogoInformacion(self)
        if dialogo.exec_() == QDialog.Accepted:
            cedula = dialogo.cedula
            nombre = dialogo.nombre
            if cedula and nombre:
                # Mostrar mensaje con la cédula y nombre si ambos fueron introducidos
                QMessageBox.information(self, 'Información', f'Cédula: {cedula}, Nombre: {nombre}')
            else:
                # Mostrar mensaje si no se introdujo alguna información
                QMessageBox.warning(self, 'Advertencia', 'No se introdujo toda la información')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
