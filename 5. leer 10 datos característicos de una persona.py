import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFormLayout, QMessageBox, QWidget

class DialogoDato(QDialog):
    def __init__(self, campo, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f'Ingresar {campo}')
        
        # Crear widgets
        self.etiqueta = QLabel(f'{campo}:')
        self.entrada = QLineEdit()
        self.boton_aceptar = QPushButton('Aceptar')
        self.boton_cancelar = QPushButton('Cancelar')

        # Crear layout
        layout = QFormLayout()
        layout.addRow(self.etiqueta, self.entrada)
        layout.addRow(self.boton_aceptar, self.boton_cancelar)
        self.setLayout(layout)

        # Conectar señales
        self.boton_aceptar.clicked.connect(self.aceptar)
        self.boton_cancelar.clicked.connect(self.cancelar)

    def aceptar(self):
        self.valor = self.entrada.text()
        self.accept()

    def cancelar(self):
        self.valor = None
        self.reject()

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.leer_datos_persona()

    def leer_datos_persona(self):
        datos = {}
        campos = ["Nombre", "Edad", "Género", "Altura", "Peso", "Nacionalidad", "Profesión", "Estado Civil", "Dirección", "Teléfono"]

        for campo in campos:
            dialogo = DialogoDato(campo, self)
            if dialogo.exec_() == QDialog.Accepted:
                valor = dialogo.valor
                if valor:
                    datos[campo] = valor
                else:
                    QMessageBox.warning(self, 'Advertencia', f'No se introdujo el {campo}')
                    return  # Terminar el proceso si no se ingresó toda la información
            else:
                return  # Cancelar si el diálogo se cierra

        # Mostrar la información recolectada
        for campo, valor in datos.items():
            print(f"{campo}: {valor}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
