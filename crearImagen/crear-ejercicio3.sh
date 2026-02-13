
for i in $(seq 1 5); do
	CLAVE_AL=$RANDOM
	docker run -di --name u$i -e CLAVE=$CLAVE_AL -p 2000$i:22 ejercicio:3 > /dev/null
	echo "El contenedor u$i escucha en el puerto 2000$i con la clave $CLAVE_AL"
done
