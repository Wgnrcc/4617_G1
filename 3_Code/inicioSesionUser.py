# Programa que permite iniciar sesion como administrador a través de una interfaz gráfica

import sqlite3
from pydoc import doc
import PySimpleGUI as sg
sg.theme('SystemDefault1')
db_name = 'usuarios.db'

# Función para ejecutar consultas de base de datos


def run_query(query, parameters=()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result

# Obtner el nombre de usuario y contraseña de la base de datos


def getUsuario():
    query = 'SELECT * FROM usuarios'
    db_rows = run_query(query)
    return db_rows

# Funcion Validacion de la cedula
def validarCedula(cedula):
    #Verifica que los dos primeros dígitos de la cedula esten entre 1 y 24
    if (int(cedula[0:2]) < 1 or int(cedula[0:2]) > 24):
        #Si no están entre 1 y 24, se retorna False
        return False
    suma = 0
    for i in range(len(cedula) - 1):
        x = int(cedula[i])
        if i%2 == 0:
            x = x * 2
            if x > 9:
                x = x - 9
        suma = suma + x
    if suma%10 != 0:
        result = 10 - (suma%10)
        if int(cedula[-1]) == result:
            return True
        else:
            return False
    else:
        return True

# Función para validar el inicio de sesión usando la base de datos
def validarInicioSesion(usuario, contraseña):
    # Verifica que los campos no estén vacíos
    if (usuario == "" or contraseña == ""):
        sg.popup_ok("Error, datos incompletos",
                    "Por favor, ingrese todos los datos solicitados")
    else:
        # Obtiene los datos de la base de datos mediante la funcion getUsuario()
        db_rows = getUsuario()
        # Recorre la base de datos
        for row in db_rows:
            # Si el usuario ingresado es igual al usuario de la base de datos
            if (usuario == row[0]):
                # Si la contraseña ingresada es igual a la contraseña de la base de datos
                if (contraseña == row[1]):
                    # Si los datos son correctos, se muestra un mensaje de éxito
                    sg.popup_ok("Bienvenido", "Inicio de sesión exitoso")
                    # Se retorna True
                    return True
                else:
                    # Si los datos son incorrectos, se muestra un mensaje de error
                    sg.popup_ok("Error", "Contraseña incorrecta")
                    # Se retorna False
                    return False
        # Si el usuario no existe, se muestra un mensaje de error
        sg.popup_ok("Error", "El usuario ingresado no existe")
        # Se retorna False
        return False


def validarRegistro(usuarioNuevo, contraseñaNueva, nombre, apellido, correo, cedula, telefono):
    # Verifica que el correo electrónico sea válido (si falta @ y .com mostrar error)
    if (correo.find("@") == -1 or correo.find(".com") == -1):
        sg.popup_ok("Error", "Correo electrónico inválido")
        return False
    # Llama a la funcion validarCedula() para validar la cedula, si es incorrecta, se muestra un mensaje de error
    if (validarCedula(cedula) == False):
        sg.popup_error("Error", "Cedula incorrecta")
        return False
    # Verifica que los campos no estén vacíos
    if (usuarioNuevo == "" or contraseñaNueva == "" or nombre == "" or apellido == "" or correo == "" or cedula == "" or telefono == ""):
        # Si los datos solicitados están vacíos, se muestra un mensaje de error
        sg.popup_ok("Error, datos incompletos", "Por favor, ingrese todos los datos solicitados")
    else:
        query = 'INSERT INTO usuarios (usuario, contraseña, nombre, apellido, correo, cedula, telefono) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(
        values['usuarioNuevo'], values['contraseñaNueva'], values['nombre'], values['apellido'], values['correo'], values['cedula'], values['telefono'])
        parameters = ()
        run_query(query, parameters)
        sg.popup_ok("Éxito", "Usuario registrado")


# Definición de la interfaz gráfica con una imagen, campos de texto y botón y etiquetas
layout = [
    [sg.Image(r'logo.png', size=(100, 100), pad=(175, 0))],
    [sg.Text('Inicio de sesión y Registro', size=(25, 1), justification='center', pad=(75, 0), font=("Helvetica", 15))],
    [sg.Text('Usuario', size=(15, 1)), sg.InputText(key='usuario')],
    [sg.Text('Contraseña', size=(15, 1)), sg.InputText(key='contraseña', password_char='*')],
    [sg.Button('Iniciar sesión'), sg.Button('Cancelar'), sg.Button('Registrarse')]
]

# Carga de la interfaz gráfica
window = sg.Window('Inicio de sesión', layout)

while True:
    # Lee los datos ingresados en la interfaz gráfica
    event, values = window.read()
    # Si se presiona el botón de iniciar sesión, se ejecuta la función validarInicioSesion
    if event == 'Iniciar sesión':
        validarInicioSesion(values['usuario'], values['contraseña'])
    # Si se presiona el botón de cancelar, se cierra la ventana
    elif event == 'Cancelar':
        window.close()
        break
    # Si presiona el botón de registrarse, se abre una ventana de registro
    elif event == 'Registrarse':
        sg.popup_ok("Registro", "Por favor, ingrese los datos solicitados")
        layout = [
            [sg.Text('Usuario', size=(15, 1)),
             sg.InputText(key='usuarioNuevo')],
            [sg.Text('Contraseña', size=(15, 1)), sg.InputText(
                key='contraseñaNueva', password_char='*')],
            # ingrese su nombre y apellido
            [sg.Text('Nombre', size=(15, 1)), sg.InputText(key='nombre')],
            [sg.Text('Apellido', size=(15, 1)), sg.InputText(key='apellido')],
            # ingrese su correo electrónico
            [sg.Text('Correo electrónico', size=(15, 1)),
             sg.InputText(key='correo')],
            # Ingrese su número de cédula
            [sg.Text('Número de cédula', size=(15, 1)),
             sg.InputText(key='cedula')],
            # Ingrese su número de teléfono
            [sg.Text('Número de teléfono', size=(15, 1)),
             sg.InputText(key='telefono')],
            [sg.Button('Registrar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Registro', layout)
        while True:
            event, values = window.read()
            if event == 'Registrar':
                # Si se presiona el botón de registrar, se ejecuta la función validarRegistro
                validarRegistro(values['usuarioNuevo'], values['contraseñaNueva'], values['nombre'], values['apellido'], values['correo'], values['cedula'], values['telefono'])
                # Guarda los datos ingresados en la base de datos
            elif event == 'Cancelar':
                break
            elif event == sg.WIN_CLOSED:
                break
    # Si se presiona el botón de cancelar, se cierra la ventana
    if event == 'Cancelar':
        break
    elif event == sg.WIN_CLOSED:
        break
