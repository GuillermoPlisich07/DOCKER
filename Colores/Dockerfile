FROM node:12.13

#Creacion de un directorio de trabajo
RUN echo "Creando directorio de trabajo /app"
WORKDIR /app

#Volumen para la persistencia de datos
RUN echo "Creacion del volumen de informacion"
VOLUME "$PWD":/app

#Copiar los ficheros .json
RUN echo "Copiando los ficheros .json"
COPY package*.json ./

#Ejecutar la instalacion de los modulos
RUN echo "Instalacion de los modulos"
RUN npm install

#Exponer el puerto
EXPOSE 3000

#Copiar el resto de ficheros
COPY . .

#Comando para ejecutar la aplicacion
CMD ["npm","run", "start"]