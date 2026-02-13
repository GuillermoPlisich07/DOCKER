#CLAVE=$RANDOM
passwd > /dev/null <<EOF
$CLAVE
$CLAVE
EOF
echo "Clave $CLAVE para la maquina " $(hostname) "con la ip " $(hostname -i)