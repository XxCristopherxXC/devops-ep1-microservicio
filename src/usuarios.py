usuarios = []

def agregar_usuario(nombre, email):
    usuario = {"id": len(usuarios) + 1, "nombre": nombre, "email": email}
    usuarios.append(usuario)
    return usuario

def obtener_usuarios():
    return usuarios
