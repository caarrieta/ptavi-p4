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
            correo = LINE.split()[1][4:]
            IP = self.client_address[0]
            self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
            expires = LINE.split("\r\n")[1][8:]
            metodo = LINE.split("\r\n")[1][:8]
            print "Expires: " + str(expires)

            if metodo == "REGISTER":
                total = time.time() + expires
                caduca = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(total))
                if expires == 0:
                    del agenda[Correo]
                    print "Eliminamos a: " + correo
                else:
                    agenda[correo] = IP

                self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
                self.register2life(correo, IP, caduca)
                print "Todos los Clientes: " + agenda

            print "Buscamos clientes: "
            self.buscar_clientes(agenda)

    def register2life(self, correo, IP, caduca):

        fich = open('registered.txt', 'r+')
        linea = fich.readlines()
        if linea ==[]:
            fich.write('correo' + '\t' + 'IP' + '\t' + 'Expires' + '\n')
        fich.close()

    def buscar_clientes(self, agenda):

        fich = open('registered.txt', 'r')
        linea = fich.readlines()
        for cliente in linea:
            if len(cliente) != 16:
                caduca = cliente.split(' ')[1]
                hora = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))
                hora = hora.split(' ')[1]
                if caduca == hora:
                    correo = cliente.split(' ')[0]
                    print correo
                    del agenda[correo]
                    self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
        fich.close()

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    #PORT = int(sys.argv[2])
    serv = SocketServer.UDPServer(("", PORT), SIPRegisterHandler)
    print "Lanzando servidor register de SIP...\n"
    serv.serve_forever()
