import tkinter as tk

from tkinter import ttk, messagebox


class MainView:

    def __init__(
        self,
        root,
        restaurante_servicio,
        mostrar_login
    ):

        self.root = root
        self.servicio = restaurante_servicio
        self.mostrar_login = mostrar_login

        self.crear_interfaz()

        self.cargar_productos()

    def crear_interfaz(self):

        self.root.configure(
            bg="#f2f4f7"
        )

        contenedor = ttk.Frame(
            self.root,
            padding=15
        )

        contenedor.pack(
            fill="both",
            expand=True
        )

        encabezado = ttk.Frame(
            contenedor
        )

        encabezado.pack(
            fill="x",
            pady=(0, 15)
        )

        ttk.Label(
            encabezado,
            text="GESTIÓN DE RESTAURANTE",
            font=("Arial", 18, "bold")
        ).pack(
            side="left"
        )

        ttk.Button(
            encabezado,
            text="Cerrar sesión",
            command=self.mostrar_login
        ).pack(
            side="right"
        )

        formulario = ttk.LabelFrame(
            contenedor,
            text="Información del producto",
            padding=10
        )

        formulario.pack(
            fill="x",
            pady=(0, 10)
        )

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.nombre_entry = ttk.Entry(
            formulario,
            width=25
        )

        self.nombre_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Categoría:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.categoria_entry = ttk.Entry(
            formulario,
            width=25
        )

        self.categoria_entry.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.precio_entry = ttk.Entry(
            formulario,
            width=25
        )

        self.precio_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Cantidad:"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.cantidad_entry = ttk.Entry(
            formulario,
            width=25
        )

        self.cantidad_entry.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

        botones = ttk.Frame(
            contenedor
        )

        botones.pack(
            fill="x",
            pady=5
        )

        ttk.Button(
            botones,
            text="Registrar",
            command=self.registrar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            botones,
            text="Actualizar",
            command=self.actualizar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            botones,
            text="Eliminar",
            command=self.eliminar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_formulario
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            botones,
            text="Consultar usuarios",
            command=self.mostrar_usuarios
        ).pack(
            side="right",
            padx=5
        )

        tabla_frame = ttk.LabelFrame(
            contenedor,
            text="Productos registrados",
            padding=10
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            pady=10
        )

        columnas = (
            "id",
            "nombre",
            "categoria",
            "precio",
            "cantidad"
        )

        self.tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings",
            height=10
        )

        self.tabla.heading(
            "id",
            text="ID"
        )

        self.tabla.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla.heading(
            "categoria",
            text="Categoría"
        )

        self.tabla.heading(
            "precio",
            text="Precio"
        )

        self.tabla.heading(
            "cantidad",
            text="Cantidad"
        )

        self.tabla.column(
            "id",
            width=40,
            anchor="center"
        )

        self.tabla.column(
            "nombre",
            width=130
        )

        self.tabla.column(
            "categoria",
            width=130
        )

        self.tabla.column(
            "precio",
            width=80,
            anchor="center"
        )

        self.tabla.column(
            "cantidad",
            width=80,
            anchor="center"
        )

        self.tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tabla.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla.bind(
            "<ButtonRelease-1>",
            self.seleccionar_producto
        )

    # -------------------------
    # PRODUCTOS
    # -------------------------

    def cargar_productos(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        productos = self.servicio.obtener_productos()

        for producto in productos:

            self.tabla.insert(
                "",
                "end",
                values=(
                    producto.get("id"),
                    producto.get("nombre"),
                    producto.get("categoria"),
                    f"{producto.get('precio', 0):.2f}",
                    producto.get("cantidad")
                )
            )

    def obtener_datos_formulario(self):

        nombre = self.nombre_entry.get().strip()

        categoria = self.categoria_entry.get().strip()

        precio_texto = self.precio_entry.get().strip()

        cantidad_texto = self.cantidad_entry.get().strip()

        if (
            not nombre
            or not categoria
            or not precio_texto
            or not cantidad_texto
        ):

            messagebox.showwarning(
                "Datos incompletos",
                "Complete todos los campos."
            )

            return None

        try:

            precio = float(precio_texto)

            cantidad = int(cantidad_texto)

            if precio < 0 or cantidad < 0:

                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Datos incorrectos",
                "El precio debe ser decimal y la cantidad entera."
            )

            return None

        return (
            nombre,
            categoria,
            precio,
            cantidad
        )

    def registrar_producto(self):

        datos = self.obtener_datos_formulario()

        if datos is None:
            return

        nombre, categoria, precio, cantidad = datos

        self.servicio.registrar_producto(
            nombre,
            categoria,
            precio,
            cantidad
        )

        messagebox.showinfo(
            "Registro exitoso",
            "El producto fue registrado correctamente."
        )

        self.cargar_productos()

        self.limpiar_formulario()

    def seleccionar_producto(self, event=None):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        item = self.tabla.item(
            seleccion[0]
        )

        valores = item.get("values")

        if not valores:
            return

        self.limpiar_formulario()

        self.id_seleccionado = int(
            valores[0]
        )

        self.nombre_entry.insert(
            0,
            valores[1]
        )

        self.categoria_entry.insert(
            0,
            valores[2]
        )

        self.precio_entry.insert(
            0,
            valores[3]
        )

        self.cantidad_entry.insert(
            0,
            valores[4]
        )

    def actualizar_producto(self):

        if not hasattr(
            self,
            "id_seleccionado"
        ):

            messagebox.showwarning(
                "Selección requerida",
                "Seleccione un producto de la tabla."
            )

            return

        datos = self.obtener_datos_formulario()

        if datos is None:
            return

        nombre, categoria, precio, cantidad = datos

        actualizado = self.servicio.actualizar_producto(
            self.id_seleccionado,
            nombre,
            categoria,
            precio,
            cantidad
        )

        if actualizado:

            messagebox.showinfo(
                "Actualización exitosa",
                "El producto fue actualizado."
            )

            self.cargar_productos()

            self.limpiar_formulario()

        else:

            messagebox.showerror(
                "Error",
                "No se encontró el producto."
            )

    def eliminar_producto(self):

        if not hasattr(
            self,
            "id_seleccionado"
        ):

            messagebox.showwarning(
                "Selección requerida",
                "Seleccione un producto de la tabla."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Desea eliminar el producto seleccionado?"
        )

        if not confirmar:
            return

        eliminado = self.servicio.eliminar_producto(
            self.id_seleccionado
        )

        if eliminado:

            messagebox.showinfo(
                "Eliminación exitosa",
                "El producto fue eliminado."
            )

            self.cargar_productos()

            self.limpiar_formulario()

        else:

            messagebox.showerror(
                "Error",
                "No se encontró el producto."
            )

    def limpiar_formulario(self):

        self.nombre_entry.delete(
            0,
            tk.END
        )

        self.categoria_entry.delete(
            0,
            tk.END
        )

        self.precio_entry.delete(
            0,
            tk.END
        )

        self.cantidad_entry.delete(
            0,
            tk.END
        )

        if hasattr(
            self,
            "id_seleccionado"
        ):

            del self.id_seleccionado

        seleccion = self.tabla.selection()

        for item in seleccion:

            self.tabla.selection_remove(
                item
            )

    # -------------------------
    # USUARIOS
    # -------------------------

    def mostrar_usuarios(self):

        ventana = tk.Toplevel(
            self.root
        )

        ventana.title(
            "Usuarios registrados"
        )

        ventana.geometry(
            "500x300"
        )

        ventana.resizable(
            False,
            False
        )

        frame = ttk.Frame(
            ventana,
            padding=15
        )

        frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "usuario",
            "nombre"
        )

        tabla_usuarios = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings"
        )

        tabla_usuarios.heading(
            "usuario",
            text="Usuario"
        )

        tabla_usuarios.heading(
            "nombre",
            text="Nombre"
        )

        tabla_usuarios.column(
            "usuario",
            width=180
        )

        tabla_usuarios.column(
            "nombre",
            width=180
        )

        tabla_usuarios.pack(
            fill="both",
            expand=True
        )

        usuarios = self.servicio.obtener_usuarios()

        for usuario in usuarios:

            tabla_usuarios.insert(
                "",
                "end",
                values=(
                    usuario.get("usuario"),
                    usuario.get("nombre")
                )
            )