#Programa que permite iniciar sesion como administrador a través de una interfaz gráfica

import PySimpleGUI as sg
sg.theme('SystemDefault1')

# Función para validar el inicio de sesión
def validarInicioSesion(usuario, contraseña):
    if (usuario == "" or contraseña == ""):
        # Si el usuario o la contraseña están vacíos, se muestra un mensaje de error
        sg.popup_error("Error", "Por favor, ingrese un usuario y contraseña")
    else:
        if (usuario == "admin" and contraseña == "admin123"):
            # Si el usuario y la contraseña son correctos, se muestra una notificación de acceso correcto
            sg.popup_ok("Éxito", "Bienvenido administrador")
        else:
            # Si el usuario o la contraseña son incorrectos, se muestra un mensaje de error
            sg.popup_error("Error", "Usuario o contraseña incorrectos")

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

