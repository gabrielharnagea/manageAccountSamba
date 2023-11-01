# Il programma invia un saluto al server
#  modifica 3 dortu su branch prova

from classi.send_receve_sock import SRS
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    sr = SRS(s)
    saluto = input("Inserisci stringa: ")
    sr.invia(saluto)
    print( sr.ricevi() )
