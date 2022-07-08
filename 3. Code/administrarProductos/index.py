#Modulo para administrar productos

from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    # Conexión con la base de datos
    db_name = 'database.db'

    def __init__(self, window):
        # Ventana Principal 
        self.wind = window
        self.wind.title('Agregar nuevos productos al catalogo')

        # Creando un Frame Container 
        frame = LabelFrame(self.wind, text = 'Registro de un nuevo producto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Entrada para el nombre del producto
        Label(frame, text = 'Nombre del producto: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # Entrada para el precio del producto
        Label(frame, text = 'Precio del producto: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        # Entrada para el proveedor del producto
        #Label(frame, text = 'Proveedor del producto: ').grid(row = 3, column = 0)
        #self.provider = Entry(frame)
        #self.provider.grid(row = 3, column = 1)

        # Butón Añadir Producto
        ttk.Button(frame, text = 'Añadir Producto', command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)

        # Menesaje de Salida 
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # Tabla de productos
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#1', text = 'Precio', anchor = CENTER)

        # Botones
        ttk.Button(text = 'Eliminar Producto', command = self.delete_product).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = 'Editar Producto', command = self.edit_product).grid(row = 5, column = 1, sticky = W + E)

        # Rellenar las filas
        self.get_products()

    # Función para ejecutar consultas de base de datos
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Obtener productos de la base de datos
    def get_products(self):
        # Limpia la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Obtiene los datos
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        # Rellena la tabla
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

    # Validación de las entradas del usuario
    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0 

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters =  (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Producto {} añadido satisfactoriamente'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'Se requiere el nombre y el precio del producto'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Por favor, seleccione un elemento'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'Elemento {} Eliminado Satisfactoriamente'.format(name)
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Por favor, seleccione un elemento'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Product'
        # Nombre actual
        Label(self.edit_wind, text = 'Nombre actual:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 0, column = 2)
        # Nombre nuevo
        Label(self.edit_wind, text = 'Nombre nuevo:').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        # Precio actual
        Label(self.edit_wind, text = 'Precio actual:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 2, column = 2)
        # Precio nuevo
        Label(self.edit_wind, text = 'Precio nuevo:').grid(row = 3, column = 1)
        new_price= Entry(self.edit_wind)
        new_price.grid(row = 3, column = 2)

        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W)
        self.edit_wind.mainloop()

    def edit_records(self, new_name, name, new_price, old_price):
        query = 'UPDATE product SET name = ?, price = ? WHERE name = ? AND price = ?'
        parameters = (new_name, new_price,name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Elemento {} actualizado satisfactoriamente'.format(name)
        self.get_products()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
