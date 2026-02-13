FROM python:3.10-alpine

#Creacion de una directorio de trabajo en docker
WORKDIR /code

#Variables de entorno de Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

#Ejecucion de comandos para instalar dependencias
RUN apk add --no-cache gcc musl-dev linux-headers

#Copio los archivos de requerimientos al contenedor
COPY requirements.txt requirements.txt

#Instalo las dependencias de python
RUN pip install -r requirements.txt

#Exposicion del puerto 5000
EXPOSE 5000

#Copio el contenido del directorio actual al contenedor
COPY . .

#Comando por defecto para ejecutar la aplicacion flask
CMD ["flask", "run", "--debug"]