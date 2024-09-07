import uuid

class Animal:
    def __init__(self, nombre, raza, especie):
        self.id  = str(uuid.uuid4())[0:8]
        self.nombre = nombre
        self.raza = raza
        self.especie = especie
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Especie: {self.especie}"
        

perro = Animal("Pepito", "Pastor alemán", "Perro")
gato = Animal("Silvestre", "Gato pelo corto", "Gato")
canario = Animal("Piolín", "Canario amarillo", "Canario")

animales = [perro, gato, canario]


def registrar_animales(archivo, lista_animales, formato):
    try: 
        ruta_base= "./archivos/"
        prefijo = str(uuid.uuid4())
        nombre_archivo = f"{prefijo[0:8]}_{archivo}.{formato}"
        path = ruta_base + nombre_archivo
        
        with open(path, "x") as nuevo_archivo:
            # for animal in lista_animales:
            #     nuevo_archivo.write(str(animal)+ "\n")
            nuevo_archivo.write(f"id|nombre|raza|especie\n")
            for animal in lista_animales:
                nuevo_archivo.write(f"{animal.id}|{animal.nombre}|{animal.raza}|{animal.especie}\n")
            
    except Exception as e:
        print("Error al intentar crear el archivo.", e)

def main():
    nombre_archivo = "animales"
    formato = "csv"
    
    registrar_animales(nombre_archivo, animales, formato)
    
main()