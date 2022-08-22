#Programa que permite iniciar sesion como administrador a través de una interfaz gráfica

import PySimpleGUI as sg
import sqlite3
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
    query = 'SELECT * FROM administrador'
    db_rows = run_query(query)
    return db_rows
    
# Función para validar el inicio de sesión
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
                    sg.popup_ok("Bienvenido", "Inicio de sesión como administrador exitoso")
                    # Abre el programa principal
                    import os
                    os.system('python programaAdmin.py')
                    window.close()
                    break
        else:
            # Si los datos son incorrectos, se muestra un mensaje de error
            sg.popup_ok("Error", "Datos de ingreso incorrectos")
            # Se retorna False
            return False
        


#Definición de la interfaz gráfica con una imagen, campos de texto y botón y etiquetas
layout = [
    #[sg.Image(r'imagenes/logo.png', size=(200, 100))],
    [sg.Text('Usuario', size=(15, 1)), sg.InputText(key='usuario')],
    [sg.Text('Contraseña', size=(15, 1)), sg.InputText(key='contraseña', password_char='*')],
    [sg.Button('Iniciar sesión'), sg.Button('Cancelar')]
]

#Carga de la interfaz gráfica
window = sg.Window('Inicio de sesión', layout)

while True:
    #Lee los datos ingresados en la interfaz gráfica
    event, values = window.read()
    #Si se presiona el botón de iniciar sesión, se ejecuta la función validarInicioSesion
    if event == 'Iniciar sesión':
        validarInicioSesion(values['usuario'], values['contraseña'])
    #Si se presiona el botón de cancelar, se cierra la ventana
    elif event == 'Cancelar':
        window.close()
        break
    elif event == sg.WIN_CLOSED:
        window.close()
        break

