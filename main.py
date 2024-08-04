# Agenda de usuarios

UserList = []

def UserOptions():
    print("1. Añadir usuario")
    print("2. Eliminar usuario")
    print("3. Buscar usuario")
    print("4. Listar usuarios")
    print("5. Salir")
    print("\n")

def AddUser():
    name = input("Ingrese el nombre del usuario: ").strip()
    phone = input("Ingrese el teléfono del usuario: ").strip()
    email = input("Ingrese el email del usuario: ").strip()
    
    # Verifica que los campos no estén vacíos
    if not name or not phone or not email:
        print("Todos los campos son obligatorios.")
        return
    
    # Crea un diccionario con las claves correctas
    userData = { "nombre": name, "teléfono": phone, "email": email }
    
    # Añade el diccionario a la lista de usuarios
    UserList.append(userData)
    
    print("Usuario añadido correctamente.")
    print("\n")

def DeleteUser():
    delname = input("Ingrese el nombre del usuario a eliminar: ").strip()
    global UserList
    UserList = [user for user in UserList if user['nombre'] != delname]
    print(f"El usuario {delname} ha sido eliminado exitosamente.")

def TrackUser():
    trackname = input("Ingrese el nombre del usuario que desea buscar: ").strip()
    global UserList
    FilteredUsers = [user for user in UserList if user['nombre'] == trackname]
    if FilteredUsers:
        print(f"Usuario {trackname} encontrado:")
        for user in FilteredUsers:
            print(f"Nombre: {user['nombre']}")
            print(f"Teléfono: {user['teléfono']}")
            print(f"Email: {user['email']}")
    else:
        print("Usuario no encontrado o no creado.")

def ShowUserList():
    if not UserList:
        print("La lista de usuarios está vacía.")
    else:
        for user in UserList:
            print(f"Nombre: {user['nombre']}")
            print(f"Teléfono: {user['teléfono']}")
            print(f"Email: {user['email']}")
            print("\n")

def main():
    while True:
        print("Bienvenido a su agenda de contactos!")
        print("\n")
        UserOptions()
        options = int(input("Ingrese una opción: "))
        if options == 1:
            AddUser()
        elif options == 2:
            DeleteUser()
        elif options == 3:
            TrackUser()
        elif options == 4:
            ShowUserList()
        elif options == 5:
            print("Fin del Programa.")
            break
        else:
            print("Por favor, Ingrese una opción válida.")
       
if __name__ == "__main__":
    main()
