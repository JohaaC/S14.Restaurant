# Restaurante_app – Semana 14

## Información del proyecto

- **Estudiante:** Johana Lorena Castro Alban
- **Asignatura:** Programación Orientada a Objetos
- **Semana:** Semana 14
- **Tema:** Componentes y contenedores en Tkinter
- **Lenguaje:** Python
- **Interfaz gráfica:** Tkinter / ttk
- **Persistencia:** Archivos JSON

---

## Descripción del proyecto

El proyecto restaurante_app es una aplicación desarrollada en Python
que permite gestionar información de un restaurante mediante una
interfaz gráfica creada con Tkinter.

En la Semana 14 se implementan mejoras en la interfaz utilizando
componentes, contenedores y gestores de geometría, con el objetivo
de organizar mejor la información y facilitar la interacción
con el usuario.

La aplicación mantiene una arquitectura modular que separa
la interfaz gráfica, los modelos, los servicios y los archivos
de datos JSON.

---

## Objetivo

Aplicar los fundamentos de componentes y contenedores de Tkinter
para mejorar la interfaz gráfica de restaurante_app, permitiendo
consultar usuarios y gestionar productos mediante operaciones
de registro, consulta, actualización y eliminación.

Además, se busca mantener la separación de responsabilidades
entre la interfaz y la lógica de negocio.

---

## Tecnologías utilizadas

- Python 3
- Tkinter
- ttk
- Archivos JSON
- Programación Orientada a Objetos
- Visual Studio Code
- Git y GitHub

---

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── assets/
│
├── main.py
│
└── README.md
```

---

## Interfaz gráfica

La aplicación utiliza Tkinter y ttk para construir una interfaz
gráfica organizada mediante componentes y contenedores.

### Componentes utilizados

- Labels: para mostrar títulos y textos.
- Entry: para ingresar información de productos.
- Buttons: para ejecutar las operaciones del sistema.
- Frames: para organizar los elementos de la interfaz.
- Treeview: para mostrar información en forma de tabla.
- Combobox: para seleccionar opciones, si corresponde.

### Gestores de geometría

Se utilizan gestores de geometría de Tkinter para organizar
la distribución de los componentes dentro de la ventana.

Entre ellos se encuentran:

- `pack()`
- `grid()`

Los gestores permiten distribuir los formularios, botones
y áreas de información de manera clara y ordenada.

---

## Inicio de sesión

La aplicación mantiene un inicio de sesión mediante una interfaz
gráfica.

El acceso es validado utilizando los servicios del sistema,
manteniendo la separación entre la interfaz y la lógica
de validación.

Después de iniciar sesión correctamente, el usuario puede
acceder a la ventana principal de la aplicación.

---

## Gestión de usuarios

La aplicación permite consultar la información de los usuarios
registrados en el sistema.

La consulta se realiza desde la interfaz gráfica y utiliza
los servicios correspondientes para acceder a los datos.

---

## Gestión de productos

La sección de productos permite realizar operaciones mediante
formularios, botones y componentes gráficos.

### Operaciones implementadas

- **Registrar:** permite ingresar un nuevo producto.
- **Consultar/Cargar:** permite visualizar la información
  de los productos registrados.
- **Actualizar:** permite modificar los datos de un producto.
- **Eliminar:** permite eliminar un producto del sistema.

Las operaciones son ejecutadas mediante botones utilizando
el parámetro `command=` de Tkinter.

La lógica de negocio y las validaciones se mantienen dentro
de `RestauranteServicio`.

---

## Persistencia de datos

El proyecto utiliza archivos JSON para conservar la información
de los productos y usuarios.

### Archivo de productos

```text
datos/productos.json
```

Este archivo permite almacenar la información de los productos
y conservar los cambios realizados desde la aplicación.

La lectura y escritura de los archivos se realiza mediante
los servicios correspondientes, evitando manipular directamente
los archivos JSON desde la interfaz gráfica.

---

## Arquitectura del proyecto

El proyecto mantiene una organización modular:

- **Modelos:** representan las entidades del sistema.
- **Servicios:** contienen la lógica de negocio y la gestión
  de los archivos.
- **Interfaz (ui):** contiene las ventanas y componentes gráficos.
- **Datos:** almacena la información en archivos JSON.
- **main.py:** punto de entrada de la aplicación.

Esta separación permite mantener el código organizado
y facilita su mantenimiento y ampliación.

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone URL_DE_TU_REPOSITORIO
```

### 2. Ingresar a la carpeta del proyecto

```bash
cd restaurante_app
```

### 3. Ejecutar la aplicación

```bash
python main.py
```

También se puede ejecutar desde Visual Studio Code
abriendo el archivo `main.py` y seleccionando la opción
de ejecutar el programa.

---

## ✅ Comprobación del funcionamiento

Para comprobar el funcionamiento de la aplicación se deben
realizar las siguientes acciones:

1. Ejecutar el archivo `main.py`.
2. Iniciar sesión en la aplicación.
3. Acceder a la ventana principal.
4. Consultar la información de los usuarios.
5. Registrar un producto.
6. Consultar un producto existente.
7. Actualizar la información de un producto.
8. Eliminar un producto.
9. Comprobar que los cambios se guarden en el archivo JSON.

---

## Conclusión

El desarrollo de la Semana 14 permite fortalecer los conocimientos
sobre el uso de componentes y contenedores en Tkinter.

La aplicación restaurante_app mejora su interfaz gráfica mediante
una organización más clara de formularios, botones y áreas
de visualización.

Además, se conserva la arquitectura modular y la persistencia
de datos, manteniendo la separación entre la interfaz gráfica
y la lógica de negocio.

---

## Autora

**Johana Lorena Castro Alban**

Proyecto académico – Universidad Estatal Amazónica (UEA).
