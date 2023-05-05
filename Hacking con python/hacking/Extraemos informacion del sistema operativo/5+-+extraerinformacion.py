from subprocess import check_output
import subprocess

sistema = check_output('systeminfo',stderr=subprocess.STDOUT)

registro = open('C:/Users/espar/Escritorio/python/hacking/Extraemos informacion del sistema operativo/registro.txt', 'wb')
registro.write(sistema)
print("Confirmacion de informacion sustraida")
registro.close()