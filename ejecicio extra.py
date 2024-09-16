"""
Este programa crea una aplicación de registro de solicitantes de becas utilizando PyQt5. 
El propósito es automatizar el proceso de inscripción, pidiendo varios datos personales y académicos al solicitante.

**Componentes del programa:**

1. **Ventana principal**:
   - Se establece la ventana con un título ('Registro de Solicitantes de Beca') y dimensiones ajustadas (500x500 píxeles).
   - Un layout vertical (`QVBoxLayout`) organiza los diferentes widgets (elementos de la interfaz) de manera ordenada.

2. **Entrada de datos**:
   - El formulario contiene varios campos para que el solicitante ingrese su información:
     - **Nombre completo** y **apellido**: campos de texto (`QLineEdit`) para capturar el nombre y apellido del solicitante.
     - **Fecha de nacimiento**: un campo de texto donde se ingresa la fecha en formato 'dd/mm/yyyy'.
     - **Dirección**, **teléfono** y **correo electrónico**: campos de texto para capturar información de contacto.
     - **Nivel de estudios**: un menú desplegable (`QComboBox`) que permite seleccionar entre varias opciones como 'Secundaria', 'Técnico', etc.
     - **Carrera que desea estudiar**: otro campo de texto donde el solicitante especifica la carrera a la que desea optar.
     - **Promedio académico**: un control de número (`QSpinBox`) que permite ingresar el promedio del solicitante con un rango de 0 a 100.
     - **Razón para solicitar la beca**: un campo de texto amplio (`QTextEdit`) donde el solicitante puede escribir una justificación detallada de por qué solicita la beca.

3. **Validación de datos**:
   - Antes de enviar la solicitud, el programa verifica que los campos obligatorios (nombre, apellido, dirección, correo, etc.) no estén vacíos. 
   - Si algún campo esencial no se ha llenado, se muestra una advertencia para que el solicitante complete la información necesaria.

4. **Botón de envío**:
   - Al hacer clic en el botón 'Enviar Solicitud', se recopilan todos los datos ingresados.
   - Si todo está correcto, se muestra un mensaje de confirmación con algunos de los datos ingresados, informando que la solicitud ha sido enviada correctamente.

5. **Automatización del registro**:
   - Este formulario reemplaza los métodos manuales de inscripción, lo que facilita el proceso tanto para los solicitantes como para los administradores de la beca. 
   - Con un enfoque digital, el programa centraliza los datos de los solicitantes y agiliza el proceso de captura de información.

**Resumen del problema que resuelve:**
El programa automatiza el registro de solicitantes a becas, haciendo que el proceso sea más eficiente, rápido y menos propenso a errores que en los métodos manuales. Al hacerlo, mejora la gestión de las solicitudes y reduce la carga de trabajo.
"""




import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, 
                             QLineEdit, QPushButton, QMessageBox, QComboBox, 
                             QTextEdit, QSpinBox)

class RegistroBeca(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        # Configuración de la ventana
        self.setWindowTitle('Registro de Solicitantes de Beca')
        self.setGeometry(100, 100, 500, 500)  # Dimensiones ajustadas

        # Crear el layout principal
        layout = QVBoxLayout()

        # Etiqueta de título
        layout.addWidget(QLabel('Formulario de Registro para Beca'))

        # Nombre completo
        layout.addWidget(QLabel('Nombre completo:'))
        self.input_nombre = QLineEdit()
        layout.addWidget(self.input_nombre)

        # Apellido
        layout.addWidget(QLabel('Apellido:'))
        self.input_apellido = QLineEdit()
        layout.addWidget(self.input_apellido)

        # Fecha de nacimiento
        layout.addWidget(QLabel('Fecha de nacimiento (dd/mm/yyyy):'))
        self.input_fecha_nacimiento = QLineEdit()
        layout.addWidget(self.input_fecha_nacimiento)

        # Dirección
        layout.addWidget(QLabel('Dirección:'))
        self.input_direccion = QLineEdit()
        layout.addWidget(self.input_direccion)

        # Teléfono
        layout.addWidget(QLabel('Teléfono:'))
        self.input_telefono = QLineEdit()
        layout.addWidget(self.input_telefono)

        # Correo electrónico
        layout.addWidget(QLabel('Correo electrónico:'))
        self.input_correo = QLineEdit()
        layout.addWidget(self.input_correo)

        # Nivel de estudios
        layout.addWidget(QLabel('Nivel de estudios alcanzado:'))
        self.combo_nivel_estudios = QComboBox()
        self.combo_nivel_estudios.addItems(['Secundaria', 'Técnico', 'Universitario', 'Otro'])
        layout.addWidget(self.combo_nivel_estudios)

        # Carrera que desea estudiar
        layout.addWidget(QLabel('Carrera que desea estudiar:'))
        self.input_carrera = QLineEdit()
        layout.addWidget(self.input_carrera)

        # Promedio académico
        layout.addWidget(QLabel('Promedio académico:'))
        self.spin_promedio = QSpinBox()
        self.spin_promedio.setRange(0, 100)  # Rango para promedio de 0 a 100
        layout.addWidget(self.spin_promedio)

        # Razón para solicitar la beca
        layout.addWidget(QLabel('Razón para solicitar la beca:'))
        self.input_razon_beca = QTextEdit()
        layout.addWidget(self.input_razon_beca)

        # Botón de enviar
        self.boton_enviar = QPushButton('Enviar Solicitud')
        self.boton_enviar.clicked.connect(self.procesar_solicitud)
        layout.addWidget(self.boton_enviar)

        # Establecer el layout para la ventana
        self.setLayout(layout)

    def procesar_solicitud(self):
        # Obtener los datos ingresados
        nombre = self.input_nombre.text()
        apellido = self.input_apellido.text()
        fecha_nacimiento = self.input_fecha_nacimiento.text()
        direccion = self.input_direccion.text()
        telefono = self.input_telefono.text()
        correo = self.input_correo.text()
        nivel_estudios = self.combo_nivel_estudios.currentText()
        carrera = self.input_carrera.text()
        promedio = self.spin_promedio.value()
        razon_beca = self.input_razon_beca.toPlainText()

        # Validación básica para verificar que los campos obligatorios estén llenos
        if not nombre or not apellido or not fecha_nacimiento or not direccion or not telefono or not correo or not carrera or not razon_beca:
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos obligatorios.")
            return

        # Simular la inscripción automatizada
        QMessageBox.information(self, "Solicitud Enviada", 
                                f"Gracias {nombre} {apellido}, su solicitud ha sido enviada exitosamente.\n"
                                f"Promedio: {promedio}\n"
                                f"Carrera: {carrera}\n"
                                f"Razón para la beca: {razon_beca[:30]}...")  # Mostrar parte de la razón


# Inicialización de la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = RegistroBeca()
    ventana.show()
    sys.exit(app.exec_())
