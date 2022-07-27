#Programa de ordenes de entrega utilizando PySimpleGUI y SQLite
#!/usr/bin/env python3

import sqlite3
import PySimpleGUI as sg
sg.theme('SystemDefault1')
    
#Definición de la interfaz gráfica con campos de texto y botón y etiquetas
layout = [
    [sg.Text('Código de orden', size=(15, 1)), sg.InputText(key='codigo')],
    [sg.Text('Cliente', size=(15, 1)), sg.InputText(key='cantidad')],
    [sg.Text('Nombre del producto', size=(15, 1)), sg.InputText(key='codigoProducto')],
    [sg.Text('Fecha de entrega', size=(15, 1)), sg.InputText(key='fecha')],
    [sg.Text('Dirección de entrega', size=(15, 1)), sg.InputText(key='direccion')],
    [sg.Button('Agregar'), sg.Button('Cancelar')]
]

#Carga de la interfaz gráfica
window = sg.Window('Ordenes de entrega', layout)

#definición de la función agregarOrden
def agregarOrden():
    #Muestra una pregunta de confirmación para agregar la orden
    confirmacion = sg.popup_yes_no('¿Desea agregar la orden?')
    #Si se presiona la opción si
    if confirmacion == 'Yes':
        #Mensaje de orden agregada
        sg.popup('Orden agregada')
        #Cerrar el programa
        exit()
    #Si se presiona la opción no
    if confirmacion == 'No':
        #Limpia los campos de texto del menú principal
        window['codigo'].update('')
        window['cantidad'].update('')
        window['codigoProducto'].update('')
        window['fecha'].update('')
        window['direccion'].update('')

#Funcion principal
def main():
    #Ciclo de ejecución de la interfaz gráfica
    while True:
        #Lee los datos de la interfaz gráfica
        event = window.read()
        #Si se presiona el botón agregar
        if event == 'Agregar':
            #Llama a la función agregarOrden
            agregarOrden()
        #Si se presiona el botón cancelar
        if event == 'Cancelar':
            #Cierra la ventana
            window.close()
            #Finaliza el programa
            exit()

#Muestrar la interfaz gráfica
while True:
    event, values = window.read()
    if event == 'Agregar':
        #Si se presiona el botón de agregar, se verifica que los campos no estén vacíos
        if values['codigo'] == '' or values['cantidad'] == '' or values['codigoProducto'] == '' or values['fecha'] == '' or values['direccion'] == '':
            sg.popup_error("Error", "Por favor, ingrese todos los datos")
        else:
            #Si los campos no están vacíos, se ejecuta la función agregarOrden
            agregarOrden()
    elif event == 'Cancelar':
        #Si se presiona el botón de cancelar, se cierra la ventana
        break
window.close()


