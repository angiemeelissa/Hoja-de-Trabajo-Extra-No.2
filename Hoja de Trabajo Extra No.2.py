import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="AngieMelissa04",
        database="basededatos",
        port=3310
    )

def guardar_datos():
    nombre = entry_nombre.get()
    email = entry_email.get()
    contrasena = entry_contrasena.get()
    fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not nombre or not email or not contrasena:
        messagebox.showerror("¡ERROR!", "Todos Los Campos Son Obligatorios")
        return

    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email, contrasena, fecha_registro) VALUES (%s, %s, %s, %s)",
                       (nombre, email, contrasena, fecha_registro))
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("¡EXITO!", "Todos Los Datos Fueron Guardados Correctamente!")
        entry_nombre.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_contrasena.delete(0, tk.END)
    except mysql.connector.Error as error:
        messagebox.showerror("¡ERROR!", f"No se Pudo Guardar: {error}")

def cancelar():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("APLICACIÓN")
ventana.geometry("400x300")
ventana.configure(bg="#f4f4f4")

lbl_titulo = tk.Label(ventana, text="Ingrese los datos", font=("Arial", 14, "bold"), bg="#f4f4f4")
lbl_titulo.pack(pady=10)

frame_form = tk.Frame(ventana, bg="#f4f4f4")
frame_form.pack(pady=10)

lbl_nombre = tk.Label(frame_form, text="Nombre:", font=("Arial", 10), bg="#f4f4f4")
lbl_nombre.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_nombre = tk.Entry(frame_form, width=30)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

lbl_email = tk.Label(frame_form, text="Email:", font=("Arial", 10), bg="#f4f4f4")
lbl_email.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_email = tk.Entry(frame_form, width=30)
entry_email.grid(row=1, column=1, padx=5, pady=5)

lbl_contrasena = tk.Label(frame_form, text="Contraseña:", font=("Arial", 10), bg="#f4f4f4")
lbl_contrasena.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_contrasena = tk.Entry(frame_form, width=30, show="*")
entry_contrasena.grid(row=2, column=1, padx=5, pady=5)

frame_botones = tk.Frame(ventana, bg="#f4f4f4")
frame_botones.pack(pady=10)

btn_guardar = tk.Button(frame_botones, text="Guardar", font=("Arial", 10), bg="#4CAF50", fg="white", width=10,
                        command=guardar_datos)
btn_guardar.grid(row=0, column=0, padx=10)

btn_cancelar = tk.Button(frame_botones, text="Cancelar", font=("Arial", 10), bg="#F44336", fg="white", width=10,
                         command=cancelar)
btn_cancelar.grid(row=0, column=1, padx=10)

ventana.mainloop()
