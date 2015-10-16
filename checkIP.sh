#!/bin/bash
#################### INICIO de script #################################
##
##       Este script permite saber cual es la IP
##       con la que nuestra maquina sale a internet
##
#######################################################################

oldip="`cat /root/public.ip`"
newip="`lynx -source http://www.cualesmiip.com/es_index.html | grep '<b>Tu IP real es' | awk '{print $5}'`"

if [ "$oldip" != "$newip" ]
then
echo $newip > /root/public.ip
echo Mensaje enviado automáticamente por: $HOSTNAME | mail -a "From:Servidor     `echo $HOSTNAME`" -s "La IP ha cambiado `echo $newip`" root
else
echo Mensaje enviado automáticamente por: $HOSTNAME | mail -a "From:Servidor     `echo $HOSTNAME`" -s "La IP no ha cambiado `echo $oldip`" root
fi
exit 0

#################### FIN de script ###################################
