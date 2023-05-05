import os

print("Ubicacion archivo python: " + os.getcwd())#obtine la ubicacion donde esta el archivo
os.chdir("C:/Users/espar/Escritorio") #cambia la ubicacion donde se pueda ejecutar el archivo
print("Ubicacion actual: " + os.getcwd()) #ubicacion ya cambiada
print(os.listdir(os.getcwd()))#mostrar todos los archivos que se encuentran en la ubicacion, utilizacion para descubrir que archivos hay en el sistema