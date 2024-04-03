from tkinter import *
from tkinter import ttk
from conexion import *

db = BaseDatos()
modificar = False

# Ventana y tamaño
ventana = Tk()
ventana.title("Empresa S.A")
ventana.geometry("600x500")
ventana.resizable(False, False)

marco = LabelFrame(ventana, text = "Gestion de empleados")
marco.place(x = 50, y = 50, width = 500, height = 400)

# Espacios para escribir
Nombre = StringVar()
Apellido = StringVar()
Telefono = StringVar()
Email = StringVar()

#Label y Entry
lblNombre = Label(marco, text = "Nombre").grid(column = 0, row = 0, padx = 5, pady = 5)
txtNombre = Entry(marco, textvariable = Nombre)
txtNombre.grid(column = 1, row = 0)

lblApellido = Label(marco, text = "Apellido").grid(column = 0, row = 1, padx = 5, pady = 5)
txtApellido = Entry(marco, textvariable = Apellido)
txtApellido.grid(column = 1, row = 1)

lblTelefono = Label(marco, text = "Telefono").grid(column = 2, row = 0, padx = 5, pady = 5)
txtTelefono = Entry(marco, textvariable = Telefono)
txtTelefono.grid(column = 3, row = 0)

lblEmail = Label(marco, text = "Email").grid(column = 2, row = 1, padx = 5, pady = 5)
txtEmail = Entry(marco, textvariable = Email)
txtEmail.grid(column = 3, row = 1)

lblMensaje = Label(marco, text = "Lista de empleados")
lblMensaje.grid(column = 0, row = 2, columnspan = 4)

# Lista
tvEmpleados = ttk.Treeview(marco, selectmode=NONE)
tvEmpleados.grid(column = 0, row = 3, columnspan = 4, padx = 5)
tvEmpleados["columns"]=("ID","Nombre","Apellido","Telefono","Email")
tvEmpleados.column("#0", width = 0, stretch = NO)
tvEmpleados.column("ID", width = 50, anchor = CENTER)
tvEmpleados.column("Nombre", width = 50, anchor = CENTER)
tvEmpleados.column("Apellido", width = 50, anchor = CENTER)
tvEmpleados.column("Telefono", width = 100, anchor = CENTER)
tvEmpleados.column("Email", width = 100, anchor = CENTER)
tvEmpleados.heading("#0", text = "")
tvEmpleados.heading("ID", text = "ID", anchor = CENTER)
tvEmpleados.heading("Nombre", text = "Nombre", anchor = CENTER)
tvEmpleados.heading("Apellido", text = "Apellido", anchor = CENTER)
tvEmpleados.heading("Telefono", text = "Telefono", anchor = CENTER)
tvEmpleados.heading("Email", text = "Email", anchor = CENTER)

# Esta funcion deberia agregar automaticamente informacion de los empleados al seleccionarlos
def seleccionar(event):
    print("Seleccionar empleado")
    if tvEmpleados.selection():
        id = tvEmpleados.selection()[0]
        values = tvEmpleados.item(id, "values")
        print("Valores:", values)
        if values:
            Nombre.set(values[1])
            Apellido.set(values[2])
            Telefono.set(values[3])
            Email.set(values[4])
            modificarTrue()

tvEmpleados.bind("<<TreeviewSelection>>", seleccionar) # No funciona, no tengo idea por que

# Botones de accion

buttonEliminar = Button(marco, text = "Eliminar", command = lambda:eliminar())
buttonEliminar.grid(column = 1, row = 4)
buttonNuevo = Button(marco, text = "Nuevo", command = lambda:nuevo())
buttonNuevo.grid(column = 2, row = 4)
buttonModificar = Button(marco, text = "Modificar", command = lambda:actualizar())
buttonModificar.grid(column = 3, row = 4)

# Funciones para gestionar la base de datos
def agregar():
    vaciar()
    sql = "SELECT * FROM empleados"
    db.cursor.execute(sql)
    filas = db.cursor.fetchall()
    for fila in filas:
        id = fila[0]
        tvEmpleados.insert("", END, id, text = id, values = fila )

def vaciar():
    filas = tvEmpleados.get_children()
    for fila in filas:
        tvEmpleados.delete(fila)

def eliminar():
    if tvEmpleados.selection():
        id = tvEmpleados.selection()[0]
        if int(id)>0:
            sql = "DELETE FROM empleados WHERE ID="+ id
            db.cursor.execute(sql)
            db.connection.commit()
            tvEmpleados.delete(id)
            lblMensaje.config(text = "Se ha eliminado el registro")
        else:
            lblMensaje.config(text="Selecciona un registro para eliminar")
    else:
        lblMensaje.config(text = "No hay elementos seleccionados para eliminar")

def modificarFalse():
    global modificar
    modificar = False
    tvEmpleados.config(selectmode = NONE)
    buttonNuevo.config(text = "Nuevo")
    buttonModificar.config(text = "Modificar")
    buttonEliminar.config(state = DISABLED)
    
def modificarTrue():
    global modificar
    modificar = True
    tvEmpleados.config(selectmode = BROWSE)
    buttonNuevo.config(text = "Cancelar")
    buttonModificar.config(text = "Actualizar")
    buttonEliminar.config(state = NORMAL)

def nuevo():
    if modificar == False:
        if validar():
            val = (Nombre.get(),Apellido.get(),Telefono.get(),Email.get())
            sql = "INSERT INTO empleados (nombre, apellido, telefono, email) VALUES(%s,%s,%s,%s)"
            db.cursor.execute(sql, val)
            db.connection.commit()
            lblMensaje.config(text = "¡Registro agregado correctamente!")
            agregar()
            limpiar()
        else:
            lblMensaje.config(text = "Rellene todos los campos", fg = "red")
    else:
        modificarFalse()
        

def actualizar():
    if modificar == True:
        if validar():
            val = (Nombre.get(), Apellido.get(), Telefono.get(), Email.get())
            id_seleccionado = tvEmpleados.selection()[0]
            sql = "UPDATE empleados SET nombre = %s, apellido = %s, telefono = %s, email = %s WHERE id = %s"
            db.cursor.execute(sql, val + (id_seleccionado,))
            db.connection.commit()
            lblMensaje.config(text = "Se ha actualizado el registro")
            agregar()
            seleccionar(None)  
            modificarFalse()
            limpiar()
        else:
            lblMensaje.config(text = "Rellene todos los campos", fg = "red")
    else:
        modificarTrue()

def validar():
    return len(Nombre.get()) and len(Apellido.get()) and len(Telefono.get()) and len(Email.get())

def limpiar():
    Nombre.set("")
    Apellido.set("")
    Telefono.set("")
    Email.set("")
    

agregar()
ventana.mainloop()        
        
        



