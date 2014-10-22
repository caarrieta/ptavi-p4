#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco
en UDP simple
"""

import SocketServer
import sys


class SIPRegisterHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        print self.client_address
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print line
            if line != '' :
                Direcciones = {}
                linea = line.split()
                if linea[0] == 'REGISTER':
                    LINE = 'SIP/2.0 OK 200 ' + '\r\n\r\n'
                    self.wfile.write(LINE)
                    Direcciones[linea[2]] = self.client_address[0]
                    print Direcciones
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    puerto = int(sys.argv[1])
    serv = SocketServer.UDPServer(("", puerto), SIPRegisterHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
