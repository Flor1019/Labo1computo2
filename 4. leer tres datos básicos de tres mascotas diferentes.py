import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFormLayout, QMessageBox, QWidget

class DialogoMascota(QDialog):
    def __init__(self, index, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f'Mascota {index + 1}')
        
        # Crear widgets
        self.etiqueta_nombre = QLabel('Nombre de la mascota:')
        self.entrada_nombre = QLineEdit()
        self.etiqueta_edad = QLabel('Edad de la mascota:')
        self.entrada_edad = QLineEdit()
        self.etiqueta_especie = QLabel('Especie de la mascota:')
        self.entrada_especie = QLineEdit()
        self.boton_aceptar = QPushButton('Aceptar')
        self.boton_cancelar = QPushButton('Cancelar')

        # Crear layout
        layout = QFormLayout()
        layout.addRow(self.etiqueta_nombre, self.entrada_nombre)
        layout.addRow(self.etiqueta_edad, self.entrada_edad)
        layout.addRow(self.etiqueta_especie, self.entrada_especie)
        layout.addRow(self.boton_aceptar, self.boton_cancelar)
        self.setLayout(layout)

        # Conectar señales
        self.boton_aceptar.clicked.connect(self.aceptar)
        self.boton_cancelar.clicked.connect(self.cancelar)

    def aceptar(self):
        self.nombre = self.entrada_nombre.text()
        self.edad = self.entrada_edad.text()
        self.especie = self.entrada_especie.text()
        self.accept()

    def cancelar(self):
        self.nombre = None
        self.edad = None
        self.especie = None
        self.reject()

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.leer_mascotas()

    def leer_mascotas(self):
        mascotas = []
        for i in range(3):
            dialogo = DialogoMascota(i, self)
            if dialogo.exec_() == QDialog.Accepted:
                nombre = dialogo.nombre
                edad = dialogo.edad
                especie = dialogo.especie
                if nombre and edad and especie:
                    mascotas.append((nombre, edad, especie))
                else:
                    QMessageBox.warning(self, 'Advertencia', 'No se introdujo toda la información')
                    return  # Terminar el proceso si no se ingresó toda la información
            else:
                return  # Cancelar si el diálogo se cierra

        # Mostrar información de todas las mascotas
        for i, mascota in enumerate(mascotas, start=1):
            print(f"Mascota {i}: Nombre: {mascota[0]}, Edad: {mascota[1]}, Especie: {mascota[2]}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
