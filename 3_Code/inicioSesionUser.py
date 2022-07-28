#Programa que permite iniciar sesion como administrador a través de una interfaz gráfica

import PySimpleGUI as sg
sg.theme('SystemDefault1')

# Función para validar el inicio de sesión
def validarInicioSesion(usuario, contraseña):
    if (usuario == "" or contraseña == ""):
        # Si el usuario o la contraseña están vacíos, se muestra un mensaje de error
        sg.popup_error("Error", "Por favor, ingrese un usuario y contraseña")
    else:
        if (usuario == "juan23" and contraseña == "201020"):
            # Si el usuario y la contraseña son correctos, se muestra una notificación de acceso correcto
            sg.popup_ok("Éxito", "Bienvenido usuario")
        else:
            # Si el usuario o la contraseña son incorrectos, se muestra un mensaje de error
            sg.popup_error("Error", "Usuario o contraseña incorrectos")

def validarRegistro(usuarioNuevo, contraseñaNueva, nombre, apellido, correo, cedula, telefono):
    if (usuarioNuevo == "" or contraseñaNueva == "" or nombre == "" or apellido == "" or correo == "" or cedula == "" or telefono == ""):
        # Si los datos solicitados están vacíos, se muestra un mensaje de error
        sg.popup_ok("Error, datos incompletos", "Por favor, ingrese todos los datos solicitados")
    else:
        sg.popup_ok("Éxito", "Usuario registrado")
        

#Definición de la interfaz gráfica con una imagen, campos de texto y botón y etiquetas
layout = [
    #[sg.Image(r'imagenes/logo.png', size=(200, 100))],
    [sg.Text('Usuario', size=(15, 1)), sg.InputText(key='usuario')],
    [sg.Text('Contraseña', size=(15, 1)), sg.InputText(key='contraseña', password_char='*')],
    [sg.Button('Iniciar sesión'), sg.Button('Cancelar'), sg.Button('Registrarse')]
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
    #Si presiona el botón de registrarse, se abre una ventana de registro
    elif event == 'Registrarse':
        sg.popup_ok("Registro", "Por favor, ingrese los datos solicitados")
        layout = [
            [sg.Text('Usuario', size=(15, 1)), sg.InputText(key='usuarioNuevo')],
            [sg.Text('Contraseña', size=(15, 1)), sg.InputText(key='contraseñaNueva', password_char='*')],
            #ingrese su nombre y apellido
            [sg.Text('Nombre', size=(15, 1)), sg.InputText(key='nombre')],
            [sg.Text('Apellido', size=(15, 1)), sg.InputText(key='apellido')],
            #ingrese su correo electrónico
            [sg.Text('Correo electrónico', size=(15, 1)), sg.InputText(key='correo')],
            #Ingrese su número de cédula
            [sg.Text('Número de cédula', size=(15, 1)), sg.InputText(key='cedula')],
            #Ingrese su número de teléfono
            [sg.Text('Número de teléfono', size=(15, 1)), sg.InputText(key='telefono')],
            [sg.Button('Registrar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Registro', layout)
        while True:
            event, values = window.read()
            if event == 'Registrar':
                #Si se presiona el botón de registrar, se ejecuta la función validarRegistro
                validarRegistro(values['usuarioNuevo'], values['contraseñaNueva'], values['nombre'], values['apellido'], values['correo'], values['cedula'], values['telefono'])
            elif event == 'Cancelar':
                break
            elif event == sg.WIN_CLOSED:
                break
    #Si se presiona el botón de cancelar, se cierra la ventana
    if event == 'Cancelar':
        break
    elif event == sg.WIN_CLOSED:
        break

