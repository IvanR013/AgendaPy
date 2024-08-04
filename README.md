# Agenda de Usuarios

Este es un programa de consola en Python para gestionar una agenda de usuarios. Permite añadir, eliminar, buscar y listar usuarios almacenados en una lista.

## Funcionalidades

- **Añadir Usuario**: Permite ingresar el nombre, teléfono y email de un nuevo usuario.
- **Eliminar Usuario**: Permite eliminar un usuario por su nombre.
- **Buscar Usuario**: Permite buscar y mostrar los detalles de un usuario por su nombre.
- **Listar Usuarios**: Muestra todos los usuarios almacenados en la agenda.

## Requisitos

- Python 3.x

## Instalación

1. Cloná el repositorio:
    
    git clone https://github.com/IvanR013/AgendaPy.git
    
2. Navegá al directorio del proyecto:
    
    cd agenda-usuarios
    

## Uso

1. Ejecutá el script principal:
    
    python main.py
    

2. seguí las instrucciones en la consola para interactuar con el programa.

## Código

El código está dividido en las siguientes funciones:

- **`UserOptions()`**: Muestra las opciones disponibles al usuario.
- **`AddUser()`**: Añade un nuevo usuario a la lista.
- **`DeleteUser()`**: Elimina un usuario de la lista por nombre.
- **`TrackUser()`**: Busca un usuario por nombre y muestra sus detalles.
- **`ShowUserList()`**: Muestra todos los usuarios en la lista.

El programa utiliza una lista llamada `UserList` para almacenar los usuarios, donde cada usuario es representado por un diccionario con las claves `"nombre"`, `"teléfono"`, y `"email"`.

## Ejemplo de Uso


# Añadir un nuevo usuario
Ingrese el nombre del usuario: Juan Pérez
Ingrese el teléfono del usuario: 123456789
Ingrese el email del usuario: juan.perez@example.com
Usuario añadido correctamente.

# Eliminar un usuario
Ingrese el nombre del usuario a eliminar: Juan Pérez
El usuario Juan Pérez ha sido eliminado exitosamente.

# Buscar un usuario
Ingrese el nombre del usuario a buscar: Juan Pérez
*Muestra al usuario/Usuario no encontrado o no creado.

# Listar todos los usuarios
Nombre: Juan Pérez
Teléfono: 123456789
Email: juan.perez@example.com
