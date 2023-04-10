# Barreras en pytom

Los locks, también llamados mutex son objetos con dos estados posibles:   
adquirido o libre. Cuando un thread adquiere la barrera, los demás threads   
que pidan adquirirlo se bloquearán hasta que el thread que lo ha adquirido   
libere la barrera, momento en el cual podrá entrar otro thread. Un mutex se   
usa en programación concurrente para que un solo procesos o hilo en nuestro   
caso pueda tomar un recurso compartido por otros. 

## Eplicacion del codigo

Lo primero es imprtar las librerias, en este caso la "threading" y la "time":
~~~
import threading
from time import sleep
~~~

Creamos un objeto Lock para sincronizar el acceso a la variable compartida:
~~~
mutex = threading.Lock()
~~~

Luego definimos la clase Hilo que hereda de threading.Thread, creamos el Constructor   
de la clase Hilo, llamamos al constructor de la clase base, asignamos el id del hilo  
y aignamos la variable d que será compartida entre los hilos.
~~~
class Hilo(threading.Thread): # Definimos la clase Hilo que hereda de threading.Thread
    def __init__(self, id, d): # Constructor de la clase Hilo
        threading.Thread.__init__(self) # Llamamos al constructor de la clase base
        self.id = id # Asignamos el id del hilo
        self.d = d # Asignamos la variable d que será compartida entre los hilos
~~~

Definimos el metodo que se ejecuta cuando se inicia el hilo( detro de la clase Hilo)  
bloqueamos el acceso a la variable compartida con `mutex.acquire()`, simulamos un proceso  
que tarda 3 segundos menos el id del hilo, imprimimos un mensaje que indica el id del hilo   
y el valor de la variable compartida y desbloqueamos el acceso a la variable compartida.

~~~
def run(self): # Método que se ejecuta cuando se inicia el hilo
        mutex.acquire() # Bloqueamos el acceso a la variable compartida
        sleep(3 - self.id) # Simulamos un proceso que tarda 3 segundos menos el id del hilo
        print("Soy el hilo %s y la variable d tiene el valor %s" % (self.id, self.d)) # Imprimimos un mensaje que indica el id del hilo y el valor de la variable compartida
        mutex.release() # Desbloqueamos el acceso a la variable compartida
~~~
Definimos la variable compartida `d = 1`

Creamos una lista de instancias de la clase Hilo con diferentes ids:

~~~
hilos = [Hilo(1, d), Hilo(2, d), Hilo(3, d)]
~~~
Al final solo ejecutamos el codigo:

~~~
for h in hilos:
    h.start() # Iniciamos cada hilo

for h in hilos:
    h.join() # Esperamos a que cada hilo termine antes de continuar
~~~
