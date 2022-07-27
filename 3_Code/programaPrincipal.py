# Programa principal que dependiendo del botón presionado ejecuta los otro módulos del programa.

import os
import PySimpleGUI as sg
sg.theme('SystemDefault1')

# Definición de la interfaz gráfica con campos de texto y botón y etiquetas
layout = [
    # Definición de botones
    # Botón iniciar sesión como administrador
    [sg.Button('Iniciar sesión como administrador'),
     # Botón iniciar sesión como usuario
     sg.Button('Iniciar sesión como usuario')],
    # Boton administrar ordenes de entrega
    [sg.Button('Administrar ordenes de entrega')],
    # Boton administrar productos
    [sg.Button('Administrar productos')],
    # Botón salir
    [sg.Button('Salir')]
]

# Carga de la interfaz gráfica
window = sg.Window('Menu principal', layout)

# Muestra la interfaz gráfica
window.read()
#atributo de button_clicked

#Acciones de los botones, dependiendo del botón presionado se ejecuta el módulo correspondiente
while True:
    event, values = window.read()
    if event == 'Iniciar sesión como administrador':
        import os
        os.system('python inicioSesionAdmin.py')
    elif event == 'Iniciar sesión como usuario':
        import os
        os.system('python inicioSesionUser.py')
    elif event == 'Administrar ordenes de entrega':
        import os
        os.system('python ordenesEntrega.py')
    elif event == 'Administrar productos':
        import os
        os.system('python administrarProductos.py')
    elif event == 'Salir':
        break
    elif event == sg.WIN_CLOSED:
        break

# Cierra la ventana
window.close()






