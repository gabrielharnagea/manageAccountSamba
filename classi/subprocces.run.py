import subprocess

class ServerLab:
    def __init__(self):
        self.__logFile = "log.txt"

    def executeCommand(self, command):
        # Esegui il comando utilizzando subprocess.run
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Apri il file di log in modalità append
        with open(self.__logFile, "a") as log:
            # Scrivi nel file di log informazioni sul comando, output e errori
            log.write(f"\n\nComando: {' '.join(command)}\n")
            log.write(f"Output:\n{result.stdout}\n")
            log.write(f"Errore:\n{result.stderr}\n")
            
    def testNetworkCommand(self, ClientCommand):
        # Simula l'esecuzione di un comando ricevuto da un client di rete
        self.executeCommand(ClientCommand)


if __name__ == "__main__":
    # Crea un'istanza di serverLab
    server = ServerLab()

    # Esegui un comando locale
    comandoLocale = ["ls", "-l"]
    server.executeCommand(comandoLocale)

    # Simula l'esecuzione di un comando di rete (sostituisci con l'input reale del client)
    comandoRete = ["echo", "Ciao, server!"]
    server.testNetworkCommand(comandoRete)
