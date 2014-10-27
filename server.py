#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco
en UDP simple
"""

import SocketServer
import sys
import time

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
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            LINE = self.rfile.read()  
            if not LINE:
                break
            print "El cliente nos manda: " + LINE
            clients = LINE.split()[1][4:]
            IP = self.client_address[0]
            expires = LINE.split("\r\n")[1][8:]
            metodo = LINE.split("\r\n")[1][:8]
            print "Expires: " + str(expires)
            if metodo == "REGISTER":
                self.buscar_clientes(agenda)
               
                
                if expires == 0:
                    del agenda[clients]
                    print "Eliminamos a: " + clients
                else:
		    total = time.time() + expires
                    caduca = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(total))
                    agenda[clients] = [IP, caduca]

            else:

                self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
                print "Clientes: " + agenda

    def register2file(self):
    #"""
   # Registramos en el fichero a los clientes
    #"""        
        fich = open('registered.txt', 'w')
        fich.write('clients' + '\t' + 'IP' + '\t' + 'Expires' + '\n')
        for clave in agenda.clave():
            ip = agenda[clave][0]
            expire = str(agenda[clave][1])
            fich.write(clave + '\t' + IP + '\t' + expire + '\n')
        fich.close()

    def buscar_clientes(self):

        for clave in agenda.claves():
            if len(cliente) != 16:
                caduca = agenda[clave][1]
                hora = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))
                if caduca <= hora:
                    del agenda[clients]
                    print "Eliminamos a: " + clave
                    self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
        fich.close()

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    #PORT = int(sys.argv[2])
    serv = SocketServer.UDPServer(("", PORT), SIPRegisterHandler)
    print "Lanzando servidor register de SIP...\n"
    serv.serve_forever()
