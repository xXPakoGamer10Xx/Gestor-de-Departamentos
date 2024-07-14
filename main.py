import mysql.connector
from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta
import subprocess
import tempfile
import os
from num2words import num2words
from contrato import obtener_texto_contrato

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title('Gestión de Arrendadores')
        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        Button(self.root, text='Imprimir Contrato', command=self.imprimir_contrato).pack(pady=10)
        Button(self.root, text='Ingresar un nuevo cliente', command=self.registro).pack(pady=10)
        Button(self.root, text='Editar un cliente', command=self.editar_cliente).pack(pady=10)
        Button(self.root, text='Mostrar clientes', command=self.mostrar_clientes).pack(pady=10)
        Button(self.root, text='Borrar', command=self.eliminar_cliente).pack(pady=10)
        Button(self.root, text='Salir', command=self.root.quit).pack(pady=10)

    def no_implementado(self):
        messagebox.showinfo("Información", "Función no implementada aún.")

    def registro(self):
        self.limpiar_pantalla()
        self.formulario_cliente()

    def formulario_cliente(self, cliente=None):
        self.nombre_arrendador = StringVar()
        self.apellidos_arrendador = StringVar()
        self.costo = DoubleVar()
        self.telefono = StringVar()
        self.fecha_inicio = StringVar()
        self.fecha_fin = StringVar()
        self.nombre_fiador = StringVar()
        self.apellidos_fiador = StringVar()
        self.telefono_fiador = StringVar()
        self.observaciones = StringVar()

        if cliente:
            self.nombre_arrendador.set(cliente[1])
            self.apellidos_arrendador.set(cliente[2])
            self.costo.set(cliente[3])
            self.telefono.set(cliente[4])
            self.fecha_inicio.set(cliente[5])
            self.fecha_fin.set(cliente[6])
            self.nombre_fiador.set(cliente[7])
            self.apellidos_fiador.set(cliente[8])
            self.telefono_fiador.set(cliente[9])
            self.observaciones.set(cliente[10])

        Label(self.root, text='Ingresa el nombre del arrendador:').pack(pady=5)
        Entry(self.root, textvariable=self.nombre_arrendador).pack(pady=5)
        Label(self.root, text='Ingresa los apellidos del arrendador:').pack(pady=5)
        Entry(self.root, textvariable=self.apellidos_arrendador).pack(pady=5)
        Label(self.root, text='Ingresa el costo del arrendamiento:').pack(pady=5)
        Entry(self.root, textvariable=self.costo).pack(pady=5)
        Label(self.root, text='Ingresa el teléfono del arrendador (solo 10 dígitos):').pack(pady=5)
        Entry(self.root, textvariable=self.telefono).pack(pady=5)
        Label(self.root, text='Ingrese la fecha de inicio del contrato (YYYY-MM-DD) o deje en blanco para la fecha actual:').pack(pady=5)
        Entry(self.root, textvariable=self.fecha_inicio).pack(pady=5)
        Label(self.root, text='Ingrese la fecha de término del contrato (YYYY-MM-DD) o deje en blanco para un año después de la fecha de inicio:').pack(pady=5)
        Entry(self.root, textvariable=self.fecha_fin).pack(pady=5)
        Label(self.root, text='Ingrese el nombre del fiador (puede dejarlo en blanco):').pack(pady=5)
        Entry(self.root, textvariable=self.nombre_fiador).pack(pady=5)
        Label(self.root, text='Ingrese los apellidos del fiador (puede dejarlo en blanco):').pack(pady=5)
        Entry(self.root, textvariable=self.apellidos_fiador).pack(pady=5)
        Label(self.root, text='Ingrese el teléfono del fiador (solo 10 dígitos, puede dejarlo en blanco):').pack(pady=5)
        Entry(self.root, textvariable=self.telefono_fiador).pack(pady=5)
        Label(self.root, text='¿Tienes observaciones? (puede dejarlo en blanco):').pack(pady=5)
        Entry(self.root, textvariable=self.observaciones).pack(pady=5)

        if cliente:
            Button(self.root, text='Guardar Cambios', command=lambda: self.guardar_datos(cliente[0])).pack(pady=10)
        else:
            Button(self.root, text='Guardar', command=self.guardar_datos).pack(pady=10)
        
        Button(self.root, text='Volver', command=self.main_menu).pack(pady=10)

    def guardar_datos(self, cliente_id=None):
        nombre_arrendador = self.nombre_arrendador.get().upper()
        apellidos_arrendador = self.apellidos_arrendador.get().upper()
        costo = self.costo.get()
        telefono = self.telefono.get()
        fecha_inicio = self.fecha_inicio.get()
        fecha_fin = self.fecha_fin.get()
        nombre_fiador = self.nombre_fiador.get().upper() or None
        apellidos_fiador = self.apellidos_fiador.get().upper() or None
        telefono_fiador = self.telefono_fiador.get() or None
        observaciones = self.observaciones.get().upper() or None

        if not fecha_inicio:
            fecha_inicio = datetime.now().strftime('%Y-%m-%d')
        if not fecha_fin:
            fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            fecha_fin = (fecha_inicio_dt + timedelta(days=365)).strftime('%Y-%m-%d')
        
        if len(telefono) != 10 or not telefono.isdigit():
            messagebox.showerror("Error", "El teléfono debe tener exactamente 10 dígitos y debe ser numérico.")
            return
        if telefono_fiador and (len(telefono_fiador) != 10 or not telefono_fiador.isdigit()):
            messagebox.showerror("Error", "El teléfono del fiador debe tener exactamente 10 dígitos y debe ser numérico.")
            return

        db = Db()
        db.conectar()
        cursor = db.conexion.cursor()
        
        if cliente_id:
            cursor.execute(
                "UPDATE Departamentos SET NombreArrendador=%s, ApellidosArrendador=%s, Costo=%s, NumeroTelefono=%s, FechaInicio=%s, FechaFin=%s, NombreFiador=%s, ApellidosFiador=%s, NumeroFiador=%s, Observaciones=%s WHERE ID=%s",
                (nombre_arrendador, apellidos_arrendador, costo, telefono, fecha_inicio, fecha_fin, nombre_fiador, apellidos_fiador, telefono_fiador, observaciones, cliente_id)
            )
        else:
            cursor.execute(
                "INSERT INTO Departamentos (NombreArrendador, ApellidosArrendador, Costo, NumeroTelefono, FechaInicio, FechaFin, NombreFiador, ApellidosFiador, NumeroFiador, Observaciones) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (nombre_arrendador, apellidos_arrendador, costo, telefono, fecha_inicio, fecha_fin, nombre_fiador, apellidos_fiador, telefono_fiador, observaciones)
            )

        db.conexion.commit()
        cursor.close()
        db.conexion.close()
        messagebox.showinfo("Información", "Los datos se han guardado correctamente.")
        self.main_menu()

    def editar_cliente(self):
        self.limpiar_pantalla()
        db = Db()
        db.conectar()
        cursor = db.conexion.cursor()
        cursor.execute("SELECT * FROM Departamentos")
        clientes = cursor.fetchall()
        cursor.close()
        db.conexion.close()

        Label(self.root, text="Seleccione el cliente que desea editar:").pack(pady=10)
        for cliente in clientes:
            cliente_info = f"ID: {cliente[0]}, Nombre: {cliente[1]} {cliente[2]}, Teléfono: {cliente[4]}"
            Button(self.root, text=cliente_info, command=lambda cliente=cliente: self.formulario_cliente(cliente)).pack(pady=5)

        Button(self.root, text='Volver', command=self.main_menu).pack(pady=10)

    def eliminar_cliente(self):
        self.limpiar_pantalla()
        db = Db()
        db.conectar()
        cursor = db.conexion.cursor()
        cursor.execute("SELECT * FROM Departamentos")
        clientes = cursor.fetchall()
        cursor.close()
        db.conexion.close()

        Label(self.root, text="Seleccione el cliente que desea eliminar:").pack(pady=10)
        for cliente in clientes:
            cliente_info = f"ID: {cliente[0]}, Nombre: {cliente[1]} {cliente[2]}, Teléfono: {cliente[4]}"
            Button(self.root, text=cliente_info, command=lambda cliente_id=cliente[0]: self.confirmar_eliminacion(cliente_id)).pack(pady=5)

        Button(self.root, text='Volver', command=self.main_menu).pack(pady=10)

    def confirmar_eliminacion(self, cliente_id):
        db = Db()
        db.conectar()
        cursor = db.conexion.cursor()
        cursor.execute("DELETE FROM Departamentos WHERE ID=%s", (cliente_id,))
        db.conexion.commit()
        cursor.close()
        db.conexion.close()
        messagebox.showinfo("Información", "Cliente eliminado correctamente.")
        self.eliminar_cliente()

    def mostrar_clientes(self):
        self.limpiar_pantalla()
        db = Db()
        db.conectar()
        cursor = db.conexion.cursor()
        cursor.execute("SELECT * FROM Departamentos")
        clientes = cursor.fetchall()
        cursor.close()
        db.conexion.close()

        Label(self.root, text="Clientes registrados:").pack(pady=10)
        for cliente in clientes:
            info_cliente = (
                f"Número de Departamento: {cliente[0]}\n"
                f"Nombre Completo: {cliente[1]} {cliente[2]}\n"
                f"Costo: {cliente[3]}\n"
                f"Teléfono: {cliente[4]}\n"
                f"Fecha de Inicio: {cliente[5]}\n"
                f"Fecha Final: {cliente[6]}\n"
                f"Nombre del Fiador: {cliente[7]}\n"
                f"Apellidos del Fiador: {cliente[8]}\n"
                f"Teléfono del Fiador: {cliente[9]}\n"
                f"Observaciones: {cliente[10]}\n"
                "----------------------------------------"
            )
            Label(self.root, text=info_cliente, justify=LEFT).pack(pady=5)

        Button(self.root, text='Volver', command=self.main_menu).pack(pady=10)

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def imprimir_contrato(self):
        self.limpiar_pantalla()
        db = Db()
        db.conectar()
        cursor = db.conexion.cursor()
        cursor.execute("SELECT * FROM Departamentos")
        clientes = cursor.fetchall()
        cursor.close()
        db.conexion.close()

        Label(self.root, text="Seleccione el cliente para imprimir el contrato:").pack(pady=10)
        for cliente in clientes:
            cliente_info = f"ID: {cliente[0]}, Nombre: {cliente[1]} {cliente[2]}, Teléfono: {cliente[4]}"
            Button(self.root, text=cliente_info, command=lambda cliente=cliente: self.mostrar_vista_previa_contrato(cliente)).pack(pady=5)

        Button(self.root, text='Volver', command=self.main_menu).pack(pady=10)

    def mostrar_vista_previa_contrato(self, cliente):
        # Obtener la fecha actual en el formato deseado
        fecha_inicio = cliente[5].strftime('%d/%m/%Y')
        fecha_fin = cliente[6].strftime('%d/%m/%Y')

        # Convertir el costo a letras
        costo_letras = num2words(cliente[3], lang='es').upper()

        # Obtener el texto del contrato desde contrato.py
        texto_contrato = obtener_texto_contrato(cliente, fecha_inicio, fecha_fin, costo_letras)

        # Mostrar la vista previa del contrato en un cuadro de texto
        self.limpiar_pantalla()
        text_area = Text(self.root, wrap=WORD, width=80, height=30)
        text_area.insert(INSERT, texto_contrato)
        text_area.pack(pady=10)
        
        # Agregar botones para continuar o cancelar la impresión
        Button(self.root, text='Imprimir', command=lambda: self.imprimir(texto_contrato)).pack(pady=5)
        Button(self.root, text='Volver', command=self.imprimir_contrato).pack(pady=5)

    def imprimir(self, texto):
        try:
            # Crear un archivo temporal con el texto del contrato
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(texto)
                temp_file_path = temp_file.name

            # Imprimir el archivo temporal usando lp
            subprocess.run(['lp', temp_file_path], check=True)

            messagebox.showinfo("Información", "El contrato se ha enviado a la impresora.")
        except subprocess.CalledError as e:
            messagebox.showerror("Error", f"Error al imprimir: {e}")
        finally:
            # Eliminar el archivo temporal
            os.remove(temp_file_path)

class Db:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.database = 'departamentos'
        self.conexion = None

    def conectar(self):
        self.conexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            database=self.database
        )

if __name__ == '__main__':
    root = Tk()
    app = Menu(root)
    root.mainloop()