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
    
    name = input("Ingrese el nombre del usuario: ")
    phone = input("Ingrese el teléfono del usuario: ")
    email = input("Ingrese el email del usuario: ")
    userData = { "nombre": name, "teléfono": phone, "email": email }
    UserList.append(userData)
    print("Usuario añadido correctamente.")

def DeleteUser():
    
    delname = input("Ingrese el nombre del usuario a eliminar: ")
    
    global UserList
    
    UserList = [user for user in UserList if user['name'] != delname]

    print(f"El usuario {delname} ha sido eliminado exitosamente.")


def TrackUser():
    
    trackname = input("Ingrese el nombre del usuario a eliminar: ")

    global UserList
    
    FilteredUsers = [user for user in UserList if user['name'] == trackname]
    
    
    if FilteredUsers:
    
        print(f"Usuario {trackname} encontrado:")
    
    
    else:
    
        print("Usuario no encontrado o no creado.")
            
    for user in FilteredUsers:
        
        print(f"Nombre: {user['name']}")
        print(f"Teléfono: {user['phone']}")
        print(f"Email: {user['email']}")

        
            
def ShowUserList(): 
    
    if not UserList:
         print("La lista de usuarios está vacía.")
         
    else:

        for user in UserList:
            
            print(f"Nombre: {user['name']}")
            print(f"Teléfono: {user['phone']}")
            print(f"Email: {user['email']}")
            print("\n")

def main():
    

    while True:
        
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
       