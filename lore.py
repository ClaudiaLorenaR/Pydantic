#Implementación de la libreria pydantic
from pydantic import BaseModel # para hacer serialización y deserialización

class usuario(BaseModel):
    nombre: str
    apellido: str
    edad: int
    correo: str
    
datos = {"nombre": "Andres", "apellido": "García", "edad": 20, "correo": "jQ2Bt@example.com"}

#Crear una instancia de la clase
usuario=usuario(**datos)
print(usuario)
print(usuario.nombre )
