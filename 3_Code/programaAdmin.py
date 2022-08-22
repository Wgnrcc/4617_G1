# Programa principal que dependiendo del botón presionado ejecuta los otro módulos del programa.

import os
import PySimpleGUI as sg
sg.theme('SystemDefault1')

# Definición de la interfaz gráfica con campos de texto y botón y etiquetas
layout = [
    # Definición de botones
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

#Acciones de los botones, dependiendo del botón presionado se ejecuta el módulo correspondiente
while True:
    event, values = window.read()
    if event == 'Administrar ordenes de entrega':
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






