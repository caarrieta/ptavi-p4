#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco
en UDP simple
"""

import SocketServer
import sys
import time


class SIPRegisterHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def register2file(self):
        fichero = open('registered.txt', 'w')
        cadena = 'User' + '\t' + 'IP' + '\t' + 'Expires' '\r\n'
        for x in Direcciones.keys():
            fecha_hora = time.strftime('%Y-%m-%d %H:%M:%S',\
 time.gmtime(Direcciones[x][1]))
            cadena += x + '\t' + Direcciones[x][0] + '\t' + fecha_hora + '\r\n'
        fichero.write(cadena)
        fichero.close()

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.client_address
        for x in Direcciones.keys():
            tiempo_actual = time.time()
            if Direcciones[x][1] < tiempo_actual:
                del Direcciones[x]

        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print line
            if line != '':
                linea = line.split()
                if linea[0] == 'REGISTER':
                    if linea[5] == '0':
                        if linea[2] in Direcciones:
                            del Direcciones[linea[2]]
                    if linea[5] > '0':
                        if not linea[2] in Direcciones:
                            tiempo = float(time.time()) + float(linea[5])
                            Direcciones[linea[2]] = (self.client_address[0],\
tiempo)
                LINE = 'SIP/2.0 OK 200 ' + '\r\n\r\n'
                self.wfile.write(LINE)
            self.register2file()
            if not line:
                break


if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    puerto = int(sys.argv[1])
    serv = SocketServer.UDPServer(("", puerto), SIPRegisterHandler)
    print "Lanzando servidor UDP de eco..."
    Direcciones = {}
    serv.serve_forever()
