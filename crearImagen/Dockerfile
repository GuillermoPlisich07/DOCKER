FROM debian:latest

ARG PAQUETE
ARG ENUN

RUN apt-get update && apt-get install -y $PAQUETE 
RUN echo 'echo El ejericio es: $EJERCICIO' >> /root/.bashrc

WORKDIR /var/www/html
COPY index.html .

RUN apt-get install -y ssh && echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config 

EXPOSE 22
ENV CLAVE=root
ENV EJERCICIO=$ENUN
COPY set-clave-root.sh /root/set-clave-root.sh
RUN chmod +x /root/set-clave-root.sh 

ENTRYPOINT ["bash", "-lc", "service ssh restart && /root/set-clave-root.sh && exec bash"]


