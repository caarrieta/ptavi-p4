#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco
en UDP simple
"""

import SocketServer
import sys

PORT = int(sys.argv[1])
agenda = {}

class SIPRegisterHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """
    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        print self.client_address
        self.wfile.write("Hemos recibido tu peticion:\t")
        self.wfile.write('SIP/2.0 200 OK\r\n\r\n')
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            LINE = self.rfile.read()  
            if not LINE:
                break
            print "El cliente nos manda: " + LINE
            CORREO = LINE.split()[1][4:]
            IP = self.client_address[0]
            print "Correo: " + CORREO + " IP: " + IP
            agenda[CORREO] = IP
            print agenda
            
if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    #PORT = int(sys.argv[2])
    serv = SocketServer.UDPServer(("", PORT), SIPRegisterHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
