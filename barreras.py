import threading
from time import sleep

mutex = threading.Lock() # Creamos un objeto Lock para sincronizar el acceso a la variable compartida

class Hilo(threading.Thread): # Definimos la clase Hilo que hereda de threading.Thread
    def __init__(self, id, d): # Constructor de la clase Hilo
        threading.Thread.__init__(self) # Llamamos al constructor de la clase base
        self.id = id # Asignamos el id del hilo
        self.d = d # Asignamos la variable d que será compartida entre los hilos

    def run(self): # Método que se ejecuta cuando se inicia el hilo
        mutex.acquire() # Bloqueamos el acceso a la variable compartida
        sleep(3 - self.id) # Simulamos un proceso que tarda 3 segundos menos el id del hilo
        print("Soy el hilo %s y la variable d tiene el valor %s" % (self.id, self.d)) # Imprimimos un mensaje que indica el id del hilo y el valor de la variable compartida
        mutex.release() # Desbloqueamos el acceso a la variable compartida

d = 1 # Definimos la variable compartida
hilos = [Hilo(1, d), Hilo(2, d), Hilo(3, d)] # Creamos una lista de instancias de la clase Hilo con diferentes ids

for h in hilos:
    h.start() # Iniciamos cada hilo

for h in hilos:
    h.join() # Esperamos a que cada hilo termine antes de continuar