import uuid
import os
import platform
import time
import csv

delay = 2

class Animal:
    def __init__(self, nombre, raza, especie, id = str(uuid.uuid4())[0:8]):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.especie = especie
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Especie: {self.especie}"
    

def leer_animales():
    print("Se está leyendo el archivo animales.csv")
    with open("./archivos/animales.csv", "r", newline='') as archivo_animales:
        data = csv.reader(archivo_animales)
        data = list(data)
        
        print("****************INICIO DATOS****************")
        for index, fila in enumerate(data[1:]):
            al = fila[0].split(";")
            # order de parámetros (nombre, raza, especie, id)
            animal = Animal(al[1], al[2], al[3], al[0])
            print(f"Indice: {index+1} -> {animal}")

            
        print("****************FIN DATOS****************\n\n")


def registrar_animal():
    print("Ingrese los datos del nuevo animal:")
    
    nombre = input("Nombre del animal: ")
    raza = input("Raza del animal: ")
    especie = input("Especie del animal: ")
    
    nuevo_animal = Animal(nombre, raza, especie)
    
    with open("./archivos/animales.csv", "a", newline="\n") as archivo_animales:
        writer = csv.writer(archivo_animales, delimiter=";")
        
    
        lista_valores = list(nuevo_animal.__dict__.values())
        writer.writerow(lista_valores)
        print(f"Anima {nuevo_animal.nombre} registrado con éxito.")
    
def salir():
    print("Gracias por utilizar el sistema.")
    
def f_repetir():
    opcion = input("Si desea volver al menú ingrese [s], de lo contrario, presione cualquier tecla: ")     
    if opcion.lower() == "s":
        limpiar_consola()
    
        return True
    else: 
        limpiar_consola()
        return False
    
def limpiar_consola():
    sistema = platform.system()
    
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def menu():
    print("Menú...")
    print("1.- Leer Animales.")
    print("2.- Registrar un nuevo animal.")
    opcion = input("Ingrese la opción: [1, 2]: ")
    limpiar_consola()
    
    if opcion == "1":
        leer_animales()
    elif opcion == "2":
        registrar_animal()
    else: 
        print("Opción inválida.")
        time.sleep(delay)
        limpiar_consola()
        
    


def main():
    repetir = True
    while repetir:
        menu()
        repetir = f_repetir()
        
    salir()
    
main()
    

