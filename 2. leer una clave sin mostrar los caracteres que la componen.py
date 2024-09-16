import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QWidget

class DialogoClave(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Clave Secreta')

        # Crear widgets
        self.etiqueta = QLabel('Introduce tu clave:')
        self.entrada_clave = QLineEdit()
        self.entrada_clave.setEchoMode(QLineEdit.Password)  # Ocultar los caracteres ingresados
        self.boton_aceptar = QPushButton('Aceptar')
        self.boton_cancelar = QPushButton('Cancelar')

        # Crear layout
        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta)
        layout.addWidget(self.entrada_clave)
        layout.addWidget(self.boton_aceptar)
        layout.addWidget(self.boton_cancelar)
        self.setLayout(layout)

        # Conectar señales
        self.boton_aceptar.clicked.connect(self.aceptar)
        self.boton_cancelar.clicked.connect(self.cancelar)

    def aceptar(self):
        self.clave = self.entrada_clave.text()
        self.accept()

    def cancelar(self):
        self.clave = None
        self.reject()

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.leer_clave()

    def leer_clave(self):
        dialogo = DialogoClave(self)
        if dialogo.exec_() == QDialog.Accepted:
            clave = dialogo.clave
            if clave:
                # Mostrar mensaje de éxito si la clave fue introducida
                QMessageBox.information(self, 'Éxito', 'Clave guardada correctamente')
            else:
                # Mostrar mensaje si no se introdujo ninguna clave
                QMessageBox.warning(self, 'Advertencia', 'No se introdujo ninguna clave')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
