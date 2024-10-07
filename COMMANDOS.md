## Comando principales

- __docker pull [imagen]__
    Este comando sirve para descargar una imagen puede ser una version especifica o la mas reciente si no le aclaramos la version
- __docker images__
    Este comando sirve para ver las imagenes que tenemos en nuestro repositorio
- __docker rmi [tags or names]__
- __docker ps__
- __docker ps -a [-q]__
- __docker stop [ids or names]__
- __docker star [ids or names]__
- __docker run -n nombre_contenedor -d -p XXXX:XX imagen_contenedor__
    Este comando es para incial un contenedor
    -p es para darle el puerto de mi maquina y el puerto del contenedor
    -d es para que el contenedor empiece a correr en el background
    -n nombre de del contenedor
- __docker rm [ids or names]__