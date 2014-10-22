#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.


# Dirección IP del servidor.
point = sys.argv
SERVER = point[1]
PORT = int(point[2])


# Contenido que vamos a enviar
if point[3] == 'register':
    LINE = 'REGISTER sip: ' + point[4] + ' SIP/2.0 ' + point[5] '\r\n\r\n'
    #REGISTER sip:luke@polismassa.com SIP/2.0\r\n\r\n

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))


print "Enviando: " + LINE
my_socket.send(LINE + '\r\n')
data = my_socket.recv(1024)
print data

#print 'Recibido -- ', data
#print "Terminando socket..."

# Cerramos todo
#my_socket.close()
#print "Fin."
