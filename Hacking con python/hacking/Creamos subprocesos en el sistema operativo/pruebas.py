import subprocess
import os

esconder = open(os.devnull, 'w')
proceso = subprocess.call(['ping','8.8.8.8'], stdout=esconder, stderr=subprocess.STDOUT)
if proceso == 0:
    print("El proceso se escondio con exito")
else:
    print("salio mal :c")