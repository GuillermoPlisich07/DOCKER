#Importo las librerias necesarias
import time
import redis
from flask import Flask

#Uso de flask y redis para contar visitas
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

#Funcion para obtener el conteo de visitas con reintentos en caso de fallo de conexion
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

##Redirijo a la ruta raiz y muestro el conteo de visitas
@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello World! I have been seen {count} times.\n'

@app.route('/about')
def about():
    return f'<h1>About Page</h1><p>Hola Guillermo</p>'